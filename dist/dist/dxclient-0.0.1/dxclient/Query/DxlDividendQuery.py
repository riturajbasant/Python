"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlDividendQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlDividendQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlDividendQuery(DxlDataQuery):
    def __init__(self):
        super(DxlDividendQuery, self).__init__()
        self.setSource('Dividend')
