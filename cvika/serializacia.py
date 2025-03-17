import json

data = [1, "2", [3, 4], (5, 6), "text", 3.14]
with open("binarny_subor.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
with open("binarny_subor.json", "r", encoding="utf-8") as f:
    data1 = json.load(f)

print(data1)
