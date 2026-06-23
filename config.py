# config.py
CACHE_TTL = 300  # Time to live for the cache in seconds
FILE_NAME = "data.txt"  # Name of the file

#pip install requests beautifulsoup4
#pip install flask
#pip install rapidfuzz

import logging

def setup_logger():
    logger = logging.getLogger("my_project_logger")
    logger.setLevel(logging.DEBUG)

    # File handler to store logs in 'app.log'
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)

    # Log format: timestamp, log level, and message
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger



#------------------------------------------------------------------------------------------------------------------------------
# my_project/
# │
# ├── cache/
# │   ├── __init__.py
# │   ├── cache_store.py       # Cache storage logic
# │   ├── cache_expiry.py      # Cache expiry logic
# │   └── cache_manager.py     # Cache management logic
# │
# ├── file/
# │   ├── __init__.py
# │   ├── file_reader.py       # File reading logic
# │   └── file_writer.py       # File writing logic
# │
# ├── config.py                # Configuration file (optional)
# ├── main.py                  # Main application logic