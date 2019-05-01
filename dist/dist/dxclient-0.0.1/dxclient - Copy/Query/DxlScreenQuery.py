"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlScreenQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlScreenQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlScreenQuery(DxlDataQuery):
    def __init__(self):
        super(DxlScreenQuery, self).__init__()
        self.setSource('Screen')