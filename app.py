# from flask import Flask, render_template, request
# from cache.cache_manager import CacheManager
# from file.file_writer import FileWriter
# from file.file_reader import FileReader
# from config import CACHE_TTL

# app = Flask(__name__)

# cache_manager = CacheManager(ttl=CACHE_TTL)
# file_writer = FileWriter()
# file_reader = FileReader()


# @app.route("/", methods=["GET", "POST"])
# def index():
#     output = None

#     if request.method == "POST":
#         name = request.form.get("name")
#         age = request.form.get("age")
#         value = request.form.get("value")

#         output = main_logic(
#             cache_manager,
#             file_writer,
#             file_reader,
#             name,
#             age,
#             value
#         )

#     return render_template("index.html", output=output)


# def main_logic(cache_manager, file_writer, file_reader, name, age, value):
#     print(f"Writing {value} to file...")
#     file_writer.write("data.txt", f"{name}-{age}-{value}")
#     print(f"Written {value} to file.")
#     print("Write done")

#     cached_data = cache_manager.get_data("file_data")

#     if cached_data is not None:
#         print("From cache")
#         return cached_data

#     print("Reading from file")
#     data = file_reader.read("data.txt")

#     latest = data.strip().split()[-1]

#     cache_manager.set_data("file_data", latest)

#     return latest


# if __name__ == "__main__":
#     app.run(debug=True)








# app.py
from flask import Flask, render_template, request, jsonify
from cache.cache_manager import CacheManager
from file.file_writer import FileWriter
from file.file_reader import FileReader
from config import CACHE_TTL

# 🔥 NEW: import chatbot
from bot.chatbot import ChatBot

app = Flask(__name__)

cache_manager = CacheManager(ttl=CACHE_TTL)
file_writer = FileWriter()
file_reader = FileReader()

# 🔥 NEW: initialize chatbot
chatbot = ChatBot(cache_manager)


@app.route("/", methods=["GET", "POST"])
def index():
    output = None

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        value = request.form.get("value")

        output = process_data(name, age, value)

    return render_template("index.html", output=output)


def process_data(name, age, value):
    entry = f"{name}-{age}-{value}"

    print(f"Storing in cache: {entry}")

    # 🔥 Store directly in cache using name as key
    cache_manager.set_data(name.lower(), entry)

    return entry


# 🔥🔥 NEW ROUTE (CHATBOT API)
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("query")

    print("Query received:", user_input)

    response = chatbot.get_response(user_input)

    print("BOT RESPONSE:", response)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)