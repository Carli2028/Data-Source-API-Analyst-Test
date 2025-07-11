# github_api_client.py

This script contains the `GitHubApiClient` class that allows connecting to the GitHub API to:

- Authenticate using a personal access token (PAT).
- Extract data: search repositories, list commits, and get repository contents.
- Handle pagination to retrieve all available results.
- Handle rate limits with automatic wait.
- Basic error handling for requests.

## Usage

1. Import the `GitHubApiClient` class.
2. Create an instance with a valid token.
3. Use the available methods to extract data, for example:
    ```python
    client = GitHubApiClient("YOUR_TOKEN")
    repos = client.search_repositories("data source")
    commits = client.list_commits("owner", "repo")
    contents = client.get_repo_contents("owner", "repo")
    ```

## Requirements

- Python 3.x
- `requests` library

## Note

The token should have permissions to access public repositories. To avoid exposing the token, it is recom

