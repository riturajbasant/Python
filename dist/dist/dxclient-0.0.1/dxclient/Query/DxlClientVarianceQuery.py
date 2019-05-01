"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlClientVarianceQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlClientVarianceQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlClientVarianceQuery(DxlDataQuery):
    def __init__(self):
        super(DxlClientVarianceQuery, self).__init__()
        self.setSource('ClientVariance')