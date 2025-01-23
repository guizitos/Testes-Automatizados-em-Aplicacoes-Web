import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        # Caminho para o Edge WebDriver
        edge_driver_path = r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe"
        service = Service(edge_driver_path)
        self.driver = webdriver.Edge(service=service)
        self.wait = WebDriverWait(self.driver, 30)  # Define um tempo de espera de 10 segundos
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        'Realiza login no sistema com as credenciais fornecidas.'
        self.wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

    def test_successful_login(self):
        'Teste de login bem-sucedido.'
        self.login('standard_user', 'secret_sauce')
        self.delay(2)  # atraso de 2 segundos 
        self.wait.until(EC.url_contains("inventory"))
        self.assertIn("inventory", self.driver.current_url)

    def test_invalid_login(self):
        'Teste de login com credenciais inválidas.'
        self.login('invalid_user', 'wrong_password')
        self.delay(2)  
        error_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container'))).text
        self.assertIn("Epic sadface", error_message)

    def test_add_to_cart(self):
        'Teste de adicionar produto ao carrinho.'
        self.login('standard_user', 'secret_sauce')
        self.delay(2)  
        self.wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        cart_count = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))).text
        self.assertEqual(cart_count, '1')

    def test_remove_from_cart(self):
        'Teste de remover produto do carrinho.'
        self.login('standard_user', 'secret_sauce')
        self.delay(2)  
        self.wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        self.delay(2)  
        self.wait.until(EC.element_to_be_clickable((By.ID, 'remove-sauce-labs-backpack'))).click()
        cart_count_elements = self.driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
        self.assertEqual(len(cart_count_elements), 0)

    def test_checkout(self):
        'Teste de finalizar compra.'
        self.login('standard_user', 'secret_sauce')
        self.delay(2)  
        self.wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        self.delay(2)  
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

        # Preenchimento de informações do cliente
        self.wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys('Test')
        self.driver.find_element(By.ID, 'last-name').send_keys('User')
        self.driver.find_element(By.ID, 'postal-code').send_keys('12345')
        self.delay(2)  
        self.driver.find_element(By.ID, 'continue').click()

        # Finalização da compra
        self.wait.until(EC.element_to_be_clickable((By.ID, 'finish'))).click()
        self.delay(2)  
        confirmation_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header'))).text
        self.assertEqual(confirmation_message.upper().rstrip('!'), 'THANK YOU FOR YOUR ORDER')

    def delay(self, seconds=5):
        'atraso para fins de observação.'
        time.sleep(seconds)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False) 
