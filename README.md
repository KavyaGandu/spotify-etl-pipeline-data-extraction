# spotify-etl-pipeline-data-extraction
Spotify ETL pipeline(DATA EXTRACTION)
Spotify ETL Pipeline using AWS Lambda, S3, Glue & Athena

This project automates the extraction, transformation, and loading (ETL) of Spotify playlist data using AWS services. It fetches trending songs from the Spotify API, stores them in AWS S3, processes the data using AWS Lambda, and enables querying with AWS Glue & Athena.

Key Features:
Extracts track, artist, and album data from the Spotify API.
Stores raw data in AWS S3.
Transforms and processes the data using AWS Lambda.
Loads structured data into AWS Glue & Athena for easy querying.
Fully automated ETL workflow with AWS EventBridge scheduling.
