import collections
import json
from operator import itemgetter
from cryptography.fernet import Fernet

class StaticFunctions():
    def merge_dict(*args: dict) -> dict:
        """Merges dictionaries, leads names with a integer which is how many dict it is

        :return: Merged dictionarie
        :rtype: dict
        """
        result = dict()
        dict_count = 0
        for dictionary in args:
            for key in dictionary.keys():
                result[str(dict_count) + "-" + str(key)] = dictionary[key]
            dict_count = dict_count + 1
        return result

    def encrypt(target: str):
        """Encrypts a string and writes it to data.txt

        :param target: String to encrypt
        :type target: str
        """
        key = b'5C2UhPiEnFdVurKEm-F4cLgWaqiqDZoDSnSIaOmGiDY='
        fernet = Fernet(key)
        target = json.dumps(target)
        encrypted = fernet.encrypt(str.encode(target))
        with open('data.txt', 'w') as f:
            f.write(encrypted.decode("utf-8"))

    def decrypt():
        """Decrypts data.txt and sets up the json data dictionary

        :return: Dicitonary build from decrypted data.txt
        :rtype: Dict
        """
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