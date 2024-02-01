
![Ekran görüntüsü 2024-02-01 011814](https://github.com/emirakyer/Data-Engineering-End-to-End-Project---Google-Cloud-dbt-Looker-Studio-Prefect-Terraform/assets/124304427/06b8021a-dc91-4ad9-9b93-b376e66ac8dd)

About Spotify dataset:

This comprehensive dataset delves deeper than your average, unveiling the anatomy of 2023's most celebrated Spotify tracks. It goes beyond basic track information, offering a multifaceted lens into each song's attributes, popularity, and reach across diverse music platforms. 


![Ekran görüntüsü 2024-02-01 011434](https://github.com/emirakyer/Data-Engineering-End-to-End-Project---Google-Cloud-dbt-Looker-Studio-Prefect-Terraform/assets/124304427/b6c18415-5f14-4770-9005-6e1908b92b90)

Dive into details like:

Track Name & Artist(s): Identify the chart-toppers and their creators.
Release Date: Uncover the timeline of musical trends.
Spotify Playlists & Charts: Understand where these tracks get the most love on Spotify.
Streaming Statistics: Gauge the global resonance of each song.
Apple Music & Deezer Presence: See how the song fares across competitor platforms.
Shazam Charts: Discover which tracks get Shazamed the most.
Audio Features: Analyze the music itself, deciphering sonic trends and preferences.


Unleash the Power of Music Data:

Music Analysis: Uncover patterns in audio features, revealing what makes a hit tick.
Platform Comparison: See how popularity translates across different music services.
Artist Impact: Unravel the connection between artist factors and a song's success.
Temporal Trends: Track how musical preferences and sonic landscapes evolve over time.
Cross-Platform Presence: Assess a song's reach and performance across the streaming spectrum.
This robust dataset, brimming with insights, empowers you to understand the heartbeat of popular music like never before. So, get ready to unlock the secrets of 2023's hottest tracks and let the music analysis begin!



![Ekran görüntüsü 2024-02-01 011543](https://github.com/emirakyer/Data-Engineering-End-to-End-Project---Google-Cloud-dbt-Looker-Studio-Prefect-Terraform/assets/124304427/a75b0f7c-b2f0-4d74-877a-1c21872262a9)

Data Source

The data is collected in CSV format using the Kaggle API and orchestrated by Python's Prefect library.



Tech Stack

Data Storage: Google Cloud Storage (GCS)
Data Transformations: Data Build Tool (DBT)
Workflow Orchestration: Prefect
Infrastructure: Terraform
Programming Language: Python
Data Visualization: Looker Studio



Prerequisites

Operating System: Linux preferred
Tools: Python, Terraform, Git
GCP Resources: GCP project, service account, and GCloud CLI



Folder Structure

The prefect folder contains all ELT steps, including Prefect blocks, deployment scripts, and DBT models for data transformation.



End-to-End Pipeline

Here are some key considerations behind the pipeline:
IaC (Terraform) creates the GCS bucket, dataset, and BigQuery tables for data sources.
Since the data was extracted from the Steam API at a specific time, batch processing was chosen for optimized ingestion. Streaming processing is unnecessary in this case.
User review data, ingested into BigQuery and used as DBT sources, is partitioned by the month of review creation. This optimizes query performance when analyzing data within specific timeframes.
Additional Notes
This edit focuses on clarity, conciseness, and technical accuracy while maintaining professionalism.
Feel free to add specific details about the files or pipeline for better context.



Dashboard
https://lookerstudio.google.com/u/0/reporting/4be68e63-9cd8-4a61-9eb4-c9002e3fc420/page/V48nD?s=pnf2o67whBw
![Ekran görüntüsü 2024-02-01 011717](https://github.com/emirakyer/Data-Engineering-End-to-End-Project---Google-Cloud-dbt-Looker-Studio-Prefect-Terraform/assets/124304427/726e9379-8174-4cc3-a7b9-826fabcbcedf)
