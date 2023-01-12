from sqlalchemy import Column, Integer, String
from .base import Base


class Wine(Base):
    __tablename__ = "wines"
    points = Column(Integer)
    title = Column(String)
    description = Column(String)
    taster_name = Column(String)
    taster_twitter_handle = Column(String)
    price = Column(Integer)
    designation = Column(String)
    variety = Column(String)
    region_1 = Column(String)
    region_2 = Column(String)
    province = Column(String)
    country = Column(String)
    winery = Column(String)
    id = Column(Integer, primary_key=True)
