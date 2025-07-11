# Data-Source-API-Analyst-Test

Homework assignment for the Data Source API Analyst role.  
This project demonstrates API research, data extraction, error handling, and documentation using GitHub’s public API, developed entirely in Google Colab.

---

## Repository Structure

Data-Source-API-Analyst-Test/
├── README.md  
├── Content/  
│   ├── github_api_reference.md          # API research and notes  
│   ├── troubleshooting_guide.md        # Guide for common issues and error handling  
│   └── github_api_client.py             # Python script containing the core API client class that handles authentication, data extraction (search, commits, contents), pagination, rate limit handling, and error management  
└── Postman_Collection/  
    └── github_api_test.ipynb            # Google Colab notebook with code and output  

---

## Objectives

- Research and test GitHub REST API  
- Extract public data:  
  - Repository list via keyword search  
  - Commit history for a public repository  
  - Repository contents via `/contents` endpoint  
- Implement:  
  - Secure authentication using personal access token  
  - Pagination to retrieve full datasets  
  - Error handling using `try/except` blocks  
- Document the technical process and troubleshooting strategies  

---

## Tools Used

- **Python** (`requests`)  
- **Google Colab** (code execution and visualization)  
- **GitHub REST API v3**  
- **Markdown** (for documentation)  

---

## Key Features

- Authentication using `getpass` to hide the token  
- Search, commits, and contents extraction using real API endpoints  
- Pagination implemented via GitHub’s `Link` header  
- Exception handling for HTTP and connection errors  
- Modular Python client script (`github_api_client.py`) encapsulating GitHub API interactions, including token-based authentication, paginated data retrieval, and robust error handling  
- Organized project structure and clear documentation  

---

## Reflection

This assignment was a great opportunity to apply and reinforce my knowledge of REST APIs and real-world data extraction techniques.  

I particularly enjoyed working with GitHub’s API, handling pagination, designing reusable functions, and documenting the process clearly. Developing the solution entirely in Colab also allowed me to focus on clean, testable code.  

I'm confident that the approach and implementation reflect a solid understanding of API workflows, error control, and data processing best practices.  

---

## How to Use

> Run the Google Colab notebook, enter your GitHub token when prompted, and follow the execution cells to test the endpoints and view results.


