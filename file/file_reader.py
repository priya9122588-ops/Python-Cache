# # file/file_reader.py

# class FileReader:
#     def read(self, file_name):
#         with open(file_name, "r") as f:
#             return f.read()

# file/file_reader.py
import logging

# Initialize the logger
logger = logging.getLogger("my_project_logger")

class FileReader:
    def read(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
        logger.info(f"Read data from file: {file_name}, data: {content}")
        return content
      