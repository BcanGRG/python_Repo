import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

alinan = input("Alınan Döviz Türü : ")
hesaplanan = input("Hesaplanacak Döviz Türü : ")
miktar = int(input("Para Miktarı : "))

result = requests.get(api_url + alinan).text
result = json.loads(result)

print("1 {0} = {1} {2}".format(alinan,result["rates"][hesaplanan],hesaplanan))
print("{0} {1} = {2} {3}".format(miktar,alinan,result["rates"][hesaplanan]*miktar,hesaplanan))


