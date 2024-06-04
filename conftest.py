import logging
import pytest
import time
from selenium import webdriver

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
 
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

# Configuração do logger
logging.basicConfig(
    filename='test_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.start_time = time.time()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Calcular a duração do teste
    if call.when == "call":
        duration = time.time() - item.start_time
        item.duration = duration
        test_name = item.nodeid.split("::")[-1]
        if call.excinfo is None:
            logging.info(f"{test_name} PASSED in {duration:.2f} seconds")
        else:
            logging.info(f"{test_name} FAILED in {duration:.2f} seconds")



def pytest_html_report_title(report):
    report.title = "Relatório de Testes do Blog do Agi"
