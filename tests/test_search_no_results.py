import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.blog_page import BlogPage

def test_search_no_results():
    driver = webdriver.Chrome()
    blog_page = BlogPage(driver)
    
    try:
        blog_page.open()
        blog_page.click_search_icon()
        blog_page.search("xyz123")
        
        # Usar espera explícita para o elemento no_results_message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, blog_page.no_results_message_xpath))
        )
        
        no_results_message = blog_page.get_no_results_message()
        assert no_results_message.is_displayed()
    except Exception as e:
        print(f"Erro no teste de busca sem resultados: {e}")
        raise
    finally:
        driver.quit()
