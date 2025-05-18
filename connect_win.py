
'''
Author: Jeffrey Zhu 1624410543@qq.com
Date: 2025-04-27 16:00:01
LastEditors: Jeffrey Zhu 1624410543@qq.com
LastEditTime: 2025-04-27 16:35:17
FilePath: \CQU-auto-connect\connect_win.py
Description: File Description Here...

Copyright (c) 2025 by JeffreyZhu, All Rights Reserved. 
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 启动Chrome浏览器，要求chromedriver驱动程序已经配置到环境变量
# 将驱动程序和当前脚本放在同一个文件夹也可以
driver = webdriver.Chrome()
 
# # 手动指定驱动程序路径
# driver = webdriver.Chrome(r'D:/uusama/tools/chromedriver.exe')
 
# driver = webdriver.Ie()        # Internet Explorer浏览器
# driver = webdriver.Edge()      # Edge浏览器
# driver = webdriver.Opera()     # Opera浏览器
# driver = webdriver.PhantomJS()   # PhantomJS

driver = webdriver.Chrome()

driver.get('http://10.254.7.4')  # 打开指定路径的页面

user = "20241539"  # 用户名
password = "qQ13527503399_-"    # 密码

sleep(5)

# try:
    
#     userInput = WebDriverWait(driver,10).until(
#         EC.visibility_of((By.NAME,'0MKKey'))  # 找到用户名输入框)
#     )
#     print("找到元素")
# except TimeoutError:
#     print("未找到")

userInput = driver.find_element(By.NAME,'DDDDD')  # 找到用户名输入框
passwordInput = driver.find_element(By.NAME,"upass")  # 找到密码输入框
loginButton = driver.find_element(By.NAME,"0MKKey")  # 找到登录按钮


userInput.send_keys(user)  # 输入用户名
passwordInput.send_keys(password)  # 输入密码

loginButton.click()  # 点击登录按钮

sleep(5)

driver.quit()  # 关闭当前窗口
