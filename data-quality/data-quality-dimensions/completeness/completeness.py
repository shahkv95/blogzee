from typing import List, Dict
import os
import logging
import pandas as pd


logging.basicConfig(level=logging.INFO)


class CustomerData:
    def __init__(self, data: List[Dict[str, str]]):
        self.data = pd.DataFrame(data)

    def read_from_csv(self, file_path: str) -> None:
        try:
            self.data = pd.read_csv(file_path)
            logging.info(f"Data loaded from {os.path.basename(file_path)}\n")
        except (FileNotFoundError, pd.errors.EmptyDataError) as e:
            logging.error(f"Error loading data from {file_path}: {e}\n")

    def check_column_completeness(self, required_columns: List[str]) -> None:
        missing_columns: set = set(required_columns) - set(self.data.columns)
        if missing_columns:
            for column in missing_columns:
                logging.error(
                    f"The following column is missing from the data: {column}\n"
                )
            raise ValueError(f"Missing columns: {', '.join(missing_columns)}\n")
        else:
            logging.info("All required columns are present in the data.\n")

    def check_row_completeness(self, required_columns: List[str]) -> None:
        missing_data = self.data[required_columns].isnull().any(axis=1)
        if missing_data.any():
            logging.error(
                f"The following rows are missing data: {missing_data.index[missing_data]}\n"
            )
            raise ValueError("Missing data in some rows.\n")
        else:
            logging.info("All rows have complete data.\n")

    def __repr__(self) -> str:
        return repr(self.data)


if __name__ == "__main__":
    # Initialize customer data object
    customer_data = CustomerData([])
    customer_data.read_from_csv("./complete_customer_data.csv")

    # Check for completeness of data
    required_columns = ["name", "email", "phone"]  # try adding empty columns
    customer_data.check_column_completeness(required_columns)
    customer_data.check_row_completeness(required_columns)
