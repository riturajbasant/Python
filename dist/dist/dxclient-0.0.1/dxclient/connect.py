import cookielib, httplib, uuid, os.path
from io import open
import urllib2, urllib
import urllib2, urllib, urlparse
import urllib2, urllib
import dxclient.constants as const
from dxclient.constants import Parameters as params

METHOD_POST = 'POST'
METHOD_GET = 'GET'

RETRY_COUNT = 1
TIMEOUT_MS = 60000

class DxlClient(object):

    m_baseUrl     = ''
    m_cookieJar   = None
    m_loggedIn    = False
    m_loginFailed = False
    m_userName    = ''
    m_passWord    = ''

    def __init__(self, baseUrl):
        self.m_baseUrl = baseUrl
        if self.m_baseUrl[:-1] != '/':
            self.m_baseUrl = self.m_baseUrl + '/'
        self.m_cookieJar = cookielib.CookieJar()

    def setCredentials(self, username, password):
        if self.m_loggedIn:
            self.logout()
        self.m_userName = username
        self.m_password = password
        self.m_loginFailed = False

    def makeWebRequest(self, url, method, parameters):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.m_cookieJar))
        try:
            if method == METHOD_POST :
                parameters=parameters.encode(u"utf-8")
                return opener.open(url, parameters, TIMEOUT_MS)
            else:
                return opener.open(url, None, TIMEOUT_MS)
        except Exception, e:
            print ('Error : '),
            print (e)
            raise

    def getUrl(self, pageName):
        return self.m_baseUrl + "Xml/" + pageName + ".aspx"

    def logout(self):
        try:
            response = self.makeWebRequest(self.getUrl(const.PAGE_LOGOUT), METHOD_GET, None)
        except urllib2.HTTPError, e:
            print 'Error logging out'
        self.m_loggedIn = False
        self.m_loginFailed = False

    def login(self):
        if self.m_userName != '' :
                parameters = params.PARAM_USERNAME + '=' + urllib.quote(self.m_userName)
                parameters = parameters + '&' + params.PARAM_PASSWORD + '=' + urllib.quote(self.m_password)
                try:
                    response = self.makeWebRequest(self.getUrl(const.PAGE_LOGIN), METHOD_POST, parameters)
                    self.m_loggedIn = True
                except urllib2.HTTPError, e:
                    self.m_loggedIn = False
        return self.m_loggedIn

    def checkLogin(self):
        if self.m_loginFailed == False :
            if self.m_loggedIn == False :
                self.login()
        return self.m_loggedIn

    def cleanUp(self):
        if self.m_loggedIn == True :
            self.logout()

    def buildRequest(self, page, parameters):
        result = self.getUrl(page)
        result = result + '?'
        first = True
        for key, value in parameters.items():
            if first == False :
                result = result + '&'
            result = result + key
            result = result + '='
            result = result + urllib.quote(value)
            first = False
        return result

    def makeAuthenticatedRequest(self, query):
        response = None
        if self.checkLogin() == True :
            try :
                response = self.makeWebRequest(query, "GET", None)
            except urllib2.HTTPError, e:
                print ('Error making request :'),
                print (e.code)
                response = None
        return response

    def getXml(self, pageName, parameters):
        result = ''
        response = self.makeAuthenticatedRequest(self.buildRequest(pageName, parameters))
        if response != None :
            result = response.read()
        return result

    def getLocalImage(self, pageName, parameters, localDir):
        result = ''
        response = self.makeAuthenticatedRequest(self.buildRequest(pageName, parameters))
        if response != None :
            try :
                path = os.path.join(localDir, unicode(uuid.uuid4()) + u'.png')
                file = open(path, 'wb')
                file.write(response.read())
                file.close()
                result = path
            except IOError, e:
                raise
        return result
