"""
Date    : 23 August 2018
Author  : Sushant Aggarwal

DxlRepoQuery
Second level child of DxlBaseQuery
DxlBaseQuery > DxlDataQuery > DxlRepoQuery
"""

from dxclient.Query.DxlDataQuery import DxlDataQuery

class DxlRepoQuery(DxlDataQuery):
    def __init__(self):
        super(DxlRepoQuery, self).__init__()
        self.setSource('Repo')