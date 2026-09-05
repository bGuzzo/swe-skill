# Python Guidelines
Rely on these guidelines when writing Python code or creating a new project.

1. Use uv as the preferred package and version management tool.
2. If you're starting a new project, always use the latest stable version (> 3.14).
3. Use Ruff and Mypy to check, format, and verify the code.
4. Use a free-threaded Python version like 3.14t to gain performance.

---

## Code Snippets & Examples
Python example snippets can be found inside the folder [snippets](../assets/python/snippets/); read the index file [PY_EXAMPLE.md](../assets/python/snippets/PY_EXAMPLE.md) to index the content.

---

## Before Writing Code
* Check `pyproject.toml` to find Ruff, Mypy, or code style enforcers.
* Then load those guidelines into context and use them when writing code to execute the user query.

---

## Before Submitting Code to the User
Always use Ruff and Mypy to check and format the code, and resolve all findings before submitting the code to the user.

```bash
uv sync
uv run ruff check . --fix
uv run ruff format .
uv run mypy src tests
```

Keep iterating and fixing with `ruff` and `mypy` until they report 0 findings.

---