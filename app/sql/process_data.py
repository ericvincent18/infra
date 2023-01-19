import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# uncomment for local development testing
# sys.path.insert(1, "/Users/ericvincent/infra/infra/app/models")
from models.reviews import Wine

# uncomment for local development testing
# sys.path.insert(1, "/Users/ericvincent/infra/infra/app/config")
from config.env_config import config


class initSession:
    def __init__(self):

        self.engine = create_engine(
            config.db_connection_string, isolation_level="SERIALIZABLE",
        )
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


# Connect to the database
session = initSession()
logging.warning("connected to the db")


class dataProcessing:
    def __init__(self, df: pd.DataFrame):
        self.df = pd.DataFrame(df)

    def formatDf(self):
        self.df = self.df.fillna(0)
        return self.df

    def insert_data(self):

        for index, row in self.df.iterrows():
            wine = Wine(
                points=row["points"],
                title=row["title"],
                description=row["description"],
                taster_name=row["taster_name"],
                taster_twitter_handle=row["taster_twitter_handle"],
                price=row["price"],
                designation=row["designation"],
                variety=row["variety"],
                region_1=row["region_1"],
                region_2=row["region_2"],
                province=row["province"],
                country=row["country"],
                winery=row["winery"],
            )
            session.session.add(wine)
        session.session.commit()
