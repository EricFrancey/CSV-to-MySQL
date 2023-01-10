############################################################################################
# USE TO INSERT DATA FROM CSV INTO LOCAL MYSQL SERVER

# ADD YOUR CSV FILES TO /data
# INSERT YOUR INFORMATION WHERE INDICATED BETWEEN < >
# ADD YOUR PRIMARY AND FOREIGN KEYS EXTERNALLY OR AT THE BOTTOM OF THIS CODE
############################################################################################

import os
import pandas as pd
import mysql.connector

############################################################################################
# MYSQL CONNECT
# ENTER YOUR CREDENTIALS AND DATABASE NAME BELOW

#######################################
# DO NOT UPLOAD YOUR PASSWORDS ONLINE #
#######################################
database = '<database_name>'
db = mysql.connector.connect(
  host= 'localhost',
  user= 'root',
  password= '<password>'
)
############################################################################################
# USE TO RESET
# cursor.execute("DROP DATABASE IF EXISTS " + database)
############################################################################################

# DATABASE
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS " + database)
cursor.execute("USE " + database)

# GET TABLE NAME AND DATA
for x in os.listdir('data'):
    tableName = x.split('.')[0]
    df = pd.read_csv(f'data/{x}')
    tableFields = df.columns
    numFields = len(df.columns)
    typeSQL = ""
    stringSQL = ""
    stringValPlaceholder = ""
  
    # SET DATA
    for y in range(len(tableFields)):

        # SET COLUMN NAMES
        if y == len(tableFields) - 1:
            stringSQL += f"{tableFields[y]} "
        else:
            stringSQL += f"{tableFields[y]}, "

        # SET NUMBER VALUES
        if y == len(tableFields) - 1:
            stringValPlaceholder += "%s"
        else:
            stringValPlaceholder += "%s,"

        # SET DATA TYPES
        if df.dtypes[y] == "int64":
            if y == len(tableFields) - 1:  
                typeSQL += f"{tableFields[y]} INT"
            else:
                typeSQL += f"{tableFields[y]} INT, "

        elif df.dtypes[y] == "float64":
            if y == len(tableFields) - 1: 
                typeSQL += f"{tableFields[y]} DECIMAL"
            else:
                typeSQL += f"{tableFields[y]} DECIMAL, "
      
        elif df.dtypes[y] == "object":
            if y == len(tableFields) - 1:
                typeSQL += f"{tableFields[y]} VARCHAR(1000)"
            else:
                typeSQL += f"{tableFields[y]} VARCHAR(1000), "

    # GENERATE TABLES
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tableName} ({typeSQL})''')
    for row in df.itertuples():
        preval = []
        for x in range(1, len(row)):
            preval.append((row[x]))
        val = tuple(preval)
        print(val)
        sql = (f'''INSERT INTO {tableName} ({stringSQL}) VALUES ({stringValPlaceholder})''')  
        cursor.execute(sql,val)   


############################################################################################

# ADD YOUR PRIMARY AND FOREIGN KEYS BELOW

# cursor.execute('''ALTER TABLE <table_name>
#                   ADD PRIMARY KEY AUTO_INCREMENT (<primary_key>),
#                   ADD FOREIGN KEY (<foreign_key>) REFERENCES <foreign_table_name>(<reference>)''')

############################################################################################

# COMMIT AND CLOSE DB
db.commit()
cursor.close()
db.close()

print("\nDatabase seeded.\n")