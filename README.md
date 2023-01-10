# CSV-to-MySQL

Convert bulk .csv data into MySQL tables. Table names, column names, column types are generated using csv_to_mysql.py.

# USAGE
```md
Required to use:
- MySQL
- Python
    - os
    - pandas
    - mysql.connector
```

```md
- Add your .csv file(s) to the /data folder
- Enter your new database name
- Enter your MySQL credentials
- (Optional) add your primary and foreign keys
- Run python3 csv_to_mysql.py
```