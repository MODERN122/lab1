from weather import TestProvider
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, create_engine
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather'
    id = Column('id', Integer, primary_key=True)
    date_time = Column('date_time', String)
    temperature = Column('temperature', Float)
    wind_speed = Column('wind_speed', Float)
    visibility = Column('visibility', Float)
    humidity = Column('humidity', Float)
    dew = Column('dew', Float)

    def __repr__(self):
        return "<Weather id=%d date_time='%s' temperature=%f wind_speed=%f visibility=%f humidity=%f dew=%f>" % (
            self.id,
            self.date_time,
            self.temperature,
            self.wind_speed,
            self.visibility,
            self.humidity,
            self.dew,
        )


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
