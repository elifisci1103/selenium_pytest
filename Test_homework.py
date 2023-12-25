from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest
from selenium.webdriver.common.action_chains import ActionChains 

class Test_homework:
  
    def setup_method(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self): 
     self.driver.quit()   

    def test_invalid_login(self):
        #-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage=self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
        assert errorMessage.text== "Epic sadface: Username is required"

    def test_invalid_login_username(self):
         #-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    
           username=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//input[@data-test='username']")))
           username.send_keys("standard_user")
          
           loginButton=self.driver.find_element(By.ID,"login-button")
           loginButton.click()
           
           errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
           assert errorMessage.text== "Epic sadface: Password is required"

    def test_invalid_login_password(self):

      #-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
       username=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//input[@data-test='username']")))
       username.send_keys("locked_out_user")

       password=self.driver.find_element(By.XPATH,"//input[@data-test='password']")
       password.send_keys("secret_sauce")

       loginButton=self.driver.find_element(By.ID,"login-button")
       loginButton.click()

       errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
       assert errorMessage.text== "Epic sadface: Sorry, this user has been locked out."
       
    def test_valid_login(self):

     #-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
      
      username=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//input[@data-test='username']")))
      username.send_keys("standard_user")

      password=self.driver.find_element(By.XPATH,"//input[@data-test='password']")
      password.send_keys("secret_sauce")

      loginButton=self.driver.find_element(By.ID,"login-button")
      loginButton.click()
      sleep(5)
     
      product_list= self.driver.find_elements(By.XPATH,"//div[@class='inventory_item']")

      assert (len(product_list))==6


    @pytest.mark.parametrize("username,password",[("standard_user","ab"),("problem_user","ba"),("standard_user","secret_sauce")])
    def test_parametrized_login(self,username,password):
       #Sauce Demo sayfasına parametreler ile 2 başarısız 1 başarılı girişi test ediniz.
        username = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys(username)
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
    

    def test_order_product(self):
        # Sauce Demo sayfasına giriş yaparak ürünleri price(low to high) olarak sıralayın ve 3. ürünün fiyatının 15.99$ olduğunu test ediniz.
        username = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        sortButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        sortButton.click()
        sleep(3)
        lowToHigh=self.driver.find_element(By.XPATH,"//option[text()='Price (low to high)']")
        lowToHigh.click()
        productPrice=self.driver.find_element(By.XPATH,"(//div[@class='inventory_item_price'])[3]")
        assert productPrice.text =="$15.99" 
        
        

    def test_buy_product(self):
        #Sauce Demo sayfasına giriş yaparak  herhangi bir ürünü sepete atıp gerekli işlemleri yaparak ""Thank you for your order!" yazısını görmeyi test ediniz.

        username = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        sleep(3)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        firstProduct = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"item_4_title_link")))
        firstProduct.click()
        sleep(2)
        addToCart=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart.click()
        sleep(2)
        shoppingCart=self.driver.find_element(By.XPATH,"//div[@class='shopping_cart_container']")
        shoppingCart.click()
        sleep(2)
        checkoutButton=self.driver.find_element(By.ID,"checkout")
        checkoutButton.click()
        sleep(3)
        firstNameText=self.driver.find_element(By.ID,"first-name")
        lastNameText=self.driver.find_element(By.ID,"last-name")
        postalCodeText=self.driver.find_element(By.ID,"postal-code")
        
        firstNameText.send_keys("elif")
        lastNameText.send_keys("isci")
        postalCodeText.send_keys("34000")

        continueButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        continueButton.click()

        finishButton=self.driver.find_element(By.ID,"finish")
        finishButton.click()
        sleep(30)
        orderMessage=self.driver.find_element(By.CLASS_NAME,"complete-header")
        assert orderMessage.text == "Thank you for your order!"
        
        
