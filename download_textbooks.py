from urllib.error import HTTPError
import requests, wget
import pandas as pd
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

df = pd.read_excel("C:/Git/springerbooks/Free+English+textbooks.xlsx")
for index, row in df.iterrows():
        # loop through the excel list
        book_folder_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
        file_name = f"{row.loc['Book Title']} - {row.loc['Author']} - {row.loc['Electronic ISBN']} - {row.loc['Publisher']}".replace('/','-').replace(':','-')
        url = f"{row.loc['OpenURL']}"
        r = requests.get(url) 
        book_download_path = f"P:/Libros/Para importar a Calibre/{book_folder_name}/"
        ensure_dir(f"{book_download_path}")
        try:
            download_url = f"{r.url.replace('book','content/pdf')}.pdf"
            wget.download(download_url, f"{book_download_path}{file_name}.pdf") 
            print(f" downloading {file_name}.pdf Complete ....")
        except HTTPError as error_pdf:
            print(f" {file_name}.pdf not found ....")
        try:
            download_url = f"{r.url.replace('book','download/epub')}.epub"
            wget.download(download_url, f"{book_download_path}{file_name}.epub") 
            print(f" downloading {file_name}.epub Complete ....")
        except HTTPError as error_epub:
            print(f" {file_name}.epub not found ....")

         