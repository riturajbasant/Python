"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlPendingQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlPendingQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlPendingQuery(DxlDataQuery):
    def __init__(self):
        super(DxlPendingQuery, self).__init__()
        self.setSource('Pending')