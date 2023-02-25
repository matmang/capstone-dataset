import requests
import json
import csv

book_lists = []

#키와 url 정의
TTBKey = "ttbkimdaye772247001"

for i in range(1, 101):
    url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?TTBKey={TTBKey}"\
          "&QueryType=ItemNewSpecial&SearchTarget=Book"\
          f"&start={i}&output=js&Version=20131101"
    res = requests.get(url)
    items = json.loads(res.text)['item']
    for item in items:
        book_dict = {}
        book_dict['prodName'] = item['title']
        book_dict['category'] = item['categoryName'].split('>')[2] if len(item['categoryName'].split('>')) > 2 else "null"
        book_dict['description'] = item['description'] if len(item['description']) > 0 else "null"
        book_lists.append(book_dict)

length = len(book_lists)
print(f"총 {length}개의 데이터가 추출되었습니다.")

with open("aladdin_data.csv", 'w', newline="") as file:
    header = ['prodName', 'category', 'description']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for element in book_lists:
        writer.writerow(element)
