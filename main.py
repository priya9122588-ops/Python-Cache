
# # main.py
# import time
# from cache.cache_manager import CacheManager
# from file.file_writer import FileWriter
# from file.file_reader import FileReader
# from config import CACHE_TTL, setup_logger

# # Initialize logger
# logger = setup_logger()

# # Constants
# file_name = "data.txt"

# # 🔹 Main Workflow Function
# def main_workflow(cache_manager, file_writer, file_reader, name, age, value):
#     # Step 1: Always write to file
#     print(f"Writing {value} to file...")
#     file_writer.write("data.txt", f"{name}-{age}-{value}")
#     print(f"Written {value} to file.")
#     print("Write done")

#     # Step 2: Check cache
#     cached_data = cache_manager.get_data("file_data")

#     if cached_data is not None:
#         # ✅ Use cache (even if new data came)
#         print("Using old cache (not expired)")
#         return cached_data

#     # Step 3: Cache expired → read fresh data
#     print("Reading from file")
#     data = file_reader.read("data.txt")

#     # take last entry only (delta)
#     latest = data.strip().split()[-1]

#     cache_manager.set_data("file_data", latest)

#     return latest

# # 🔹 Main Execution
# if __name__ == "__main__":
#     # Initialize CacheManager, FileWriter, and FileReader
#     cache_manager = CacheManager(ttl=CACHE_TTL)
#     file_writer = FileWriter()
#     file_reader = FileReader()

#     # List of data to write to the file
#     data_list = ["A", "B", "C", "D"]

#     # Run the main workflow
#     main_workflow(cache_manager, file_writer, file_reader, data_list)















# main.py
import time
from cache.cache_manager import CacheManager
from file.file_writer import FileWriter
from file.file_reader import FileReader
from config import CACHE_TTL

file_name = "data.txt"

def main_workflow(cache_manager, file_writer, file_reader, data_list):
    last_written = None

    for item in data_list:
        print(f"Writing {item} to file...")
        file_writer.write(file_name, item)
        print(f"Written {item} to file.")
        print("Write done")

        cached_data = cache_manager.get_data("file_data")

        if cached_data is None:
            print("Reading from file")
            data = file_reader.read(file_name)
            latest = data.strip().split()[-1]
            cache_manager.set_data("file_data", latest)
        else:
            latest = cached_data

        if last_written != item:
            print("Cache Data:", item)

        last_written = item
        print("------")
        time.sleep(1)


if __name__ == "__main__":
    cache_manager = CacheManager(ttl=CACHE_TTL)
    file_writer = FileWriter()
    file_reader = FileReader()

    data_list = ["A", "B", "C", "D"]

    main_workflow(cache_manager, file_writer, file_reader, data_list)