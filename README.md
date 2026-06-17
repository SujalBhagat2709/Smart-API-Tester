# Smart API Tester

## Overview

Automatically scans APIs, tests endpoints, and generates an HTML report.

---

## Installation

```bash
pip install requests
```

---

## Run

```bash
python test_runner.py
```

---

## Example

Input:

```text
https://jsonplaceholder.typicode.com
```

Output:

```text
Scanning Endpoints...

Found:
/users

Found:
/posts

Running Tests...

✓ /users

✓ /posts

Report Generated:
test_report.html
```

---

## Generated File

```text
test_report.html
```

Contains:

- Endpoint URL
- Status Code
- Test Results

---

## Future Improvements

- Swagger/OpenAPI Support
- POST Request Testing
- Authentication
- Load Testing
- JSON Validation
- Response Time Analysis