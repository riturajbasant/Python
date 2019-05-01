"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlClientQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlClientQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlClientQuery(DxlDataQuery):
    def __init__(self):
        super(DxlClientQuery, self).__init__()
        self.setSource('Client')