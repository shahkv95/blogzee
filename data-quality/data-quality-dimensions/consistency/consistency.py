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


# import re
# import pandas as pd
# from faker import Faker
# import logging


# class DataProcessor:
#     def __init__(self, locale: str = "hi_IN") -> None:
#         self.locale = locale
#         self.fake = Faker(locale=self.locale)
#         self.logger = logging.getLogger(__name__)
#         self.data = pd.DataFrame(columns=["email", "phone"])

#     def generate_sample_data(self, n: int = 100) -> None:
#         """
#         Generate n rows of sample data and save it to a CSV file
#         """
#         for _ in range(n):
#             email = self.fake.email()
#             phone = self.fake.phone_number()
#             self.data = pd.concat(
#                 [self.data, pd.DataFrame(
#                     {"email": [email], "phone": [phone]})],
#                 ignore_index=True,
#             )
#         self.data.to_csv("consistent_customer_data.csv", index=False)
#         self.logger.info(
#             f"{n} rows of sample data generated and saved to consistent_customer_data.csv file."
#         )

#     def check_phone_format(self, format: str) -> pd.DataFrame:
#         """
#         Check if the phone number column in the dataframe matches the given format

#         Args:
#             format : str : regular expression format for the phone number

#         Return:
#             pd.DataFrame : with new column "phone_format_valid" indicating if the phone number is in the correct format
#         """
#         try:
#             self.data["phone_format_valid"] = self.data["phone"].apply(
#                 lambda x: bool(re.match(format, x))
#             )
#             self.logger.info(f"Checked phone number format using {format}")
#             return self.data
#         except Exception as e:
#             self.logger.error(
#                 f"Error occurred while checking phone number format: {e}")
#             raise


# if __name__ == "__main__":
#     logging.basicConfig(
#         level=logging.INFO
#     )
#     dp = DataProcessor(locale="hi_IN")


# import re
# import pandas as pd
# from faker import Faker

# # Create an instance of the Faker library
# fake = Faker(locale="hi_IN")

# # Create an empty dataframe to store the data
# data = pd.DataFrame(columns=["email", "phone"])

# # Generate 100 rows of sample data
# for _ in range(5):
#     email = fake.email()
#     phone = fake.phone_number()
#     data = data.append({"email": email, "phone": phone}, ignore_index=True)

# # Save the data to a CSV file
# data.to_csv("consistent_customer_data.csv", index=False)

# print("Sample data generated and saved to consistent_customer_data.csv file.")

# # Load the data from a CSV file
# data = pd.read_csv("consistent_customer_data.csv")


# def check_phone_format(data: pd.DataFrame, format: str) -> pd.DataFrame:
#     """
#     Check if the phone number column in the dataframe matches the given format

#     Args:
#         data : pd.DataFrame
#         format : str : regular expression format for the phone number

#     Return:
#         pd.DataFrame : with new column "phone_format_valid" indicating if the phone number is in the correct format
#     """
#     data["phone_format_valid"] = data["phone"].apply(
#         lambda x: bool(re.match(format, x))
#     )
#     return data


# data = check_phone_format(data, "^\d{11}$")

# # Print the data with the new name_consistent and city_consistent columns
# print(data)
