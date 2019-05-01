"""
Date    : 22 August 2018
Author  : Sushant Aggarwal

DxlSFQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlSFQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlSFQuery(DxlDataQuery):
    def __init__(self):
        super(DxlSFQuery, self).__init__()
        self.setSource('SF')
