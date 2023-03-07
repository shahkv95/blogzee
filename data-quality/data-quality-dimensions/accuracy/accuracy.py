import pandas as pd
import os
import re
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)


class CustomerData:
    def __init__(self, data: List[Dict[str, str]]):
        self.data = pd.DataFrame(data)

    def read_from_csv(self, file_path: str):
        try:
            self.data = pd.read_csv(file_path)
            logging.info(
                f"Data loaded from {os.path.basename(file_path)} \n"
            )  # logging basename to maintain privacy of absolute location - you can just pass file path
        except FileNotFoundError as e:
            logging.error(f"Error loading data from {file_path}: {e}")
        except pd.errors.EmptyDataError as e:
            logging.error(f"Error loading data from {file_path}: {e}")

    def check_email_accuracy(self):
        email_regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        self.data["is_email_accurate"] = self.data["email"].apply(
            lambda x: bool(re.match(email_regex, x))
        )

    def __repr__(self) -> str:
        return repr(self.data)


if __name__ == "__main__":
    # Initialize customer data object
    customer = CustomerData([])

    customer.read_from_csv("customer_data.csv")

    # Apply the email accuracy check to the data
    customer.check_email_accuracy()

    # Print the data with the new email_accurate column
    print(customer)
