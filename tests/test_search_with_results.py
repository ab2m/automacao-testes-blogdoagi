from pages.blog_page import BlogPage
from selenium import webdriver

def test_search_with_results(driver):
    blog_page = BlogPage(driver)
    
    try:
        blog_page.open()
        blog_page.click_search_icon()
        blog_page.search("Drex")
        
        results = blog_page.get_results()
        assert len(results) > 0
    except Exception as e:
        print(f"Erro no teste de busca com resultados: {e}")
        raise
    
        
