from playwright.sync_api import sync_playwright

def acessar_site_com_firefox():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        context = browser.new_context()

        # Abre uma nova página
        page = context.new_page()
        page.goto('https://example.com')

        # Exibe o título da página
        print("Título da página:", page.title())

        # Fecha o navegador
        browser.close()

# Chamada da função para acessar o site com Firefox
acessar_site_com_firefox()
