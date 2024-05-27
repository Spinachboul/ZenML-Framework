from zenml import pipeline
from steps.ingest_data import Ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluation import evaluate_model
from pydantic import BaseModel
import pandas as pd


@pipeline
def train_pipeline(data_path: str) -> None:
    df = Ingest_data(data_path)
    df = clean_data(df)
    train_model(df)
    evaluate_model(df)
