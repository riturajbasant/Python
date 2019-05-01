"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlIntradayQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlIntradayQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlIntradayQuery(DxlDataQuery):
    def __init__(self):
        super(DxlIntradayQuery, self).__init__()
        self.setSource('Intraday')