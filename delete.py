from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://twitter.com/i/flow/login")
time.sleep(3)

loginInput = "label.css-1dbjc4n.r-1roi411.r-z2wwpe.r-rs99b7.r-18u37iz"
loginInputBtn = driver.find_element(By.CSS_SELECTOR, loginInput)
loginInputBtn.send_keys("USERNAME")

nextBtn = driver.find_element(By.XPATH,"//span[text()='Next']")
nextBtn.click()
time.sleep(3)

passwdInput = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
passwdInput.send_keys("PASSWORD")

LoginBtn = driver.find_element(By.XPATH,"//span[text()='Log in']")
LoginBtn.click()
time.sleep(3)

driver.get("https://twitter.com/USERNAME")
# Usa o de baixo no lugar do de cima pra deletar as replies
# driver.get("https://twitter.com/USERNAME/with_replies")
time.sleep(3)

# Numero de tweets pra deletar
for _ in range(3000):   
    try:
            
        ellipsisBtn = driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1p0dtai.r-xoduu5.r-1d2f490.r-xf4iuw.r-1ny4l3l.r-u8s1d.r-zchlnj.r-ipm5af.r-o7ynqc.r-6416eg")
        driver.execute_script("arguments[0].click();", ellipsisBtn)

        deleteBtn = driver.find_element(By.XPATH,"//span[text()='Delete']")
        driver.execute_script("arguments[0].click();", deleteBtn)

        deleteConfirm = driver.find_element(By.XPATH,"//span[text()='Delete']")
        driver.execute_script("arguments[0].click();", deleteConfirm)

    except:
        # 3 Segundos pra você clicar no unRetweet ou quem sabe 5 minutos
        # pra você implementar o click lá, eu fiquei com preguiça.
        time.sleep(3)