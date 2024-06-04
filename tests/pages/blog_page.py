from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BlogPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://blogdoagi.com.br/"
        self.search_icon_xpath = "//*[@class='ast-search-menu-icon slide-search']"
        self.search_input_id = "search-field"
        self.no_results_message_xpath = "//*[contains(text(), 'Lamentamos, mas nada foi encontrado para sua pesquisa, tente novamente com outras palavras.')]"
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
            WebDriverWait(self.driver, 4).until(
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
            # Verificar se o no_results_message_xpath está visível
            WebDriverWait(self.driver, 4).until(
                EC.visibility_of_element_located((By.XPATH, self.no_results_message_xpath))
            )
            return self.driver.find_element(By.XPATH, self.no_results_message_xpath)
        except Exception as e:
            print(f"Erro ao obter a mensagem de 'sem resultados': {e}")
            raise

    def get_results(self):
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, self.results_xpath))
            )
            return self.driver.find_elements(By.XPATH, self.results_xpath)
        except Exception as e:
            print(f"Erro ao obter os resultados da busca: {e}")
            raise
