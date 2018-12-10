import numpy as np
from sklearn.datasets import make_regression
from scipy.stats import norm
import pandas as pd
import sys
import argparse
from sqlalchemy import create_engine
import random

parser = argparse.ArgumentParser()
parser.add_argument(
    'RowCount', type=int, help='The number of rows to generate'
)

args = parser.parse_args()

id_list = []

try:
    print("Creating sqlite3 database")
    sqlite_engine = create_engine('sqlite:///queriosqlite.db')
    print("Sqlite3 database created")
except Error:
    print(e)
    sys.exit(1)



def create_github_stars(rc):

    github_stars_list = []
    github_name_list = []

    for i in range(0, rc):
        github_stars = random.randint(1, 5) * random.randint(1, 9) + 10 * random.randint(1,17)+ random.randint(1,15) / 6
        github_stars = np.floor(github_stars)
        github_stars_list.append(abs(github_stars))
        github_name_list.append("repo #{}".format(str(i)))

    return pd.DataFrame(
        {
        'github_id': id_list, 'stars': github_stars_list, 'link': github_name_list,
        }
    ) 

def create_person_github():
    return pd.DataFrame(
        {
        'person_id': id_list, 'github_id': id_list,
        }
    )


row_count = args.RowCount

for i in range(1, (row_count + 1)):
    id_list.append( i )

age, income = make_regression(row_count, 1, 1, noise=3.3, random_state=42)
age = age.reshape((row_count,))
age = np.log(age * age + 1) * 17 + 20
age = np.floor(age)
income = income * income * 6 + 500

height = norm.rvs(size=row_count, loc=180, scale=10, random_state=42)
xs = -random.randint(0, 20) * income / 10 + age**2 / 2
is_client = (norm.rvs(size=row_count, loc=-100, scale=100) + xs) > 0

github_df = create_github_stars(row_count)

person_df = pd.DataFrame(
    {
        'person_id': id_list, 'age': age, 'height': height,'income': income,
         'is_client': is_client
    }
)
person_github_df = create_person_github()

try:
    print("Adding data to sqlite3...")
    with sqlite_engine.connect() as sqlite_conn, sqlite_conn.begin():
        person_df.to_sql('person', sqlite_conn, if_exists='replace')
        github_df.to_sql('github', sqlite_conn, if_exists='replace')
        person_github_df.to_sql('person_github', sqlite_conn, if_exists='replace')
    print("Added data to sqlite3")
except Error as e:
    print(e)
