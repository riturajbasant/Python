"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlAccountPerformanceQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlAccountPerformanceQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlAccountPerformanceQuery(DxlDataQuery):
    def __init__(self):
        super(DxlAccountPerformanceQuery, self).__init__()
        self.setSource('AccountPerformance')