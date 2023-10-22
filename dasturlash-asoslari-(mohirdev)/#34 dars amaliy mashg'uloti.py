import json

data = {
    'Model': 'Malibu',
    'Rang': 'Qora',
    'Yil': 2020,
    'Narh': 40000  
}
data_json = json.dumps(data, indent=4)
print(data_json)
with open('data.json', 'w') as f:
    json.dump(data, f)

talaba_json = {"ism": "Hasan", "familiya": "Husanov", "tyil":2000} 
with open('talaba.json', 'w') as f:
    json.dump(talaba_json, f)

with open('D:\Python\GitHubRepos\python-vazifalar\dasturlash-asoslari-(mohirdev)\students.json') as f:
    data = json.load(f)

for item in data['student']:
    print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")

with open("D:\Python\GitHubRepos\python-vazifalar\dasturlash-asoslari-(mohirdev)\wikipedia.json") as f:
    w_data = json.load(f)

print(w_data)
print(w_data.keys())
print(w_data['query'].keys())
print(w_data['query']['pages']['13801']['title'])
print(w_data['query']['pages']['13801']['extract'])