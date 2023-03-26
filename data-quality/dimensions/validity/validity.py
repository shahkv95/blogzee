import logging
from typing import List
from pydantic import BaseModel, validator


class Employee(BaseModel):
    name: str
    age: int

    @validator("age")
    def age_validator(cls, value):
        if value < 0:
            raise ValueError("Age cannot be less than 0")
        elif value > 200:
            raise ValueError("Age cannot be greater than 200")
        return value


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler("validity.log"), logging.StreamHandler()],
    )

    with open("check_validity_data.csv", "r") as f:
        employee_data = f.readlines()

    valid_employees = []
    invalid_employees = []
    for line in employee_data:
        try:
            name, age = line.strip().split(",")
            employee = Employee(name=name, age=int(age))
            valid_employees.append(employee)
        except ValueError as e:
            logging.warning(f"Invalid employee data: {line.strip()}, error: {e}")
            invalid_employees.append(line.strip())

    logging.info(f"Valid Employees: {valid_employees}")
    logging.info(f"Invalid Employees: {invalid_employees}")
