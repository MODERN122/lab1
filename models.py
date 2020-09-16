from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer

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
