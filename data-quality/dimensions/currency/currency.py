# Import modules
import os
import logging
from datetime import datetime, timedelta

from config import FILE_PATH


logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# Define a class for checking data currency
class DataCurrencyChecker:
    # Initialize the class with a file path attribute
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    # Define a method to check if the file exists and handle exceptions
    def check_file_existence(self) -> bool:
        try:
            # Check if the file exists using os.path.isfile()
            if os.path.isfile(self.file_path):
                return True
            else:
                raise FileNotFoundError(f"{self.file_path} does not exist")
        except FileNotFoundError as e:
            # Log the error message using logging.error()
            logging.error(e)
            return False

    # Define a method to check the data currency and handle exceptions
    def check_data_currency(self) -> None:
        try:
            # Check if the file exists using the previous method
            if self.check_file_existence():
                # Get the modification time of the file using os.path.getmtime()
                modification_time = os.path.getmtime(self.file_path)

                # Convert the modification time to a datetime object using datetime.fromtimestamp()
                date_modified: datetime = datetime.fromtimestamp(modification_time)

                # Calculate the time difference between now and the date modified using datetime.now() and timedelta()
                time_diff: timedelta = datetime.now() - date_modified
                print(f"Time difference is: {time_diff}")

                # Check if the data is less than 24 hours old using timedelta(hours=24)
                if time_diff < timedelta(hours=24):
                    print("Data is up-to-date as data is less than 24 hours old")
                else:
                    print("Data is not up-to-date as data is more than 24 hours old")
            else:
                raise Exception(f"Cannot check data currency for {self.file_path}")
        except Exception as e:
            # Log any other exception using logging.exception()
            logging.exception(e)


if __name__ == "__main__":
    # Define the file path as a constant variable using uppercase letters and underscores
    file_path: str = FILE_PATH

    # Create an instance of DataCurrencyChecker class with FILE_PATH as an argument
    data_currency_checker = DataCurrencyChecker(file_path)

    # Call the check_data_currency() method on the instance
    data_currency_checker.check_data_currency()
