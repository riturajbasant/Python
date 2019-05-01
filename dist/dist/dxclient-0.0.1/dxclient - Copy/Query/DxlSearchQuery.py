"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlSearchQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlSearchQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlSearchQuery(DxlDataQuery):
    def __init__(self):
        super(DxlSearchQuery, self).__init__()
        self.setSource('Search')