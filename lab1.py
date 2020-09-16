from weather import TestProvider
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, create_engine
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///test.db')
    metadata = MetaData()
    weather = Table(
        'weather',
        metadata,
        Column('date_time', String),
        Column('temperature', Float),
        Column('wind_speed', Float),
        Column('visibility', Float),
        Column('humidity', Float),
        Column('dew', Float),
    )
    metadata.create_all(engine)
    with engine.connect() as connection:
        # Insert a row of data
        provider = TestProvider()
        connection.execute(
            weather.insert(),
            [
                {
                    'date_time': item['datetime'],
                    'temperature': item['temp'],
                    'wind_speed': item['wspd'],
                    'visibility': item['visibility'],
                    'humidity': item['humidity'],
                    'dew': item['dew'],
                }
                for item in provider.get_data('', '', '')
            ],
        )

        for row in connection.execute(select([weather])):
            print(row)
