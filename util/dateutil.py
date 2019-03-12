# -*- coding:utf-8 -*-
"""
@author: Lucy
@file: dateutil.py
@time: 2019/03/03
"""

import calendar
import pandas as pd
from common.constant import const
from datetime import datetime, timedelta, date


class dateutil:

    DATE_FORMAT_TUSHARE = '%Y%m%d'
    DATE_FORMAT_DB = '%Y-%m-%d'

    @classmethod
    def get_first_day_of_next_month(cls, my_date):
        """
        获取下个月的第一天
        :param date: datetime
        """
        if isinstance(my_date, (datetime, date)):
            first_day = datetime(my_date.year, my_date.month, 1)
            days_num = calendar.monthrange(first_day.year, first_day.month)[1]
            first_day_of_next_month = first_day + timedelta(days=days_num)
            return first_day_of_next_month
        raise Exception("Unexpected data type: %s", type(my_date))

    @classmethod
    def get_next_day(cls, date):
        """
        获取下一天
        :param date: datetime / str
        """
        if isinstance(date, datetime):
            next_day = date + timedelta(days=1)
            return next_day
        if isinstance(date, str):
            date_tmp = cls.yyyymmdd_to_datetime(date)
            next_day = date_tmp + timedelta(days=1)
            return cls.datetime_to_yyyymmdd(next_day)
        raise Exception("Unexpected data type")

    @classmethod
    def datetime_to_yyyymmdd(cls, date):
        """
        date转yyyymmdd str
        :param date: datetime
        """
        if isinstance(date, datetime):
            return date.strftime(cls.DATE_FORMAT_TUSHARE)
        raise Exception("Unexpected data type")

    @classmethod
    def datetime_to_yyyy_mm_dd(cls, date):
        """
        date转yyyy-mm-dd str
        :param date: datetime
        """
        if isinstance(date, datetime):
            return date.strftime(const.DATE_FORMAT_ONE)
        raise Exception("Unexpected data type")

    @classmethod
    def yyyymmdd_to_datetime(cls, yyyymmdd):
        """
        yyyymmdd str转datetime
        :param yyyymmdd str
        """
        if isinstance(yyyymmdd, str):
            return datetime.strptime(yyyymmdd, const.DATE_FORMAT_TUSHARE)
        raise Exception("Unexpected data type")

    @classmethod
    def yyyy_mm_dd_to_datetime(cls, yyyy_mm_dd):
        """
            yyyy_mm_dd str转datetime
            :param yyyy_mm_dd: str
            """
        if yyyy_mm_dd:
            return None
        if isinstance(yyyy_mm_dd, str):
            return datetime.strptime(yyyy_mm_dd, const.DATE_FORMAT_ONE)
        raise Exception("Unexpected data type")

    @classmethod
    def tushare_date_to_datetime(cls, col):
        pd.to_datetime(col, format=const.DATE_FORMAT_TUSHARE, errors='coerce')