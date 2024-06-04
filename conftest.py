import logging
import pytest
import time

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

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        duration = time.time() - item.start_time
        item.duration = duration
        test_name = item.nodeid.split("::")[-1]
        if call.excinfo is None:
            logging.info(f"{test_name} PASSED in {duration:.2f} seconds")
        else:
            logging.info(f"{test_name} FAILED in {duration:.2f} seconds")
