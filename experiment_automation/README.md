UI Automation Level 2 Framework

Tech Stack
- Selenium
- Pytest
- Docker Selenium Grid
- Allure Reports


cd docker 
docker-compose up -d

Run Tests

pytest -n 3

Run with Allure

pytest --alluredir=reports
allure serve reports