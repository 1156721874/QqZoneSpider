        #********************************************************************************
        #                            QQ空间好友爬虫 
        #                author:CeaserWang time : 2016-07-01  ~  2016-07-01-14 QQ：1156721874
        #********************************************************************************

# coding=utf-8
from _overlapped import NULL
import codecs  
import os    
import re            
import shutil
import sys  
import time            
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver        
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys        

from com.qq.qzone.user.ReadFile import ReadFile 
from com.qq.qzone.user.Util import Util
from com.qq.qzone.user.UserInfo import UserInfo 
import selenium.webdriver.support.ui as ui        

#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
# executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# os.environ["webdriver.chrome.driver"] = executable_path
# os.environ["webdriver.chrome.bin"] = executable_path
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
options.add_argument("--user-data-dir="+r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/")

driver = webdriver.Chrome(chrome_options=options)
# profileDir = "C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\3xyz8wz3.default"
# profile = webdriver.FirefoxProfile(profileDir)
#driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
#driver = webdriver.Chrome(chrome_options=options)
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(chromedriver)
#wait = ui.WebDriverWait(driver,10)
currentqq = "1156721874"
maxQQCount = 10000

class QzoneSpider:
    
        #********************************************************************************
        #                            第一步: 登陆QQ空间  
        #                login() 参数用户名 密码  http://user.qzone.qq.com/1156721874  
        #********************************************************************************
    
    @classmethod
    def login(cls):
        driver.get("http://user.qzone.qq.com/1156721874")
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source.encode('utf-8','ignore'), "html.parser")
        iframe = soup.findAll("iframe", attrs={"id":"login_frame"})
        framesrc = (iframe[0].attrs["src"])
        driver.get(framesrc)
        time.sleep(2)
        driver.find_element_by_id("img_out_1156721874").click()
        time.sleep(2)
    
    def cycleCurrentQQzone(self):
        f = open("li.txt", "w",encoding='utf-8')
        for i in range(0,5):
            feed_friend_list = driver.page_source.encode('utf-8','ignore')
            feedsoup = BeautifulSoup(feed_friend_list,"html.parser")
            if i==0:
                ul = feedsoup.findAll("ul",attrs={"id":"feed_friend_list"})
                li = BeautifulSoup(str(ul),"html.parser")
                liA = li.findAll("li")[0]
                liB = li.findAll("li")[1]
                liC = li.findAll("li")[2]
                f.write(str(liA))
                f.write("\n")
                f.write(str(liB))
                f.write("\n")
                f.write(str(liC))
                f.write("\n")
            else:
                ul = feedsoup.findAll("ul",attrs={"data-page":str(i-1)})
                li = BeautifulSoup(str(ul),"html.parser")
                liA = li.findAll("li")[0]
                liB = li.findAll("li")[1]
                liC = li.findAll("li")[2]
                f.write(str(liA))
                f.write("\n")
                f.write(str(liB))
                f.write("\n")
                f.write(str(liC))
                f.write("\n")
                 
            ActionChains(driver).send_keys(Keys.END).perform()
            time.sleep(3)

        #********************************************************************************
        #                            第二步: 遍历当前QQ好已有的所有相关QQ好友信息  
        #                cycleEveryOne()   
        #********************************************************************************
      
    @classmethod
    def cycleEveryOne(cls):
        #取得当前QQ号的QQ数量 参考：http://jingyan.baidu.com/article/e2284b2b3dba8be2e6118dd1.html
        #qqlistlength = ReadFile.getFileLength()
        innerindex = 1
        while (innerindex <= maxQQCount):
            qqUserAddress = ReadFile.getOneLine(innerindex)
            cls.constructUserData(qqUserAddress)
            innerindex = innerindex+1
