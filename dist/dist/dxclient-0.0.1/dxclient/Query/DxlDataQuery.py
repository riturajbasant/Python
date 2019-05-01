"""
Date    : 22 August 2018
Author  : Sushant Aggarwal

DxlDataQuery
First level child of DxlBaseQuery
"""

from dxclient.Query.DxlBaseQuery import DxlBaseQuery

class DxlDataQuery(DxlBaseQuery):
    def __init__(self):
        super(DxlDataQuery, self).__init__()
