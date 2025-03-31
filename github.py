import requests

def fetch_pr_details(repo_url):
    response = requests.get(repo_url)

    if response.status_code == 200:
        output = response.json()
        for i in output:
          print(i["user"]["login"])
    else:
        print(f"Repository URL is invalid Status Code: {response.status_code}")

repo_url = input("Enter GitHub Repository API: ")
fetch_pr_details(repo_url)

# repo_url = "https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls"