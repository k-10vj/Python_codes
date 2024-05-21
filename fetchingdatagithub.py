import requests
import base64


def fetch_readme_content(username, repo, token):
    url = f"https://api.github.com/repos/{username}/{repo}/contents/README.md"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        content = data.get("content")
        if content:
            # GitHub API returns content as base64 encoded, decode it
            return base64.b64decode(content).decode("utf-8")
    elif response.status_code == 404:
        return "README.md not found in the specified repository."
    else:
        return f"Failed to fetch README.md. Status code: {response.status_code}"


# Replace these values with your GitHub username, repository name, and personal access token
username = "k-10vj"
repo = "Codes"
token = "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"

readme_content = fetch_readme_content(username, repo, token)
print(readme_content)
