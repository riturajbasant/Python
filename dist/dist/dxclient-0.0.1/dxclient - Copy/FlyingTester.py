#setting environment
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))



#import dxclient

#from dxclient import *
from dxclient.constants import *
from dxclient.constants import Parameters as params
from dxclient.SupportClasses import *
from dxclient.Query import *
from dxclient.DxOpenClient import DxOpenClient
#import dxclient.dxlxml as DxlObjects


# QA_DXOPEN_URL   = constants.QA_DXOPEN_URL
# PROD_DXOPEN_URL = constants.PROD_DXOPEN_URL
# QA_DXLAPI_URL   = constants.QA_DXLAPI_URL
# PROD_DXLAPI_URL = constants.PROD_DXLAPI_URL

client     = None
clientFlag = None


def loginClient(realm, userName = Credentials.USER, password = Credentials.PASSWORD, apiPath = ApiPath.DxOpen ):
    global clientFlag
    global client
    if clientFlag is not None:
        if clientFlag != realm:
            print 'Different realm login detected.'
            print 'Current realm: ' + clientFlag + '. New realm: ' + realm
            client.logout()

    client = DxOpenClient(getUrl(realm, apiPath))
    client.setCredentials(userName, password)
    client.checkLogin()
    clientFlag = realm
    print realm + ' realm logged in!'

def getUrl(realm, apiPath):
    if realm == Realm.QA:
        return QA_DXOPEN_URL if apiPath == ApiPath.DxOpen else QA_DXLAPI_URL
    elif realm == Realm.PROD:
        return PROD_DXOPEN_URL if apiPath == ApiPath.DxOpen else PROD_DXLAPI_URL
    else:
        return None

def logoutClient():
    global client
    global clientFlag
    print 'Attempting logout for '+ clientFlag.value + ' realm...'
    client.logout()
    clientFlag = None
    print 'Logout successful!'


def client_Data():
    loginClient(Realm.QA, userName = Credentials.API2_USER, password = Credentials.API2_PASSWORD, apiPath=ApiPath.DxlApi)
    my_Fields = ['LendableValue', 'LenderValueOnLoan', 'Utilisation']

    #creating query object now
    query = DxlClientQuery()
    query.addFields(my_Fields)
    query.addIdentifier('Market', 'S&P500')
    query.setSource('Client.Market')
    query.setFromDate('20180522') #('22 May 2018')
    query.setToDate('20180524') #('22 May 2018')

#    marketData = client.getClient(query).get_Market()
    marketData = client.getClient(query)


    for data in marketData:
        dates = data.get_DataDate()
        for dataDate in dates:
            chunk = dataDate.get_Inventory()
            print 'Date: '+ unicode(dataDate.value.strftime('%d %b %Y'))
            print 'Lendable Value: ' + unicode(chunk.LendableValue)
            print 'Lender Value On Loan: ' + unicode(chunk.LenderValueOnLoan)
            print 'Utilisation: ' + unicode(chunk.Utilisation)



def Benchmark_Performance_Data():
    loginClient(Realm.QA, userName = Credentials.API2_USER, password = Credentials.API2_PASSWORD, apiPath = ApiPath.DxlApi)
    fields = ['Date' , 'MarketArea', 'ValueOnLoan', 'ValueOnLoanVsCash', 'SLDailyReturn', 'RiDailyReturn', 'TotalReturn']

    #creating query object now
    query = DxlBenchmarkQuery()
    query.addFields(fields)
    query.addIdentifier('BenchmarkFilter1', 'All Client')
    query.setSource('BenchmarkPerformance.MarketDetail')
    query.addIdentifier('Market', 'All Securities')
    query.setFromDate('20180522') #('22 May 2018')
    query.setToDate('20180522') #('22 May 2018')

    marketData = client.getBenchmarkPerformance(query).MarketDetail # I receive the data here....but it is not market data...an enclosing class of it. Dont get misled by name.

    dataList = marketData._PluralBinding__list
    for data in dataList:
        dates = data.get_DataDate()
        for dataDate in dates:
            reinvestment = dataDate.get_Reinvestment()
            trading = dataDate.get_Trading()
            print 'Date: '+ unicode(dataDate.value.strftime('%d %b %Y'))
            print 'Market Area: ' + unicode(trading.MarketArea)
            print 'SL Daily Return: ' + unicode(trading.SlDailyReturn)
            print 'Total Return: ' + unicode(trading.TotalReturn)
            print 'ValueOnLoan: ' + unicode(trading.ValueOnLoan)
            print 'ValueOnLoan Vs Cash: ' + unicode(trading.ValueOnLoanVsCash)
            print 'Ri Daily Return: ' + unicode(reinvestment.RiDailyReturn)

#client_Data()
Benchmark_Performance_Data()
logoutClient()
