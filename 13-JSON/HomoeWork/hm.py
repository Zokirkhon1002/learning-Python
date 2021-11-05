import json
import requests

# data = {
#     "Model": "Malibu",
#     "Rang": "Qora",
#     "Yil": 2020,
#     "Narh": 40000
# }

# json_data = json.dumps(data, indent=4)
# print(json_data)
# with open("data.json", "w") as f:
#     f.write(json_data)


# with open("data.json") as f:
#     data2 = json.load(f)
# print(data2)



# talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
# for key,value in talaba_json.items():
#     print(value)

# with open("data.json", "a") as f:
#     json.dump(talaba_json, f, indent=4)







with open("students.json", "r") as f:
    data = json.load(f)

for key in data['student']:
    print(f"{key['name']} {key['lastname']} Faculty of {key['faculty']}")






# wikiapi = "https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python"
# response = requests.get(wikiapi)
# python_python = json.dumps(response.json(), indent = 4)
# print(python_python)

# with open("wiki.json", "w") as f:
#     json.dump(response.json(), f, indent=4)





with open("wiki.json") as f:
    wiki = json.load(f)

print(wiki["query"]["pages"]["13801"]["title"])
print(wiki["query"]["pages"]["13801"]["extract"])