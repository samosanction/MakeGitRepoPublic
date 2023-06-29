import requests

access_token = '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'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'User-Agent': 'Python'
}
base_url = "https://api.github.com/samosanction/repos"

# Get a list of all repositories
response = requests.get(base_url, headers=headers)
repositories = response.json()

if response.status_code != 200:
    # Handle any errors in retrieving the repositories
    print('Error:', response.text)
    exit()

# Loop through each repository and make it public
for repository in repositories:
    repo_name = repository['name']
    repo_url = repository['url']

    # Set the repository visibility to public
    data = {
        'private': False
    }

    # Update the repository visibility
    response = requests.patch(repo_url, json=data, headers=headers)

    if response.status_code == 200:
        print('Repository "{}" is now public.'.format(repo_name))
    else:
        # Handle any errors in updating the repository visibility
        print('Error updating repository "{}": {}'.format(repo_name, response.text))

