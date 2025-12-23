# Optibet Test Automation Project

This project contains automated UI tests for the Optibet website.

## Technologies Used

*   **Language:** Python 3+
*   **Framework:** Pytest
*   **UI Automation:** Playwright
*   **Reporting:** Allure
*   **Environment:** Docker

## Covered Scenarios

*   **Header:**
    *   Verified that the logo is visible.
    *   Verified the presence of main navigation menu items.
    *   Verified language switching functionality (RU, EN, LT).
*   **Promotions:**
    *   Verified that the promotions page loads and displays promotion cards.
    *   Verified filtering functionality for different promotion categories.
*   **Registration:**
    *   Negative scenario with an invalid email.
    *   Negative scenarios with weak passwords (parametrization used).
    *   Negative scenario with an empty required field.
*   **Login:**
    *   Negative scenario with non-existent credentials.

## Limitations

*   No real financial actions are performed.
*   Tests are run against the live production environment.
*   The selectors used might be brittle and could break with website updates.
*   The tests are not exhaustive and only cover a subset of the website's functionality.

## How to Install Dependencies Locally

1.  Clone the repository.
2.  Install Python 3.8+ if you don't have it.
3.  Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Install Playwright browsers:
    ```bash
    playwright install
    ```

## How to Run Tests Locally

You can run tests using the `pytest` command.

**Run all tests:**

```bash
pytest
```

**Run tests in headless mode:**

```bash
pytest --headless
```

**Specify a different base URL:**

```bash
pytest --base_url=https://www.another-optibet.com/
```
**Run on specific browsers:**
By default, tests run on Chromium. You can specify one or multiple browsers using the --browser flag (options: chromium, firefox, webkit)
 
 Run on multiple browsers (will run each test for each browser): 
 
 ```bash
 pytest --browser chromium --browser firefox --browser webkit
 ```

## How to Run Tests via Docker

1.  Build the Docker image:
    ```bash
    docker build -t optibet-tests .
    ```
2.  Run the tests inside the container:
    ```bash
    docker run --rm -v $(pwd)/allure-results:/app/allure-results optibet-tests
    ```

## How to Generate/View Allure Report

1.  Generate Allure results by running the tests (the previous commands already do this).
2.  Install the Allure command-line tool (if not already installed). You can find instructions [here](https://docs.qameta.io/allure/#_installing_a_commandline).
3.  Serve the Allure report:
    ```bash
    allure serve allure-results
    ```
    This will open the report in your web browser.

4.  **Generate Static Report:**
    To generate a static HTML report folder (e.g., for hosting or CI artifacts):
    ```bash
    allure generate allure-results --clean -o allure-report
    ```
    The report will be generated in the `allure-report` folder. To view it locally, run `allure open allure-report`.

## Test Rationale

The selected scenarios cover the most critical, user-facing functionalities of the website: navigation, information discovery (promotions), and core user actions (registration, login). These are high-traffic areas where bugs would have the most impact.

Given more time, I would add:

*   **More comprehensive validation:** Deeper checks on the content of pages and elements.
*   **CI/CD Integration:** Setting up a pipeline (e.g., GitHub Actions) to run tests automatically on every code change.

