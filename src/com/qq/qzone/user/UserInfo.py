# coding=gbk
class UserInfo:
    __qq =''                    #qq号码
    __nick=''                   #昵称
    __pqq=''                    #所属QQ号
    __sex=''                    #性别
    __age=''                    #年龄
    __birthday=''               #生日
    __star=''                   #星座
    __location=''               #居住地
    __marital=''                #婚姻状况
    __blood=''                  #血型
    __hometownAddress=''        #故乡
    __occupation=''             #职业
    __companyName=''            #公司名称
    __companyLocation=''        #公司所在地
    __detailAddress=''          #详细地址
    __mode=''                   #说说内容
    __time=''                   #发表时间
    
    def toStr(self):
        str = "{"
        str += "'qq':"+"'"+self.getQq()+"',"
        str += "'nick':'"+self.getNick()+"',"
        str += "'pqq':'"+self.getPqq()+"',"
        str += "'sex':'"+self.getSex()+"',"
        str += "'age':'"+self.getAge()+"',"
        str += "'birthday':'"+self.getBirthday()+"',"
        str += "'star':'"+self.getStar()+"',"
        str += "'location':'"+self.getLocation()+"',"
        str += "'marital':'"+self.getMarital()+"',"
        str += "'blood':'"+self.getBlood()+"',"
        str += "'hometownAddress':'"+self.getHometownAddress()+"',"
        str += "'occupation':'"+self.getOccupation()+"',"
        str += "'companyName':'"+self.getCompanyName()+"',"
        str += "'companyLocation':'"+self.getCompanyLocation()+"',"
        str += "'detailAddress':'"+self.getDetailAddress()+"',"
        str += "'mode':'"+self.getMode()+"',"
        str += "'time':'"+self.getTime()
        str += "'}"
        return str
    
    def setQq(self,qq):
        self.__qq=qq
        
    def getQq(self):
        return self.__qq
    
    def setNick(self,nick):
        self.__nick=nick
    
    def getNick(self):
        return  self.__nick   
    
    def setPqq(self,pqq):
        self.__pqq = pqq
    
    def getPqq(self):
        return self.__pqq
    
    def getSex(self):
        return self.__sex
    
    def setSex(self,sex):
        self.__sex=sex
    
    def setAge(self,age):  
        self.__age=age
        
    def getAge(self):
        return self.__age    
        
    def setBirthday(self,birthday):  
        self.__birthday=birthday
        
    def getBirthday(self):
        return self.__birthday
    
    def setStar(self,star):
        self.__star = star
    
    def getStar(self):
        return self.__star
        
    def setLocation(self,location):    
        self.__location = location
    
    def getLocation(self):
        return self.__location
    
    def setMarital(self,marital):
        self.__marital = marital
    
    def getMarital(self):
        return self.__marital    
    
    def setBlood(self,blood):
        self.__blood = blood
    
    def getBlood(self):
        return self.__blood
    
    def getHometownAddress(self):
        return self.__hometownAddress
    
    def setHometownAddress(self,hometownAddress):
        self.__hometownAddress=hometownAddress
    
    def setOccupation(self,occupation):
        self.__occupation = occupation
    
    def getOccupation(self):
        return self.__occupation    
    
    def setCompanyName(self,companyName):
        self.__companyName = companyName
    
    def getCompanyName(self):
        return self.__companyName        
    
    def setCompanyLocation(self,companyLocation):
        self.__companyLocation = companyLocation
    
    def getCompanyLocation(self):
        return self.__companyLocation 
    
    def setDetailAddress(self,detailAddress):
        self.__detailAddress = detailAddress
    
    def getDetailAddress(self):
        return self.__detailAddress     
    
    def setMode(self,mode):
        if self.getMode()=='':
            self.__mode+= str(mode)
        else:
            self.__mode+= "@_@"+str(mode)
        
    def getMode(self):    
        return self.__mode
    
    def setTime(self,time):
        if self.getTime()=='':
            self.__time+=str(time)
        else:
            self.__time += "@_@"+str(time)
        
    def getTime(self):
        return self.__time
    
        
# u = UserInfo()
# u.setAge("120")
# u.setMode("ooo")
# print (u.toStr())
    