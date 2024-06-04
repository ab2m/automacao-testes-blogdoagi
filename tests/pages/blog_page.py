from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BlogPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://blogdoagi.com.br/"
        self.search_icon_xpath = "//*[@id='ast-desktop-header']/div[1]/div/div/div/div[3]/div[2]/div"
        self.search_input_id = "search-field"
        self.no_results_message_xpath = "//*[contains(text(), 'Lamentamos')]"
        self.results_xpath = "//div[@class='ast-row']/article"

    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print(f"Erro ao abrir a URL: {e}")
            raise

    def click_search_icon(self):
        try:
            self.driver.find_element(By.XPATH, self.search_icon_xpath).click()
        except Exception as e:
            print(f"Erro ao clicar no ícone de busca: {e}")
            raise

    def search(self, query):
        try:
            # Verificar se o search_input_id está visível
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.search_input_id))
            )
            search_input = self.driver.find_element(By.ID, self.search_input_id)
            search_input.send_keys(query)
            search_input.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Erro ao realizar a busca: {e}")
            raise

    def get_no_results_message(self):
        try:
            return self.driver.find_element(By.XPATH, self.no_results_message_xpath)
        except Exception as e:
            print(f"Erro ao obter a mensagem de 'sem resultados': {e}")
            raise

    def get_results(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.results_xpath))
            )
            return self.driver.find_elements(By.XPATH, self.results_xpath)
        except Exception as e:
            print(f"Erro ao obter os resultados da busca: {e}")
            raise
