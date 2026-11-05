# Sauce Demo — Playwright Python Test Automation Framework

An automated UI testing framework for [Sauce Demo](https://www.saucedemo.com/), developed using **Python, Playwright, and pytest**.

This project demonstrates practical software quality engineering techniques, including:

- **Page Object Model (POM)** for organizing page interactions and locators.
- **pytest fixtures** for reusable browser setup, authentication, and test preconditions.
- **Functional, negative, and regression testing** across key e-commerce workflows.
- **Automated assertions** using Playwright's built-in waiting and retry mechanisms.
- **Centralized configuration** for application URLs and demo credentials.
- **HTML and JUnit XML reporting**, with screenshots and Playwright traces for failed tests.
- **GitHub Actions CI/CD integration** for automated test execution and downloadable reports.

## Test Reports

View the latest GitHub Actions workflow status and access downloadable test reports:

[![Playwright Python Tests](https://github.com/kwanjul/saucedemo-playwright-python/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/kwanjul/saucedemo-playwright-python/actions/workflows/playwright-tests.yml)

## Test Coverage

The framework currently contains **19 automated tests** across five functional areas:

| Functional Area | Coverage |
|---|---|
| Login | Successful login, invalid credentials, locked-out users, login page validation |
| Inventory | Product display, sorting, adding and removing products |
| Product Details | Product information validation, adding and removing products |
| Shopping Cart | Cart contents, product removal, continuing shopping |
| Checkout Information | Valid checkout information and required-field validation |

## Framework Architecture

The framework follows the **Page Object Model (POM)** design pattern, separating page interactions from test logic to improve readability, maintainability, and reuse.

### Project Structure

```text
saucedemo-playwright-python/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_information_page.py
│   ├── inventory_page.py
│   ├── login_page.py
│   └── product_details.py
├── tests/
│   ├── conftest.py
│   ├── test_cart.py
│   ├── test_checkout_information.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── test_product_details.py
├── .gitignore
├── config.py
├── pytest.ini
├── README.md
└── requirements.txt
```

### Key Components

| Component | Purpose |
|---|---|
| `pages/` | Page Object Model classes that encapsulate page elements and interactions |
| `tests/` | pytest test modules containing functional and negative test scenarios |
| `tests/conftest.py` | Shared pytest fixtures for reusable test setup and preconditions |
| `config.py` | Centralized application URL and demo account configuration |
| `pytest.ini` | pytest configuration, registered test markers, and HTML reporting options |
| `requirements.txt` | Python package dependencies |
| `.github/workflows/playwright-tests.yml` | GitHub Actions workflow for automated test execution and artifact uploads |
| `.gitignore` | Excludes generated files and local environment artifacts from version control |

### Design Approach

Tests use page objects to interact with the application, keeping page-specific locators and actions separate from test assertions.

Reusable pytest fixtures provide common setup and application states, reducing duplicated code across test modules.

Playwright's auto-waiting capabilities and retrying assertions help make test execution more reliable.

## Configuration

The framework uses `config.py` to centralize application settings, including the Sauce Demo base URL and standard demo account credentials.

Default values are provided for local execution. These settings can also be overridden using environment variables without modifying the source code.

For example, on macOS or Linux:

```bash
export BASE_URL="https://www.saucedemo.com"
export STANDARD_USERNAME="standard_user"
export STANDARD_PASSWORD="secret_sauce"
```

The credentials used by this project are publicly available Sauce Demo test credentials. Do not store private passwords or production credentials in the repository.

## Installation

Create and activate a Python virtual environment, then install the project dependencies:

```bash
git clone https://github.com/kwanjul/saucedemo-playwright-python.git
cd saucedemo-playwright-python
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

On Windows, activate the virtual environment using `.venv\Scripts\activate` instead.

## Running Tests

Run the complete test suite:

```bash
pytest
```

Run tests with a visible browser:

```bash
pytest --headed
```

Run tests using Chromium:

```bash
pytest --browser chromium
```

Run only smoke tests:

```bash
pytest -m smoke
```

Run only regression tests:

```bash
pytest -m regression
```

The smoke suite contains five critical tests covering login, inventory, cart functionality, and checkout information. The regression suite includes all 19 tests, including the smoke tests.

### Test Reports and Failure Artifacts

The framework generates a self-contained HTML report at:

`reports/report.html`

To enable screenshots and Playwright traces for failed tests, run:

```bash
pytest --tracing retain-on-failure --screenshot only-on-failure --output test-results
```

Failure artifacts are saved in the `test-results/` directory.

GitHub Actions automatically executes the test suite and uploads downloadable HTML and JUnit XML reports, along with available failure screenshots and traces.

## Continuous Integration

The framework uses **GitHub Actions** to execute automated tests in Chromium on Ubuntu.

The workflow runs automatically:

- When changes are pushed to the `main` branch.
- When a pull request targets `main`.
- On a scheduled weekday run.
- When manually triggered through GitHub Actions.

Each execution generates downloadable test artifacts:

- **HTML report:** Human-readable test results, including failures and execution details.
- **JUnit XML report:** Machine-readable test results.
- **Failure artifacts:** Playwright screenshots and traces when tests fail.

The latest workflow status is displayed near the top of this README.