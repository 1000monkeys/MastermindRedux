import collections
import json
from operator import itemgetter
from cryptography.fernet import Fernet

class StaticFunctions():
    def merge_dict(*args: dict) -> dict:
        result = dict()
        dict_count = 0
        for dictionary in args:
            for key in dictionary.keys():
                result[str(dict_count) + "-" + str(key)] = dictionary[key]
            dict_count = dict_count + 1
        return result

    def encrypt(target):
        key = b'5C2UhPiEnFdVurKEm-F4cLgWaqiqDZoDSnSIaOmGiDY='
        fernet = Fernet(key)
        target = json.dumps(target)
        encrypted = fernet.encrypt(str.encode(target))
        with open('data.txt', 'w') as f:
            f.write(encrypted.decode("utf-8"))

    def decrypt():
        key = b'5C2UhPiEnFdVurKEm-F4cLgWaqiqDZoDSnSIaOmGiDY='
        fernet = Fernet(key)
        with open('data.txt') as f:
            encrypted = f.read()
        encrypted = fernet.decrypt(encrypted.encode("utf-8"))
        encrypted = encrypted.decode("utf-8")

        json_data = json.loads(encrypted)
        json_data["0"] = dict(sorted(json_data["0"].items(), key=lambda item: item[1], reverse=True))
        json_data["1"] = dict(sorted(json_data["1"].items(), key=lambda item: item[1], reverse=True))
        json_data["2"] = dict(sorted(json_data["2"].items(), key=lambda item: item[1], reverse=True))

        return json_data
"""
data = {
    "settings": {
        "language_pos": 0,
        "game_rounds_pos": 0,
        "time_guess_pos": 0,
        "amount_pins_pos": 0,
        "name": "user"
    },
    "0": {"user": 1400, "user1": 2500},
    "1": {},
    "2": {}
}

StaticFunctions.encrypt(data)
print(StaticFunctions.decrypt())
"""
