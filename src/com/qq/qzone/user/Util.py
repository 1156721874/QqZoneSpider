# coding=utf-8
import re
from bs4 import BeautifulSoup

class Util:
    
    @classmethod
    def isExists(cls,driver,id):
        isExists = True
        try:
            driver.find_element_by_id(str(id))
        except:
            isExists=False    
        return   isExists  
    
    @classmethod
    def getNumber(cls,instr):
        str = ""
        try:
            mode = re.compile(r'\d+')
            str = mode.findall(instr)
        except:
            str = ""
        if len(str)>0:
            return str[0]
        else:   
            return str
        
    @classmethod
    def haveContent(cls,str):
        flag = True
        try:
           vo = str.contents[0]
           if vo!='':
             flag = True
           else:
             flag = False       
        except:
            flag = False
        return flag
    #type 0:国家,1省,2:市,3:国家-省-市
    @classmethod
    def getLocationInfo(cls,istr,type):
        istrlen = len(istr)
        country = ""
        province = ""
        city = ""
        if istrlen>0:
            dicSoup = BeautifulSoup(str(istr[0]),"html.parser")
            spans = dicSoup.findAll("span")
            spanlen = len(spans)
            if spanlen==1:
                if len(spans[0].contents)>0:
                    country=spans[0].contents[0]
            elif spanlen==2:
                if len(spans[0].contents)>0:
                    country=spans[0].contents[0]
                if len(spans[1].contents)>0:    
                    province = spans[1].contents[0]
            elif spanlen==3:
                if len(spans[0].contents)>0: 
                    country=spans[0].contents[0]
                if len(spans[1].contents)>0:     
                    province = spans[1].contents[0]
                if len(spans[2].contents)>0:     
                    city = spans[2].contents[0]
            else :
                return u"未填写"    
        if type==0:
            return country
        elif   type==1:      
            return province
        elif type==2:  
            return city
        elif type==3:  
            return country+"-"+province+"-"+city
        else :
            return ""
                