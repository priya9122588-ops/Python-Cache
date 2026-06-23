from file.file_reader import FileReader
from cache.cache_manager import CacheManager
from bot.fuzzy_matcher import FuzzyMatcher


class ChatBot:
    def __init__(self, cache_manager):
        self.file_reader = FileReader()
        self.cache_manager = cache_manager
        self.matcher = FuzzyMatcher()

    def get_all_entries(self):
     entries = []

     for key in self.cache_manager.cache_store.cache:
        value, expiry = self.cache_manager.cache_store.cache[key]
        entries.append(value)

     return entries

    def get_all_names(self, entries):
        names = []
        for entry in entries:
            try:
                name = entry.split("-")[0]
                names.append(name)
            except:
                continue
        return list(set(names))

    def extract_field(self, query):
        query = query.lower()

        if "age" in query:
            return "age"
        elif "value" in query or "price" in query:
            return "value"
        elif "name" in query:
            return "name"
        else:
            return "full"

    def extract_name(self, query, names):
        words = query.lower().split()

        best_match = None
        best_score = 0

        for word in words:
            match, score = self.matcher.find_best_match(word, names)

            if match and score > best_score:
                best_match = match
                best_score = score

        return best_match

    def get_response(self, user_query):
        print("USER QUERY:", user_query)

        entries = self.get_all_entries()
        print("ENTRIES:", entries)

        names = self.get_all_names(entries)
        print("NAMES:", names)

        name = self.extract_name(user_query, names)
        print("MATCHED NAME:", name)

        if not name:
            return "User not found"

        field = self.extract_field(user_query)
        print("FIELD:", field)

        # 🔹 Check cache
        cached = self.cache_manager.get_data(name)

        if cached:
            entry = cached
        else:
            entry = None
            for e in entries:
                if e.startswith(name):
                    entry = e
                    self.cache_manager.set_data(name, e)
                    break

        if not entry:
            return "Data not found"

        parts = entry.split("-")

        if len(parts) < 3:
            return "Invalid data format"

        name_val, age_val, value_val = parts[0], parts[1], parts[2]

        if field == "age":
            return age_val
        elif field == "value":
            return value_val
        elif field == "name":
            return name_val
        else:
            return entry