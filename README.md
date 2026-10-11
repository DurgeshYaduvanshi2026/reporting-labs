# Reporting Labs Test Automation Report

An open-source, zero-config, self-contained HTML reporting plugin for Pytest. Get advanced analytics, interactive timelines, and trends without setting up servers, databases, or runtime dependencies like Node.js.

## Features

* **Zero Infrastructure:** Generates a single, self-contained HTML file. No login or server required.
* **Smart Analytics:** Automatically tracks execution trends, new vs. known failures, and flaky tests over multiple runs.
* **Rich Timelines:** Embed high-level metadata, nested execution steps, API transactions, and media attachments.

---

## Getting Started

### Step 1: Install ReportLab
Download and install the latest open-source version using `pip`:
```bash
pip install reporting-labs
```

### Step 2: Verify the Installation
Check the installed package version and details:
```bash
pip show reporting-labs
```

### Step 3: Run Tests and View the Report
Execute your Pytest suite. Run the suite twice to enable trend tracking, new-vs-known failure analysis, and flaky test detection.

```bash
# Run your pytest suite
pytest

# Open the self-contained HTML report
open reporting-labs/index.html         # macOS
xdg-open reporting-labs/index.html    # Linux
start reporting-labs\index.html        # Windows
```

---

## Enhancing Your Reports (Optional)

You can enrich your test code using custom hooks and helpers to unlock advanced analytics, structured timelines, and clear execution steps inside your final dashboard.

### Implementation Example (`test_login.py`)

```python
from playwright.sync_api import Page, expect
import pytest
from config import Config
from reporting_labs import meta, log, test_data, step
from src.pages.orangehrm_login_page import LoginPage
from src.pages.orangehrm_home_page import HomePage

@pytest.mark.meta(
    priority="P1",
    owner="Durgesh Yaduvanshi",
    feature="login",
    story="• As a Returning User, I Can Log In Successfully with Valid Credentials",
)
def test_login(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    login_page.login(Config.Username, Config.Password)
    log("Login successfully")
    
    expect(home_page.heading_message).to_be_visible()
```

### Component Breakdown

* **`@pytest.mark.meta(...)`**: Drives high-level dashboard intelligence. It populates the *Needs-Attention Ranking*, feeds metrics into *Breakdown Charts*, and applies *Per-Test Chips* (like Priority and Owner) directly onto the test row.
* **`log(...)`**: Adds custom text logs chronologically into the interactive test timeline for simpler debugging.
* **`step(...)`**: Groups code blocks into nested, expandable steps to break down long, complex end-to-end workflows.
* **`test_data(...)`**: Injects dedicated data blocks into the report to showcase the exact inputs, configurations, or environments used.
* **`api(...)` and `attach(...)`**: Dynamically logs backend API network transactions and embeds attachments (like failure screenshots or server logs) directly into the test file archive.

---

## Managing the Plugin

### Exporting Reports
* **Export as PDF:** The dashboard report can be exported directly as a PDF document for distribution.

### Disabling the Plugin
If you need to temporarily disable the reporting plugin for a specific run, use either of the following flags:

```bash
pytest -p no:reporting_labs
# OR
pytest --no-rl
```
