import requests
import zipfile

r = requests.get(
    'https://github.com/soft7it/Python/archive/refs/heads/main.zip')

with open ('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())

# extract in my folder    
# with zipfile.ZipFile('data.zip', 'r') as data_zip:
    # print(data_zip.extractall)

# extract in my folder    
# with zipfile.ZipFile('data.zip', 'r') as data_zip:
    # (data_zip.extractall('data'))
