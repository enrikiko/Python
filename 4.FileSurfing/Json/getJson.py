import json

# Key Methods:
# json.load(f): Load JSON data from file
# json.loads(s): Load JSON data from string
# json.dump(j, f): Write JSON object to file
# json.dumps(j): Write JSON object as string

json_file = open("./film.json", "r", encoding="utf-8")
film = json.load(json_file)
json_file.close()

print(film)
