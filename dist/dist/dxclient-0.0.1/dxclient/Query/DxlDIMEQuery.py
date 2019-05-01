"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlDIMEQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlDIMEQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlDIMEQuery(DxlDataQuery):
    def __init__(self):
        super(DxlDIMEQuery, self).__init__()
        self.setSource('DIME')
