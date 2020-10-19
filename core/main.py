#-*- coding:utf-8 -*-
"""
@author: Lucy
@file: main.py
@time: 2019/03/01
"""
from core.market import MarketInfo
from core.index import IndexInfo
from core.pe_ttm import PEInfo
from core.stock import StockInfo
from common.constant import const
from datetime import datetime
import os
import logging

mi = MarketInfo()
index_info = IndexInfo(mi)
stock_info = StockInfo(mi)
pe_ttm = PEInfo(mi)