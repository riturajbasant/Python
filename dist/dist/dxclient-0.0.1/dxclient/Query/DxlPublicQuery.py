"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlPublicQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlPublicQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlPublicQuery(DxlDataQuery):
    def __init__(self):
        super(DxlPublicQuery, self).__init__()
        self.setSource('Public')