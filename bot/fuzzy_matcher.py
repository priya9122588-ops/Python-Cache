from rapidfuzz import process

class FuzzyMatcher:
    def find_best_match(self, query, choices):
        result = process.extractOne(query, choices)

        if result:
            match, score, _ = result
            if score > 70:
                return match, score
        return None, 0