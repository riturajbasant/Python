"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlTriPartyTradingQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlTriPartyTradingQuery
"""

from Query.DxlDataQuery import DxlDataQuery

class DxlTriPartyTradingQuery(DxlDataQuery):
    def __init__(self):
        super(DxlTriPartyTradingQuery, self).__init__()
        self.setSource('TriPartyTrading')