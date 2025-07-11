# GitHub API Reference (Research Notes)

This document summarizes the GitHub API endpoints explored during the test and how they were used.

---

## Search Repositories

**Endpoint:**  
`GET https://api.github.com/search/repositories?q=data`

**Purpose:**  
To search for public repositories containing a specific keyword (e.g., "data").

**Key Parameters:**
- `q`: The search keyword.
- `per_page`: Limits results per page (e.g., 5).

---

## Get Repository Contents

**Endpoint:**  
`GET https://api.github.com/repos/{owner}/{repo}/contents/{path}`

**Purpose:**  
To retrieve the list of files and folders at a given path in a repository.

**Example:**  
`https://api.github.com/repos/octocat/Hello-World/contents/`

**Returns:**  
A list of file and folder metadata, including name, type, and download URL.

---

## Get Commits

**Endpoint:**  
`GET https://api.github.com/repos/{owner}/{repo}/commits`

**Purpose:**  
To list the commit history of a public repository.

**Pagination Support:**  
Yes — use `?per_page=...&page=...` or parse the `Link` header.

---

## Documentation Used

- [GitHub REST API v3 Docs](https://docs.github.com/en/rest)
- Authentication: [Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

