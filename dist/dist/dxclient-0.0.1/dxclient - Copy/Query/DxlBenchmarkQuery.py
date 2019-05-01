"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlBenchmarkQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlBenchmarkQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlBenchmarkQuery(DxlDataQuery):
    def __init__(self):
        super(DxlBenchmarkQuery, self).__init__()
        self.setSource('BenchmarkPerformance')