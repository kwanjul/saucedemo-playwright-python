# saucedemo-playwright-python
Playwright Python test automation framework for Sauce Demo

## Getting started

This starter test logs in to Sauce Demo with its standard demo account and
checks that the inventory page displays all six products.
The base URL and demo credentials are set once in `pytest.ini`. Tests can
navigate with relative paths such as `page.goto("/")` and access the shared
settings through the `sauce_demo_settings` fixture.

The configured Sauce Demo accounts are public test credentials. Do not put
private account passwords in a checked-in configuration file.

### Install

Create and activate a virtual environment, then install the project
dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

On macOS and Linux, use the commands above. On Windows, activate the
environment with `.venv\Scripts\activate` instead.

### Run the test

```bash
pytest
```

To watch the browser while the test runs:

```bash
pytest --headed
```

The test is in [`tests/test_login.py`](tests/test_login.py).
