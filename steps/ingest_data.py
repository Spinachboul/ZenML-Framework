import logging
import pandas as pd
from zenml import step

class IngestData:
    # Ingesting the data from the data_path
    def __init__(self, data_path:str):

        """Arguements:
        data_path: Path to the data
        """
        # Create a variable using self
        self.data_path = data_path

    def get_data(self):
        logging.info("Ingesting Data from {self.data_path}")
        return pd.read_csv(self.data_path)
    

@step
def Ingest_data(data_path: str) -> pd.DataFrame:
    """Ingesting the data from the datapath
    Args: 
        data_path: Path to the data
    Returns:
        pd.Dataframe: the ingested data
    """

    try:
        # Create an instance of the class
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting the data {e}")
        raise e
    



    
