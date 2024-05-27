from pipelines.train_pipeline import train_pipeline
from pydantic import BaseModel
import pandas as pd

class DataFrameModel(BaseModel):
    df: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True


if __name__ == '__main__':
    # load the data into a dataframe
    df = pd.read_csv('C:\\Users\\mridu\\Desktop\\Predictive MLOPs\\heart_attack_prediction_dataset.csv')

    # create a model object
    data = DataFrameModel(df=df)

    # run the pipeline
    train_pipeline(data)

