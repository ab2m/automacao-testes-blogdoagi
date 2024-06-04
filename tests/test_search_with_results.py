import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.blog_page import BlogPage

def test_search_with_results():
    driver = webdriver.Chrome()
    blog_page = BlogPage(driver)
    
    try:
        blog_page.open()
        blog_page.click_search_icon()
        blog_page.search("drex")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, blog_page.results_xpath))
        )
        
        results = blog_page.get_results()
        assert len(results) > 0
    except Exception as e:
        print(f"Erro no teste de busca com resultados: {e}")
        raise
    finally:
        driver.quit()
