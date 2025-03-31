import os

folders = input("Please provide folder names with spaces in between: ").split()

for folder in folders:
    try:
      files = os.listdir(folder)
    except FileNotFoundError:
      print("Please provide a valid folder name as it not exist:",folder)
      continue

    for file in files:
       print(file)