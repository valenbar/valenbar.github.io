import json
import json2html

with open("data/database.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data.pop("users")

with open("data/index.html", "w", encoding="utf-8") as f:
    f.write(json2html.json2html.convert(json = data))