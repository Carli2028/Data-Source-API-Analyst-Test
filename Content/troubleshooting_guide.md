
# Troubleshooting Guide

This document outlines the most common issues encountered while working with the GitHub API and how they were resolved.

---

## 401 Unauthorized

**Issue:**  
Occurs when the token is missing, invalid, or lacks permissions.

**Solution:**  
- Generated a Personal Access Token from GitHub
- Used `getpass.getpass()` to hide the token in Colab
- Added it as a Bearer token in the `Authorization` header

---

## 403 Forbidden / Rate Limits

**Issue:**  
GitHub limits the number of unauthenticated requests per hour.

**Solution:**  
- Always used authenticated requests via token
- Checked and respected the `X-RateLimit-Remaining` and `Retry-After` headers when needed

---

## 422 Unprocessable Entity

**Issue:**  
Happens if the search query (`q`) is missing or invalid.

**Solution:**  
- Always included a valid `q` parameter in search requests (e.g., `"q=data"`)

---

## Handling Pagination

**Problem:**  
Some endpoints (like commits) return paginated results.

**Solution:**  
- Implemented logic to detect the `Link` header
- Used a loop to retrieve all pages
- Combined results into a single list

---

## Error Handling

**Implementation:**  
Added `try/except` blocks in the main API function to catch:
- HTTP errors
- Connection issues
- Unexpected exceptions

This ensures the program continues or fails gracefully.
