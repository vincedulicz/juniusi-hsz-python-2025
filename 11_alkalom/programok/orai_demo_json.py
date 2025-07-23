import json

adat = {
    "név": "Anna",
    "kor": 25,
    "város": "Bp"
}

json_string = json.dumps(adat)

json_adat = '{"név": "Anna","kor": 25,"város": "Bp"}'
adat = json.loads(json_adat) # dict | json

# print(adat.get("nev"))

with open("adat.json", "w", encoding='utf-8') as file:
    json.dump(adat, file, indent=4, ensure_ascii=True)

with open("adat.json", "r", encoding='utf-8') as file:
    adat = json.load(file)
    print(type(adat))
    print(adat.get("kor"))


sample_json = """{
    "company":{
        "employee":{
            "name":"emma",
            "payble":{
                "salary":7000,
                "bonus":800
            }
        }
    }
}"""

data = json.loads(sample_json)
print(type(data))
print(data['company']['employee']['payble']['salary'])

print(data.get("company").get('employee'))
