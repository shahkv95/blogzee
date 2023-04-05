from config import DATA_SOURCE
import pandas as pd
import logging
from typing import Union

logging.basicConfig(level=logging.INFO)


class PhoneNumberStandardizer:
    def __init__(self, phone: Union[str, int]) -> None:
        self.phone = phone

    def standardize_phone_number(self) -> Union[str, None]:
        try:
            phone = self.phone
            phone = "".join(filter(str.isdigit, phone))

            if len(phone) == 10:
                return phone[:3] + "-" + phone[3:6] + "-" + phone[6:]

            elif len(phone) == 12 and phone[0:2] == "91":
                return phone[2:5] + "-" + phone[5:8] + "-" + phone[8:]
            else:
                return "INVALID"
        except Exception as e:
            logging.error(f"Error occurred while standardizing phone number: {e}")
            return None


if __name__ == "__main__":
    try:
        logging.info(" Phone numbers are considered to be Indian number format.\n")
        filename = DATA_SOURCE

        df = pd.read_csv(filename)
        df["consistent_format"] = df["phone_number"].apply(
            lambda x: PhoneNumberStandardizer(x).standardize_phone_number()
        )
        print(df)
    except FileNotFoundError:
        logging.error("File not found.")
