import pytest
import pandas as pd

filename = "C:/Users/gaura/Desktop/Invsto/dataset.csv"

# Function to simulate data ingestion from CSV
def ingest_data_csv(filename):
    # Simulate reading data from CSV file
    df = pd.read_csv(filename)
    return df

def test_data_ingestion_csv():
    # Path to the downloaded dataset
    filename = "C:/Users/gaura/Desktop/Invsto/dataset.csv"
    
    # Call the data ingestion function
    df = ingest_data_csv(filename)
    
    # Assert that the DataFrame is not empty
    assert not df.empty

if __name__ == "__main__":
    pytest.main([__file__])