import re
import pandas as pd
from faker import Faker
import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


class DataGenerator:
    def __init__(self, locale: str):
        self.fake = Faker(locale=locale)
        self.data = pd.DataFrame(columns=["email", "phone"])

    def generate_data(self, rows: int):
        try:
            for _ in range(rows):
                email = self.fake.email()
                phone = self.fake.phone_number()
                self.data = self.data.append(
                    {"email": email, "phone": phone}, ignore_index=True
                )
            logging.info(f"{rows} rows of sample data generated.")
        except Exception as e:
            logging.error(f"Error generating data: {e}")

    def save_data(self, filename: str):
        try:
            self.data.to_csv(filename, index=False)
            logging.info(f"Sample data saved to {filename}.")
        except Exception as e:
            logging.error(f"Error saving data to {filename}: {e}")

    def load_data(self, filename: str):
        try:
            self.data = pd.read_csv(filename)
            logging.info(f"Data loaded from {filename}.")
        except Exception as e:
            logging.error(f"Error loading data from {filename}: {e}")

    def check_phone_format(self, format: str):
        try:
            self.data["phone_format_valid"] = self.data["phone"].apply(
                lambda x: bool(re.match(format, x))
            )
            logging.info("Phone format checked.")
        except Exception as e:
            logging.error(f"Error checking phone format: {e}")


if __name__ == "__main__":
    generator = DataGenerator(locale="hi_IN")
    generator.generate_data(rows=5)
    generator.save_data("consistent_customer_data.csv")
    generator.load_data("consistent_customer_data.csv")
    generator.check_phone_format("^\d{11}$")
    print(generator.data)
