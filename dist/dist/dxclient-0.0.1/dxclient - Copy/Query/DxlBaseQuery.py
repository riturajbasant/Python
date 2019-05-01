"""
Date    : 22 August 2018
Author  : Sushant Aggarwal

DxlBaseQuery
Base class for query objects.
"""

from datetime import datetime
#from . import constants as const
#from constants import Parameters as params
import dxclient.constants as const
from const import Parameters as params


class DxlBaseQuery(object):

    def __init__(self, version=None):
        '''
        If you are changing/adding in new members
        make sure you adjust the getQueryElement()
        and probably relevant constants
        '''
        self.__m_batch       = None
        self.__m_categories  = []
        self.__m_currency    = 'GBP'
        self.__m_dateFormat  = const.DEFAULT_DATE_FORMAT  #'%d-%m-%Y'
        self.__m_days        = None
        self.__m_fields      = []
        self.__m_filters     = []
        self.__m_fromDate    = const.MIN_DATE
        self.__m_identifiers = {}  # Making it a dictionary of lists
        self.__m_modifiers   = None
        self._m_source       = None
        self.__m_toDate      = const.MIN_DATE
        self.__m_version     = '2.0' if version is None else version
        if not version is None:
            self.version = version

    def addCategory(self, category):
        if category not in self.__m_categories:
            self.__m_categories.append(category)

    def addCategories(self, categories):
        for category in categories:
            if category not in self.__m_categories:
                self.__m_categories.append(category)

    def addField(self, field):
        if field not in self.__m_fields:
            self.__m_fields.append(field)

    def addFields(self, fields):
        for field in fields:
            if field not in self.__m_fields:
                self.__m_fields.append(field)

    def addFilter(self, name, value):
        if [name, value] not in self.__m_filters:
            self.__m_filters.append([name, value])

    def addIdentifier(self, type, value):
        identifierList = self.__m_identifiers[type] if type in self.__m_identifiers else []
        if value not in identifierList:
            identifierList.append(value)
        self.__m_identifiers[type] = identifierList

    def clearIdentifiers(self):
        self.__m_identifiers = {}

    def clearFields(self):
        self.__m_fields = []

    def clearFilters(self):
        self.__m_filters = []

    def getQueryElement(self, type):
        queryElements = {
            params.PARAM_BATCH      : self.__m_batch,
            params.PARAM_CATEGORY   : self.__m_categories,
            params.PARAM_CURRENCY   : self.__m_currency,
            params.PARAM_DAYS       : self.__m_days,
            params.PARAM_FIELDS     : self.__m_fields,
            params.PARAM_FILTER     : self.__m_filters,
            params.PARAM_FROM_DATE  : self.__m_fromDate,
            params.PARAM_IDENTIFIER : self.__m_identifiers,
            params.PARAM_MODIFIER   : self.__m_modifiers,
            params.PARAM_SOURCE     : self._m_source,
            params.PARAM_TO_DATE    : self.__m_toDate,
            params.PARAM_VERSION    : self.__m_version
        }

        if type not in queryElements:
            raise TypeError

        return queryElements[type]

    def resetQuery(self):
        self.__m_batch       = None
        self.__m_categories  = []
        self.__m_currency    = 'GBP'
        self.__m_dateFormat  = const.DEFAULT_DATE_FORMAT
        self.__m_days        = None
        self.__m_fields      = []
        self.__m_filters     = []
        self.__m_fromDate    = const.MIN_DATE
        self.__m_identifiers = {}
        self.__m_modifiers   = None
        self._m_source       = None
        self.__m_toDate      = const.MIN_DATE
        self.__m_version     = '2.0'

    def setDays(self, no_Of_Days):
        self.__m_days = no_Of_Days

    def setFromDate(self, dateString):
        self.__m_fromDate = datetime.strptime(dateString, self.__m_dateFormat).date()

    # Just a non-sensical concept of setting and using Protected variable

    def setSource(self, source):
        self._m_source = source

    def setToDate(self, dateString):
        self.__m_toDate = datetime.strptime(dateString, self.__m_dateFormat).date()