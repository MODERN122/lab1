import json
import sqlite3
from weather import TestProvider

with sqlite3.connect('test.db') as connection:
    c = connection.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS weather
             (date_time text, temperature real, wind_speed real, visibility real, humidity real, dew real)''')

    # Insert a row of data
    provider = TestProvider()
    for item in provider.get_data('','',''):
        c.execute("INSERT INTO weather VALUES (?,?,?,?,?,?)", (item['datetime'], item['temp'], item['wspd'], item['visibility'], item['humidity'], item['dew']))

    for row in c.execute('SELECT * FROM weather ORDER BY date_time'):
        print(row)

