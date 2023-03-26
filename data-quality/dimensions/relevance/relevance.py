import logging
import pandas as pd
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)


class RelevantData:
    def __init__(self, data: pd.DataFrame, date_column: str):
        self.data = data
        self.date_column = date_column

    def filter_by_date_range(self, start_date: str, end_date: str) -> pd.DataFrame:
        try:
            self.data[self.date_column] = pd.to_datetime(self.data[self.date_column])

            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

            data = self.data[
                (self.data[self.date_column] >= start_date)
                & (self.data[self.date_column] <= end_date)
            ]

            logging.info(
                f"\t{len(data)} rows returned for date range: {start_date} - {end_date}\n"
            )
            return data

        except Exception as e:
            logging.exception(f"Error occurred while filtering data by date range: {e}")
            raise


if __name__ == "__main__":
    customer_data = pd.DataFrame(
        {
            "first_name": ["Rajesh", "Amit", "Priya", "Sangeeta", "Pradeep"],
            "last_name": ["Sharma", "Patel", "Singh", "Yadav", "Mishra"],
            "age": [35, 27, 47, 31, 55],
            "date_column": [datetime.now() - timedelta(days=x) for x in range(5)],
        }
    )

    customer_data.to_csv("relevant_customer_data.csv", index=False)

    data = pd.read_csv("relevant_customer_data.csv")

    start_date = "2023-01-01"
    end_date = "2023-03-25"

    relevant_data = RelevantData(data, "date_column")
    filtered_data = relevant_data.filter_by_date_range(start_date, end_date)

    logging.info(f"\n {filtered_data}")
