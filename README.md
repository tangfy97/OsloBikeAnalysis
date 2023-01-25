# Oslo City Bike Data Analysis
## Prerequisites
First make sure you have installed the following required Python3 packages:
``````python
- pymysql
- csv
- glob
- pandas
- os
``````

## Structure

The project structure:
```
project

│ README.md
│ convert_norsk_char.py
│ load_csv.py
| load_one_csv.py
| create_db.py
| clear_db.py
| calc_trip_time.py
| start2end.py
| start2end.csv

└───origin_csv
│ │ 01.csv
│ │ 02.csv
    ...
│ │ 12.csv
│ │ update.csv


└───processed_csv
│ │ 01.csv
│ │ 02.csv
    ...
│ │ 12.csv
│ │ update.csv

```

## Files description

- `origin_csv`: origin CSV data including 01/2022 - recent (01/2023) data
- `processed_csv`: processed CSV data with transformed Norwegian characters (æ, ø, å) with the English version (ae, oe, aa)
- `convert_norsk_char.py`: transforms Norwegian characters (æ, ø, å) into the English version (ae, oe, aa) 

    **NOTED:** the result is under `processed_csv`, this task can be time-consuming
- `create_db.py`: creates mySQL database `bike_test`
- `load_csv.py`: load processed CSVs into the database
- `load_one_csv.py`: load processed latest CSVs (2023) to database, corresponds to questions in Part 2
- `calc_trip_time.py`: calculate the average trip time for all trips in the year 2022
- `start2end.py`: start and end station pairs, sorted from the most common to the least common, from all trips taken from 2022 to the most recent data, generate `start2end.csv` as output


## Usage

Here we use the instructions for MacOS:

+ Start your mySQL server in Terminal using `mysql -u root -p`.

  **IMPORTANT: Make sure your machine was connected to mySQL server and used the correct credentials** 

+ Run `create_db.py`  to create the database

+ Run `load_csv.py` to load the CSV data to the database, it might take a while (< a few minutes)

  **NOTED:** `filelocation` needs to be replaced to your `dir-to-the-files`

+ Run `calc_trip_time.py` to calculate the average trip time for all trips in the year 2022

+ Run `start2end.py`, start and end station pairs, sorted from the most common to the least common, from all trips taken from 2022 to the most recent data

  **NOTED:** `start2end.csv` is already included -- this step can be skipped

