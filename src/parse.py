import config
import json

lang_data = {}
terms_data = {}

with open("src/json/lang.json", "r") as read_file:
    lang_data = json.load(read_file)

with open("src/json/terms.json", "r") as read_file:
    terms_data = json.load(read_file)


def parse_lang():
    for lang in lang_data:
        for pronunciation in lang_data[lang]:
            if pronunciation in config.current_line:
                config.current_lang = lang
                break


def parse_objective():
    for term in terms_data:
        for pronunciation in terms_data[term]:
            if pronunciation in config.current_line:
                config.current_objective = term
                break


def parse():
    parse_lang()
    parse_objective()
    print(
        f"Looking up {config.current_objective} in the {config.current_lang} documentation"
    )
