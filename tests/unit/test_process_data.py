import unittest

import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# sys.path.insert(1, "/Users/ericvincent/infra/infra/app")

# from models.reviews import Wine
# from models.base import Base

# sys.path.insert(1, "/Users/ericvincent/infra/infra/app")
# from sql.process_data import initSession, dataProcessing

# Base
# session = initSession()


# class TestSessin(unittest.TestCase):
#     def test_initSession(self):
#         # Test that initSession creates an engine and session object
#         s = initSession()
#         self.assertIsNotNone(s.engine)
#         self.assertIsNotNone(s.Session)
#         self.assertIsNotNone(s.session)

# def test_connection(self):
#     # Test that initSession connects to the database
#     s = initSession()
#     try:
#         s.engine.connect()
#         connected = True
#     except Exception as e:
#         connected = False
#     self.assertTrue(connected)


# class TestDataProcessing(unittest.TestCase):
#     def test_formatDf(self):
#         # Test that formatDf correctly fills null values with 0
#         df = pd.DataFrame({"a": [1, 2, None, 4], "b": [None, 2, 3, 4]})
#         dp = dataProcessing(df)
#         formatted_df = dp.formatDf()
#         self.assertEqual(formatted_df["a"].isnull().sum(), 0)
#         self.assertEqual(formatted_df["b"].isnull().sum(), 0)

# def test_insert_data(self):
#     # Test that insert_data correctly inserts data into the database

#     df = pd.DataFrame(
#         {
#             "points": [95],
#             "title": ["Château Margaux"],
#             "description": [
#                 "Aromas of cedar and dark berries with a hint of tobacco and vanilla"
#             ],
#             "taster_name": ["Jane Doe"],
#             "taster_twitter_handle": ["@janedoe"],
#             "price": [250],
#             "designation": ["Grand Vin"],
#             "variety": ["Cabernet Sauvignon"],
#             "region_1": ["Bordeaux"],
#             "region_2": "",
#             "province": ["France"],
#             "country": ["France"],
#             "winery": ["Château Margaux"],
#             "id": [1],
#             "points": [92],
#             "title": ["Château Léoville-Las-Cases"],
#             "description": [
#                 "Full-bodied with a dense tannic structure and flavors of dark fruit and chocolate"
#             ],
#             "taster_name": ["John Smith"],
#             "taster_twitter_handle": ["@johndoe"],
#             "price": [150],
#             "designation": "",
#             "variety": ["Cabernet Sauvignon"],
#             "region_1": ["Bordeaux"],
#             "region_2": "",
#             "province": ["France"],
#             "country": ["France"],
#             "winery": ["Château Léoville-Las-Cases"],
#             "id": [2],
#             "points": [89],
#             "title": ["Château Rauzan-Ségla"],
#             "description": ["Aromas of blackcurrant, plum, and spice with"],
#             "taster_name": ["Jane Doe"],
#             "taster_twitter_handle": ["@janedoe"],
#             "price": [250],
#             "designation": ["Grand Vin"],
#             "variety": ["Cabernet Sauvignon"],
#             "region_1": ["Bordeaux"],
#             "region_2": "",
#             "province": ["France"],
#             "country": ["France"],
#             "winery": ["Château Margaux"],
#             "id": [1],
#         }
#     )

#     dp = dataProcessing(df)
#     dp.formatDf()
#     dp.insert_data()
#     result = session.session.query(Wine).filter_by(points=1).first()
#     self.assertEqual(result.title, "Château Margaux")
