import requests

response = requests.get("https://api.github.com/iam-veeramalla/python-for-devops/pulls")

print(response)