#             if maxQQCount<=qqlistlength:
#                 print ("the qq  user size is enough , current size is : "+str(qqlistlength))
#                 break
            
            
            
        #********************************************************************************
        #                            第三步: 获取每个好友的前三条说说内容，以及每天说说点赞qq好友的主页地址，最后获取好友的个人档案资料  
        #                constructUserData() qqUserAddress 要访问的qq好友主页地址 
        #********************************************************************************            
            
    @classmethod           
    def  constructUserData(cls,qqUserAddress):
            driver.get(str(qqUserAddress))
            #等待3秒，让页面加载完毕
            time.sleep(3)
            #声明用户实体
            userInfo = UserInfo()
            context = driver.page_source.encode('utf-8','ignore')
            contextSoup = BeautifulSoup(context,"html.parser")
            #验证是否开通QQ空间
            errorPage =  contextSoup.findAll("div",attrs={"class":"img_box error_img"})
            if ''!=errorPage and len(errorPage)>0:
                print ("对方未开通空间！")
                return
            
            isDefined =  contextSoup.findAll("p",attrs={"class":"tips"})
            #验证当前被访问的用户是否可以被访问。
            if ''!=isDefined and len(isDefined)!=0:
                if u'主人设置了权限，您可通过以下方式访问'==isDefined[0].contents[0]:
                    print (isDefined[0].contents[0])
                    return 
            #所有的说说以及动态都在内置的frame里边，因此要切换到需要的frame，首先判断iframe是否存在【部分用户没有任何动态会导致程序异常】
            elif Util.isExists(driver,"QM_Feeds_Iframe") :
                theTitle = driver.find_element_by_tag_name("title").get_attribute("innerHTML")
                tilesplit = theTitle.split("[")
                qq =  Util.getNumber(tilesplit[1]) 
                nick = tilesplit[0]
                userInfo.setQq(qq)
                userInfo.setNick(nick)
                userInfo.setPqq(currentqq)
                print ("currnent QQ is : "+str(qq))
                #切换到iframe操作
                driver.switch_to_frame("QM_Feeds_Iframe")
                #host_home_feedslen = driver.find_element_by_id("host_home_feeds")
                if not Util.isExists(driver,"host_home_feeds"):
                    return
                feed_friend_list = driver.find_element_by_id("host_home_feeds").get_attribute("innerHTML")
                ul =  BeautifulSoup(str(feed_friend_list),"html.parser")
                lies = ul.findAll("li",attrs={"class":"f-single f-s-s"})
                lengthOflies = len(lies)
                for j in range(0,lengthOflies):
                    #print (lies[j])
                    #记录前三条说说内容
                    if j<=3:
                        innerLi = BeautifulSoup(str(lies[j]),"html.parser")
                        timeDiv = innerLi.findAll("div",attrs={"class":"info-detail"})[0]
                        timeSpan = BeautifulSoup(str(timeDiv),"html.parser")
                        theTime = timeSpan.findAll("span")[0].contents[0]
                        #说说发布时间
                        userInfo.setTime(theTime)
                        #说说内容
                        modIfo = innerLi.findAll("div",attrs={"class":"f-info"})
                        if ''!=modIfo and len(modIfo)!=0:
                            modIfoSoup = BeautifulSoup(str(modIfo[0]),"html.parser")
                            span = modIfoSoup.findAll("span")
                            #是否是上传图片类型的说说
                            if ''!=span and len(span)>0:
                                userInfo.setMode(span[0].contents[0])
                            else:
                                #非发表图片，手动发布的说说记录
                                if Util.haveContent(modIfo[0]):
                                    userInfo.setMode(modIfo[0].contents[0])
                                else:
                                    userInfo.setMode("NULL")    
                        user_list = innerLi.findAll("div",attrs={"class":"user-list"})
                        #是否有点赞用户
                        if ''!=user_list and len(user_list)!=0:
                            flower = BeautifulSoup(str(user_list[0]),"html.parser")
                            flowLink = flower.findAll("a")
                            flowerLength = len(flowLink)
                            #记录点赞用户的QQ空间链接，为下一层的数据爬取做准备
                            for n in range(0,flowerLength):
                                userMainLink = flowLink[n].attrs["href"]
                                if 'javascript:;'!=userMainLink:
                                    #print (">>>>>>>>>"+userMainLink)#javascript:;
                                    ReadFile.writeQQListFile(str(userMainLink))
                                    #ReadFile.writeQQListFile("\n")
                    else:
                        #说说信息记录完毕，然后切换到默认上下文
                        driver.switch_to_default_content()
                        #得到用户私人信息
                        moreUserInfo = driver.find_elements_by_link_text(u"查看详细资料") 
                        if len(moreUserInfo)>0:
                            try:
                                moreUserInfo[0].click()
                            except:
                                continue
                            time.sleep(2)
                            #print (BeautifulSoup(driver.page_source.encode('utf-8','ignore'),"html.parser"))
                            driver.switch_to_frame("app_canvas_frame")
                            info_preview = driver.find_element_by_id("info_preview").get_attribute("innerHTML")
                            info_previewSoup =  BeautifulSoup(str(info_preview),"html.parser") 
                            #print (info_previewSoup)
                            
                            fsex = info_previewSoup.findAll("div",attrs={"id":"sex"})[0]
                            if len(fsex.contents)>0:
                                sex = fsex.contents[0]                                                                      #性别
                                userInfo.setSex(sex)
                            fage = info_previewSoup.findAll("div",attrs={"id":"age"})[0]                                    #年龄
                            if len(fage.contents)>0:
                                age = fage.contents[0]  
                                userInfo.setAge(age)   
                            fbirthday = info_previewSoup.findAll("div",attrs={"id":"birthday"})[0]                           #生日
                            if len(fbirthday.contents)>0:
                                birthday = fbirthday.contents[0]
                                userInfo.setBirthday(birthday)
                            fastro = info_previewSoup.findAll("div",attrs={"id":"astro"})[0]                                 #星座
                            if len(fastro.contents)>0:
                                astro = fastro.contents[0]
                                userInfo.setStar(astro)
                            live_address = info_previewSoup.findAll("div",attrs={"id":"live_address"})                       #居住地
                            userInfo.setLocation(Util.getLocationInfo(live_address, 3))
                            #print (str(live_address))
                            fmarriage = info_previewSoup.findAll("div",attrs={"id":"marriage"})[0]                           #婚姻
                            if len(fmarriage.contents)>0:
                                marriage =  fmarriage.contents[0]
                                userInfo.setMarital(marriage)
                            fblood = info_previewSoup.findAll("div",attrs={"id":"blood"})[0]                                 #血型
                            if len(fblood.contents)>0:
                                blood = fblood.contents[0]
                                userInfo.setBlood(blood)
                                
                            hometown_address = info_previewSoup.findAll("div",attrs={"id":"hometown_address"})               #故乡
                            userInfo.setHometownAddress(Util.getLocationInfo(hometown_address,3))
                            #print (str(hometown_address))
                            fcareer = info_previewSoup.findAll("div",attrs={"id":"career"})[0]                               #职业
                            if len(fcareer.contents)>0:
                                career = fcareer.contents[0]
                                userInfo.setOccupation(career)
                            
                            fcompany = info_previewSoup.findAll("div",attrs={"id":"company"})[0]                             #公司名称
                            if len(fcompany.contents)>0:
                                company = fcompany.contents[0]
                                userInfo.setCompanyName(company)
                            company_caddress = info_previewSoup.findAll("div",attrs={"id":"company_caddress"})               #公司所在地
                            userInfo.setCompanyLocation(Util.getLocationInfo(company_caddress,3))
                            #print (str(company_caddress))
                            fcaddress = info_previewSoup.findAll("div",attrs={"id":"caddress"})[0]                           #详细地址
                            if len(fcaddress.contents)>0:
                                caddress = fcaddress.contents[0]
                                userInfo.setDetailAddress(caddress)
                            
            #print (userInfo.toStr())   
            if userInfo.getQq()!='':
                ReadFile.writeAllQqUsersInfo(userInfo.toStr())     
            return
                       
QzoneSpider.login()
QzoneSpider.cycleEveryOne()
