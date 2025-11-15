A Behavior-Driven Development (BDD) automation framework built using:

Python 3
Behave (Gherkin BDD)
Selenium WebDriver
Page Object Model (POM)
Environment variables (.env)
ALLURE reporting

**This framework automates key workflows of Zenportal Login & Logout functionality.**

Task18-BDD_Framework/
├── Feature/
│   └── login.feature                 # All Gherkin feature files
│
├── pages/
│   ├── __init__.py
│   └── login_page.py                 # Page Object Model class
│
├── steps/
│   └── steps.py                      # Step definitions for Behave
│
├── reports/
│   └── report.html                   # Auto-generated HTML report
│
├── testdata/
│   └── testdata.json                 # Optional test input data
│
├── .env                              # Stores username/password variables
├── .gitignore                        # To hide env, reports, cache files
├── main.py                           # Optional entry point
├── requirements.txt                  # Project dependencies
└── README.md                         # Documentation


