import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_failed_login_with_empty_password(self): 
        
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_c_failed_login_with_empty_email_and_password(self): 
        
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() 
        time.sleep(1)

        
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test_d_failed_login_with_empty_email(self): 
        
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("persija") 
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_e_success_register(self): 
        
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#name_register").send_keys("ondrej") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#email_register").send_keys("ondrej@kudela.com") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("persija") 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_f_failed_register_with_empty_name_email_and_password(self): 
        
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#name_register").send_keys("") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#email_register").send_keys("") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
