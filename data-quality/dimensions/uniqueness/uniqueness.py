import pandas as pd
import logging

logging.basicConfig(
    filename="unique_data.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


class UniqueDataChecker:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def check_unique_data(self) -> pd.DataFrame:
        try:
            data = pd.read_csv(self.file_path)

            if data["student_id"].nunique() == data.shape[0]:
                logging.info("No duplicate student IDs found")
            else:
                logging.warning("Duplicate student IDs found")

            if data["name"].nunique() == data.shape[0]:
                logging.info("No duplicate names found")
            else:
                logging.warning("Duplicate names found")

            return data

        except Exception as e:
            logging.error(f"An error occurred while checking unique data: {e}")
            return pd.DataFrame()


if __name__ == "__main__":
    data_checker = UniqueDataChecker("check_unique_data.csv")
    unique_data = data_checker.check_unique_data()
    print(unique_data)
