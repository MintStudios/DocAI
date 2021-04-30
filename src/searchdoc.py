import json
import config
import webbrowser

docpages = {}

with open("src/json/docpages.json", "r") as read_file:
    docpages = json.load(read_file)


def search():
    config.current_objective = config.current_objective.replace(" ", "%20")
    webbrowser.open(f"{docpages[config.current_lang]}{config.current_objective}")
