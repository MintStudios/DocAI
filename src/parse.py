from os import EX_DATAERR
import config
import json

data = {}

with open("src/json/lang.json", "r") as read_file:
    data = json.load(read_file)


def parse_lang():
    for lang in data:
        for pronunciation in data[lang]:
            if pronunciation in config.current_line:
                config.current_lang = lang
                print(f"{lang} documentation.")
                break


def parse():
    parse_lang()


parse()
