from urllib.error import HTTPError
import requests, wget
import pandas as pd
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

df = pd.read_excel("Free+English+textbooks.xlsx")
for index, row in df.iterrows():
        # loop through the excel list
        file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
        url = f"{row.loc['OpenURL']}"
        r = requests.get(url) 
        ensure_dir(f"./download/{file_name}/")
        download_url = f"{r.url.replace('book','content/pdf')}.pdf"
        wget.download(download_url, f"./download/{file_name}/{file_name}.pdf") 
        print(f"downloading {file_name}.pdf Complete ....")
        try:
            download_url = f"{r.url.replace('book','download/epub')}.epub"
            wget.download(download_url, f"./download/{file_name}/{file_name}.epub") 
            print(f"downloading {file_name}.epub Complete ....")
        except HTTPError as error:
            print(f"{file_name}.epub not found ....")


         