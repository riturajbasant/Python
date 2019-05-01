'''
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxOpenClient

A wrapper over DxClient class to maintain
coherence in coding across diff. DxOpen clients
such as C#, Java etc.
'''
from itertools import ifilter
import urllib2, urllib
import urllib2, urllib, urlparse
import urllib2, urllib
import cookielib, httplib, uuid, os.path
import constants as const, datetime, dxlxml as DxlObjects
from constants import Parameters as params
from connect import DxlClient

class DxOpenClient(DxlClient):
    m_useJsonPath = False
    #m_parameters = []
    m_query = None

    # def __init__(self, baseUrl):
    #     super(DxOpenClient, self).__init__(self, baseUrl)
    def __init__(self, baseUrl, useJsonPath=False):
        self.m_useJsonPath = useJsonPath
        super(DxOpenClient, self).__init__(baseUrl)

    def buildRequest(self, page, parameters):
        if self.m_query is None:
            print 'empty query in buildRequest method. Check again!!!'
            return None
        result = self.getUrl(page)
        result = result + '?' + self.getParametersFromQuery()
        if const.DEBUG_QUERY_PRINT:
            print 'DEBUGGER > THE URL IS: ' + result
        return result

    def getLocalImage(self, pageName, parameters, localDir):
        return super(DxOpenClient, self).getLocalImage(pageName, parameters, localDir)

    def getData(self, query=None, parameters=None, pageName=const.PAGE_API):
        self.m_query = query
        if not self.m_useJsonPath:
            return super(DxOpenClient, self).getXml(pageName, parameters)
        raise NotImplementedError # For JSON implementation
        #return None #Disabled Path for JSON as of now.

    def getDataConduit(self, query):
        if query is None:
            raise ValueError
        rawData = self.getData(query = query)
        formattedData = DxlObjects.CreateFromDocument(rawData)
        return formattedData

    def getUrl(self, pageName):
        return self.m_baseUrl + const.PAGE_JSON +".aspx" if self.m_useJsonPath else super(DxOpenClient, self).getUrl(pageName)

    # def getXml(self, pageName, parameters):
    #     return super().getXml(self, pageName, parameters)

    def getParametersFromQuery(self):
        query = self.m_query

        def getVersion():
            return (params.PARAM_VERSION + params.VALUE_ASSIGN + urllib.quote(query.getQueryElement(params.PARAM_VERSION)))\
             if query.getQueryElement(params.PARAM_VERSION) is not None else None

        def getSource():
            return (params.PARAM_SOURCE + params.VALUE_ASSIGN + urllib.quote(query.getQueryElement(params.PARAM_SOURCE)))\
             if query.getQueryElement(params.PARAM_SOURCE) is not None else None #raise TypeError

        def getBatch():
            return (params.PARAM_BATCH + params.VALUE_ASSIGN + urllib.quote(query.getQueryElement(params.PARAM_BATCH)))\
             if query.getQueryElement(params.PARAM_BATCH) is not None else None

        def getCurrency():
            return (params.PARAM_CURRENCY + params.VALUE_ASSIGN + urllib.quote(query.getQueryElement(params.PARAM_CURRENCY)))\
             if query.getQueryElement(params.PARAM_CURRENCY) is not None else None

        def getCategories():
            categories = query.getQueryElement(params.PARAM_CATEGORY)
            if not categories:
                return None
            result = params.PARAM_CATEGORY + params.VALUE_ASSIGN
            first = True
            for category in categories:
                if not first:
                    result = result + params.VALUE_SEPARATOR
                result = result + urllib.quote(category)
                first = False
            return result

        def getFields():
            fields = query.getQueryElement(params.PARAM_FIELDS)
            if not fields:
                return None
            result = params.PARAM_FIELDS + params.VALUE_ASSIGN
            first = True
            for field in fields:
                if not first:
                    result = result + params.VALUE_SEPARATOR
                result = result + urllib.quote(field)
                first = False
            return result

        def getFilters():
            filters = query.getQueryElement(params.PARAM_FILTER)
            if not filters:
                return None
            result = params.PARAM_FILTER + params.VALUE_ASSIGN
            first = True
            for filter in filters:
                if not first:
                    result = result + params.VALUE_SEPARATOR
                result = ifilter[0] + ':' + urllib.quote(ifilter[1])
                first = False
            return result

        def getIdentifiers():
            identifiers = query.getQueryElement(params.PARAM_IDENTIFIER)
            if not identifiers:
                return None
            first = True
            result = ''
            for key, valueList in identifiers.items():
                if not first:
                    result = result + params.IDENTIFIER_SEPARATOR
                result = result + params.PARAM_IDTYPE + params.VALUE_ASSIGN + key + params.IDENTIFIER_SEPARATOR\
                 + params.PARAM_IDVALUE + params.VALUE_ASSIGN + parseMultiValueParameter(valueList)
                first = False
            return result

        def getFromDate():
            date = query.getQueryElement(params.PARAM_FROM_DATE)
            if date is const.MIN_DATE:
                return None
            return params.PARAM_FROM_DATE + params.VALUE_ASSIGN +  urllib.quote(date.strftime(const.DEFAULT_DATE_FORMAT))

        def getToDate():
            date = query.getQueryElement(params.PARAM_TO_DATE)
            if date is const.MIN_DATE:
                return None
            return params.PARAM_TO_DATE + params.VALUE_ASSIGN +  urllib.quote(date.strftime(const.DEFAULT_DATE_FORMAT))

        def parseMultiValueParameter(valueList):
            first = True
            result = ''
            for value in valueList:
                if not first:
                    result = result + params.VALUE_SEPARATOR
                result = result + urllib.quote(value)
                first = False
            return result

        assembledQueryElements = ''
        parameterAssembly = [getSource, getFields, getCurrency, getCategories, getFilters, getIdentifiers, getFromDate, getToDate, getVersion, getBatch]

        for parameterMethod in parameterAssembly:
            chunk = parameterMethod()
            if chunk is not None:
                assembledQueryElements = assembledQueryElements + chunk + params.IDENTIFIER_SEPARATOR

        assembledQueryElements = assembledQueryElements[:-1] #to remove last &
        return assembledQueryElements
    #_______________ Data Request Methods | Start _______________

    def doAdminQuery(self, dxl_Admin_Query):
        raise NotImplementedError

    def getAccountPerformance(self, dxl_Account_Performance_Query):
        formattedData = self.getDataConduit(dxl_Account_Performance_Query)
        return formattedData.AccountPerformance

    def getBenchmarkPerformance(self, dxl_Benchmark_Query):
        formattedData = self.getDataConduit(dxl_Benchmark_Query)
        return formattedData.BenchmarkPerformance

    def getChart(self, dxl_Chart_Query):
        raise NotImplementedError

    def getClient(self, dxl_Client_Query):
        formattedData = self.getDataConduit(dxl_Client_Query)
        return formattedData.Client

    def getClientVariance(self, dxl_Client_Variance_Query):
        formattedData = self.getDataConduit(dxl_Client_Variance_Query)
        return formattedData.ClientVariance

    def getDataUpdates(self, dxl_Data_Updates_Query):
        formattedData = self.getDataConduit(dxl_Data_Updates_Query)
        return formattedData.DataUpdates

    def getDIME(self, dxl_DIME_Query):
        formattedData = self.getDataConduit(dxl_DIME_Query)
        return formattedData.DIME

    def getDividend(self, dxl_Dividend_Query):
        formattedData = self.getDataConduit(dxl_Dividend_Query)
        return formattedData.Dividend

    def getIM(self, dxl_IM_Query):
        formattedData = self.getDataConduit(dxl_IM_Query)
        return formattedData.IM

    def getIntraday(self, dxl_Intraday_Query):
        formattedData = self.getDataConduit(dxl_Intraday_Query)
        return formattedData.Intraday

    def getMeta(self, dxl_Meta_Query):
        formattedData = self.getDataConduit(dxl_Meta_Query)
        return formattedData.Meta

    def getPending(self, dxl_Pending_Query):
        formattedData = self.getDataConduit(dxl_Pending_Query)
        return formattedData.Pending

    def getPublic(self, dxl_Public_Query):
        formattedData = self.getDataConduit(dxl_Public_Query)
        return formattedData.Public

    def getRates(self, dxl_Rates_Query):
        formattedData = self.getDataConduit(dxl_Rates_Query)
        return formattedData.Rates

    def getRepo(self, dxl_Repo_Query):
        formattedData = self.getDataConduit(dxl_Repo_Query)
        return formattedData.Repo

    def getScreen(self, dxl_Screen_Query):
        formattedData = self.getDataConduit(dxl_Screen_Query)
        return formattedData.Screen

    def getSearch(self, dxl_Search_Query):
        raise NotImplementedError

    def getSF(self, dxl_SF_Query):
        #return self.getDataConduit(dxl_SF_Query).SF  # This works as well. Disabled as it helps in debugging.
        formattedData = self.getDataConduit(dxl_SF_Query)
        return formattedData.SF

    def getTriPartyTrading(self, dxl_TriParty_Trading_Query):
        formattedData = self.getDataConduit(dxl_TriParty_Trading_Query)
        return formattedData.TriPartyTrading
    #_______________ Data Request Methods | End _______________
