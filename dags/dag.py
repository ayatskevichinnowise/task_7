import pandas as pd
import re
import pendulum
from airflow.sensors.filesystem import FileSensor
from airflow.decorators import task_group, task, dag
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


@dag(schedule=None, start_date=pendulum.now(), catchup=False)
def etl():

    @task
    def get_data(path: str) -> pd.DataFrame:
        return pd.read_csv(path)

    @task
    def remove_na(data: pd.DataFrame) -> pd.DataFrame:
        data.dropna(how='all', inplace=True)
        return data

    @task
    def fillna_val(data: pd.DataFrame) -> pd.DataFrame:
        data.fillna('-', inplace=True)
        return data

    @task
    def sort_val(data: pd.DataFrame) -> pd.DataFrame:
        data.sort_values('at', inplace=True)
        return data

    def rep_emo(text: str) -> str:
        regrex_pattern = re.compile(pattern="["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"
            u"\u3030"
                            "]+", flags=re.UNICODE)
        return regrex_pattern.sub(r'', text)

    @task
    def replace_st(data: pd.DataFrame) -> pd.DataFrame:
        data['content'] = data['content'].apply(rep_emo)
        return data

    @task_group
    def all_tasks(data: pd.DataFrame) -> pd.DataFrame:
        return replace_st(sort_val(fillna_val(remove_na(data))))

    @task
    def load_data(data: pd.DataFrame) -> None:
        client = MongoClient(os.getenv('CONNECT'))
        db = client['reviews']['tik_tok']
        db.insert_many(data.to_dict('records'))

    path_to_file = os.getenv('FILE')
    wait_for_file = FileSensor(task_id='wait_for_file',
                               poke_interval=10,
                               filepath=path_to_file
                               )

    data = wait_for_file >> get_data(path_to_file)
    load_data(all_tasks(data))


etl()
