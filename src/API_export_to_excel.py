import pandas as pd
import requests

#Asking the categories
url = "http://www.gmkitchen.hu/wp-json/wp/v2/categories?per_page=100"
response = requests.get(url)


if response.status_code ==200:
    categories = response.json()
    #Making list from the datas we need
    data = []
    for cat in categories:
        data.append({
            "Name": cat['name'],
            "ID": cat['id']
        })
    #put it in a dataframe
    df = pd.DataFrame(data)
    #export to Excel
    df.to_excel("output\categories.xlsx", index=False) 
    print("Succesfully export: categories.xlsx")  
else:
    print("Error:", response.status_code)

