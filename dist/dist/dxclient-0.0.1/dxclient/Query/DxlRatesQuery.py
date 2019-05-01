"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlRatesQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlRatesQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlRatesQuery(DxlDataQuery):
    def __init__(self):
        super(DxlRatesQuery, self).__init__()
        self.setSource('Rates')