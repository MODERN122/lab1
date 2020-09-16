from weather import TestProvider
from models import Weather, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('sqlite:///test.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    # Insert a row of data
    provider = TestProvider()
    session.add_all(
        [
            Weather(
                date_time=item['datetime'],
                temperature=item['temp'],
                wind_speed=item['wspd'],
                visibility=item['visibility'],
                humidity=item['humidity'],
                dew=item['dew'],
            )
            for item in provider.get_data('', '', '')
        ],
    )

    for weather in session.query(Weather).order_by(Weather.date_time):
        print(weather)
