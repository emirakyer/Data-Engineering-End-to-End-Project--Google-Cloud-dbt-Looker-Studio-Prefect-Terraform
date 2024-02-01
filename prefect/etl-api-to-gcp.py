from pathlib import Path
import pandas as pd
import kaggle
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket

@task(retries=3, log_prints=True)
def download_data(dataset_kaggle: str) -> None:
    """Download Data from Kaggle

    Args:
        dataset_kaggle (str): Direction of Kaggle Data Source
    """
    print('Downloading file from Kaggle..........')
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_kaggle, path='../data/', unzip=True)
    print('File downloaded to the destination Dir..........')

# Internal function call
def local_path(dataset_file: str) -> Path:
    return Path(f'../data/{dataset_file}').as_posix()

# Internal function call
def remote_path(dataset_file: str) -> Path:
    return Path(f'data/{dataset_file}').as_posix()

@flow(name='Subflow fetchData', retries=3, log_prints=True)
def transform_data(dataset_kaggle: str, dataset_file: str) -> pd.DataFrame:
    download_data(dataset_kaggle)
    path = local_path(dataset_file)

    df = pd.read_csv(path, encoding='iso-8859-1')
    df.columns = df.columns.str.replace(' ', '').str.replace('\(', '').str.replace('\)', '').str.replace('%', '').str.replace('_', '')
    df = df[df['streams'] != 'BPM110KeyAModeMajorDanceability53Valence75Energy69Acousticness7Instrumentalness0Liveness17Speechiness3']
    df = df.dropna(subset=['streams', 'indeezerplaylists', 'inshazamcharts'])
    df["streams"] = df["streams"].astype('int64')
    df["indeezerplaylists"] = df["indeezerplaylists"].str.replace(',', '').astype('int64')
    df["inshazamcharts"] = df["inshazamcharts"].str.replace(',', '').astype('int64')

    print(df.columns)
    return df


@task(retries=3, log_prints=True)
def write_local(df: pd.DataFrame, dataset_file: str) -> None:
    df.columns = df.columns.str.replace(' ', '').str.replace('\(', '').str.replace('\)', '').str.replace('%', '').str.replace('_', '')
    df.to_parquet(local_path(dataset_file))
    print('Writing to local Dir in parquet extension.......')

@task(retries=3, log_prints=True)
def write_gcs(local_path: Path, remote_path: Path) -> None:
    print("Uploading file to GCS")
    gcs_block = GcsBucket.load("zoom-gcs-2")
    gcs_block.upload_from_path(from_path=f"{local_path}", to_path=remote_path)
    print("Uploaded file to GCS")
    return

@flow(name='EL API TO GCP')
def etl_web_to_gcs() -> None:
    dataset_file = 'spotify-2023.csv'
    dataset_file_parquet = 'spotify-2023.parquet'
    dataset_kaggle = 'nelgiriyewithana/top-spotify-songs-2023'

    df = transform_data(dataset_kaggle, dataset_file)
    write_local(df, dataset_file_parquet)
    write_gcs(local_path(dataset_file_parquet), remote_path(dataset_file_parquet))

if __name__ == '__main__':
    """Principal MAIN"""
    etl_web_to_gcs()
