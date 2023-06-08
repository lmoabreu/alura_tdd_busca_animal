from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        # Obs: baixar drive e referenciar no PATH
        self.browser = webdriver.Chrome()
        self.animal = Animal.objects.create(
            nome_animal='leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )

    def tearDown(self):
        self.browser.quit()

    # def test_abre_janela_do_chrome(self):
    #   self.browser.get(self.live_server_url)

    # def test_falhador(self):
    #   """teste de exemplo de erro"""
    #   self.fail('Teste falhou!')

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando
        find_element(By.CSS_SELECTOR, 'exemplo')
        """

        home_page = self.browser.get(self.live_server_url + '/')
        # brand_element =  self.browser.find_element_by_css_selector('.navbar')
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        buscar_animal_input.send_keys('leão')
        # self.browser.find_element_by_css_selector('form button').click()
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)
