"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlIMQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlIMQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlIMQuery(DxlDataQuery):
    def __init__(self):
        super(DxlIMQuery, self).__init__()
        self.setSource('IM')