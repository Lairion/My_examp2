from datetime import date 
import requests,json
d= date.today()
d = str(d)
d = d.replace("-","")
req = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=UAH&date="+d+"&json")
obj_json = json.loads(req._content) 
print obj_json[0]["cc"]