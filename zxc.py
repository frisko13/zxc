import os

path = 'data'
files = os.listdir(path)

print(f"Количество файлов в папке {path}: {len(files)}")