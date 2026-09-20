# Python Guidelines
Rely on these guidelines when writing Python code or creating a new project.

1. Use uv as the preferred package and version management tool.
2. If you're starting a new project, always use the latest stable version (> 3.14).
3. Use Ruff and Mypy to check, format, and verify the code.
4. Use a strong typing style:
    * Always declare the type of a variable, argument, or return value.
    * Never use `Any`; always scan the libraries/classes and add the real type.
        * Avoid `Any` at any cost; use it only if there are no other options left.
    * Always state the type, such as a class or a native type.
    * Always state the full type, such as `dict[str: list[...]]` instead of `dict`.
5. Always declare the logger as a constant at the beginning of each file after imports, like `LOGGER: logging.Logger = get_logger(...)`.

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

## Package Structure
* Always make sure to use a folder `src/<project_name>/...` to add all the Python sources inside.
* Make sure that the `pyproject.toml` is configured and that ruff/mypy check only this folder.

---