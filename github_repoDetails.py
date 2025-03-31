import requests

def fetch_repo_details(repo_url):
    response = requests.get(repo_url)

    if response.status_code == 200:
        output = response.json()

        repo_name = output.get("name")
        repo_owner = output.get("owner", {}).get("login","Unknown Owner")
        repo_desc = output.get("description","No description available")

        print(f"Repository Name: {repo_name}")
        print(f"Repository Owner: {repo_owner}")
        print(f"Repository Description: {repo_desc}")
    else:
        print(f"Repository URL is invalid {response.status_code}")

repo_url = input("Enter the GitHub Repository API URL: ")
fetch_repo_details(repo_url)

# repo_url = "https://api.github.com/repos/v2devendranabar/learnpython"