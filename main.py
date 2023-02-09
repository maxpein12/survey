from selenium import webdriver
import time
import os
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSciCCH5msji405qSZyqjZgJADr_DlVu_Zv50h8ZSyJ3TBY8Vw/viewform?fbclid=IwAR1bcACEXuKcWhsroZQkj_t8GKydDAfIdUVss2_nNCTEmA-L5w72nlc1-OA')

time.sleep(2)

first = web.find_element_by_xpath('//*[@id="i10"]/div[3]/div')
first.click()

second = web.find_element_by_xpath('//*[@id="i26"]/div[3]/div')
second.click()

trd = web.find_element_by_xpath('//*[@id="i48"]/div[3]/div')
trd.click()

frt = web.find_element_by_xpath('//*[@id="i61"]/div[3]/div')
frt.click()

ftf = web.find_element_by_xpath('//*[@id="i74"]/div[3]/div')
ftf.click()

sxt = web.find_element_by_xpath('//*[@id="i84"]/div[3]/div')
sxt.click()

svb = web.find_element_by_xpath('//*[@id="i97"]/div[3]/div')
svb.click()

et = web.find_element_by_xpath('//*[@id="i110"]/div[3]/div')
et.click()

nn = web.find_element_by_xpath('//*[@id="i123"]/div[3]/div')
nn.click()

tn = web.find_element_by_xpath('//*[@id="i133"]/div[3]/div')
tn.click()

lvn = web.find_element_by_xpath('//*[@id="i155"]/div[3]/div')
lvn.click()

twv = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div')
twv.click()

trt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div')
trt.click()

fds = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div')
fds.click()

efc = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div')
efc.click()

sxa = web.find_element_by_xpath('//*[@id="i172"]/div[3]/div')
sxa.click()

sva = web.find_element_by_xpath('//*[@id="i185"]/div[3]/div')
sva.click()

egq = web.find_element_by_xpath('//*[@id="i201"]/div[3]/div')
egq.click()

# sbm = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
# sbm.click()

# get_confirm = web.find_element_by_css_selector(".vHW8K")
# print(get_confirm)
# if ((get_confirm.text) == "Naitala ang iyong tugon."):
#     os.system("taskkill /im chrome.exe /f")
#     time.sleep(2)
#     os.system("python C:\\Users\\rov\\PycharmProjects\\survey\\main.py")

