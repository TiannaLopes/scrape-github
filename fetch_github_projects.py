import requests
import json

# GitHub username
username = 'TiannaLopes'

# GitHub API URL for user repositories
api_url = f'https://api.github.com/users/{username}/repos'

# Send GET request to GitHub API
print(f"Fetching repositories for {username} from {api_url}")
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    repos = response.json()
    projects = []

    for repo in repos:
        # Fetch topics (skills) for each repository
        topics_url = f"https://api.github.com/repos/{username}/{repo['name']}/topics"
        topics_response = requests.get(topics_url, headers={'Accept': 'application/vnd.github.mercy-preview+json'})
        topics = topics_response.json().get('names', [])

        project = {
            'id': repo['id'],
            'name': repo['name'],
            'description': repo['description'],
            'url': repo['html_url'],
            'skills': topics
        }
        print(f"Adding project: {project['name']}")
        projects.append(project)

    # Save projects to a JSON file
    with open('projects.json', 'w') as json_file:
        json.dump(projects, json_file, indent=4)

    print('Projects data has been saved to projects.json')
else:
    print(f'Failed to retrieve repositories: {response.status_code}')
