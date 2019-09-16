# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 字典推导.py
@time: 2019/09/02 21:33:11
"""

DIAL_CODES = [
 (86, 'China'),
 (91, 'India'),
 (1, 'United States'),
 (62, 'Indonesia'),
 (55, 'Brazil'),
 (92, 'Pakistan'),
 (880, 'Bangladesh'),
 (234, 'Nigeria'),
 (7, 'Russia'),
 (81, 'Japan'),
 ]
country_code = {country: code for code, country in DIAL_CODES}

code_country = {code: country.upper() for country, code in country_code.items() if code < 66}

print(country_code)
print(code_country)
