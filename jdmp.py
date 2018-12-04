import requests

url = 'http://122.224.74.182:6061/JDMP/SystemAction.do?method=login'
urlquantity = 'http://122.224.74.182:6061/JDMP/DeviceAction.do?method=DeviceManage'
urlnoread = 'http://122.224.74.182:6061/JDMP/queryreport.do?method=RptUnreadDevQuery'
logindata={
    'usercode':'admin',
    'password':'admin'
}
noreaddata={
    'begindate':'2018-12-02',
    'enddate':'2018-12-02',
    'limit':'20'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
# res = requests.get(url，headers=headers)
response=requests.post(url,data=logindata,headers=headers)
# print (response.text)
# print (response.cookies)
# print (type(response.cookies))
cookies=response.cookies

resnoread=requests.post(urlnoread,data=noreaddata,headers=headers,cookies=cookies)
resquantity=requests.get(urlquantity,cookies=cookies)
print(resquantity.text)
