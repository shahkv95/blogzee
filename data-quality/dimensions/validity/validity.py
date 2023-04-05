import logging
import hashlib
from config import SOURCE_FILE_PATH, MIGRATED_FILE_PATH

logging.basicConfig(level=logging.INFO)


class ChecksumValidator:
    def __init__(self, source_file_path: str, migrated_file_path: str) -> None:
        self.source_file_path = source_file_path

        self.migrated_file_path = migrated_file_path

    def _calculate_checksum(self, data: bytes) -> str:
        """
        Calculate the SHA-256 checksum for a given set of data.
        """
        sha256 = hashlib.sha256()

        sha256.update(data)

        return sha256.hexdigest()

    def _read_file(self, file_path: str) -> bytes:
        with open(file_path, "rb") as file:
            data = file.read()

        return data

    def validate(self) -> None:
        """
        Validate the data migration process by comparing the checksum values
        of the source and migrated data files.
        """
        try:

            logging.info("   Source file path: %s", self.source_file_path)
            logging.info(" Migrated file path: %s", self.migrated_file_path)

            source_data = self._read_file(self.source_file_path)
            source_checksum = self._calculate_checksum(source_data)
            logging.info("    Source checksum: %s", source_checksum)

            migrated_data = self._read_file(self.migrated_file_path)
            migrated_checksum = self._calculate_checksum(migrated_data)
            logging.info("  Migrated checksum: %s", migrated_checksum)

            if source_checksum == migrated_checksum:
                logging.info(" Data migration successful. Checksum values match.")
            else:
                logging.info(" Data migration failed. Checksum values do not match.")

        except FileNotFoundError as ex:
            logging.error(" Error occurred while validating data migration:", ex)

        except Exception as ex:
            logging.error(" Error occurred while validating data migration: ", ex)


if __name__ == "__main__":
    validator = ChecksumValidator(SOURCE_FILE_PATH, MIGRATED_FILE_PATH)
    validator.validate()
