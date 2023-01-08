import os

from deta import Deta # pip install deta
# from dotenv import load_dotenv
# load_dotenv(".env")
# DETA_KEY = os.getenv("DETA_KEY")

import streamlit as st


DETA_KEY=st.secrets["DETA_KEY"]


#initialise with project key

deta=Deta(DETA_KEY)


db=deta.Base("monthly_reports")

def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
