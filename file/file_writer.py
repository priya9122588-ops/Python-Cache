# # file/file_writer.py

# class FileWriter:
#     def write(self, file_name, data):
#         with open(file_name, "a") as f:
#             f.write(data + " ")


# file/file_writer.py
import logging

# Initialize the logger
logger = logging.getLogger("my_project_logger")

class FileWriter:
    def write(self, file_name, data):
        with open(file_name, "a") as f:
            f.write(data + " ")
        logger.info(f"Written data: '{data}' to file: {file_name}")