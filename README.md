# Scheduled Crypto ETL Pipeline

## Overview

This project is a simple **ETL (Extract, Transform, Load) pipeline** that fetches real-time cryptocurrency data from an external API, processes it, and stores the results in structured CSV files. The pipeline is designed to run automatically at scheduled intervals.

## Features

* Fetches real-time crypto market data using an API
* Cleans and transforms raw data into structured format
* Exports processed data to CSV files
* Automated scheduling for periodic data updates
* Handles output directory creation dynamically

## Tech Stack

* Python
* Requests (API calls)
* Pandas (data processing)
* Schedule (automation)
* CSV (data storage)

## Project Structure

```
.
├── app.py
├── requirements.txt
├── output/
│   ├── crypto_data.csv
│   ├── top_10_positive.csv
│   └── top_10_negative.csv
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

## Output

The pipeline generates CSV files inside the `output/` folder containing:

* Latest crypto market data
* Top gainers
* Top losers

## Author

Zain Ali
