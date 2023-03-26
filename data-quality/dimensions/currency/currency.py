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


class DataCurrencyChecker:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def check_file_existence(self) -> bool:
        try:
            if os.path.isfile(self.file_path):
                return True
            else:
                raise FileNotFoundError(f"{self.file_path} does not exist")
        except FileNotFoundError as e:
            logging.error(e)
            return False

    def check_data_currency(self) -> None:
        try:
            if self.check_file_existence():
                modification_time = os.path.getmtime(self.file_path)

                date_modified: datetime = datetime.fromtimestamp(modification_time)

                time_diff: timedelta = datetime.now() - date_modified
                print(f"Time difference is: {time_diff}")

                if time_diff < timedelta(hours=24):
                    print("Data is up-to-date as data is less than 24 hours old")
                else:
                    print("Data is not up-to-date as data is more than 24 hours old")
            else:
                raise Exception(f"Cannot check data currency for {self.file_path}")
        except Exception as e:
            logging.exception(e)


if __name__ == "__main__":
    file_path: str = FILE_PATH

    data_currency_checker = DataCurrencyChecker(file_path)

    data_currency_checker.check_data_currency()
