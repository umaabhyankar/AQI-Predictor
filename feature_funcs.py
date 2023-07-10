# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:04:23 2023

@author: umaab
"""

def pm10_sub_index(pm_10):
    if pm_10 <= 100:
        pm10_si = pm_10
    elif (pm_10 > 100 and pm_10 <= 250):
        pm10_si = 100+(pm_10-100)*(100/150)
    elif (pm_10 > 250 and pm_10 <= 350):
        pm10_si = 200+(pm_10-250)
    elif (pm_10 > 350 and pm_10 <= 430):
        pm10_si = 300+(pm_10-350)*(100/80)
    elif pm_10 > 430:
        pm10_si = 400+(pm_10-430)*(100/80)
    return pm10_si

def pm25_sub_index(pm_25):
    if pm_25 <= 30:
        pm25_si = pm_25*(50/30)
    elif (pm_25 > 30 and pm_25 <= 60):
        pm25_si = 50+(pm_25-30)*(50/30)
    elif (pm_25 > 60 and pm_25 <= 90):
        pm25_si = 100+(pm_25-60)*(100/30)
    elif (pm_25 > 90 and pm_25 <= 120):
        pm25_si = 200+(pm_25-90)*(100/30)
    elif (pm_25 > 120 and pm_25 <= 250):
        pm25_si = 300+(pm_25-120)*(100/130)
    elif pm_25 > 250:
        pm25_si = 400+(pm_25-250)*(100/130)
    return pm25_si

def so2_sub_index(so2):
    if so2 <= 40:
        so2_si = so2*50/40
    elif (so2 > 40 and so2 <= 80):
        so2_si = 50+(so2-40)*50/40
    elif (so2 > 80 and so2 <= 380):
        so2_si = 100+(so2-80)*100/300
    elif (so2 > 380 and so2 <= 800):
        so2_si = 200+(so2-380)*(100/420)
    elif (so2 > 800 and so2 <= 1600):
        so2_si = 300+(so2-800)*(100/800)
    elif so2 > 1600:
        so2_si = 400+(so2-1600)*(100/800)
    return so2_si

def no2_sub_index(no2):
    if no2 <= 40:
        no2_si = no2*50/40
    elif (no2 > 40 and no2 <= 80):
        no2_si = 50+(no2-40)*50/40
    elif (no2 > 80 and no2 <= 180):
        no2_si = 100+(no2-80)*100/100
    elif (no2 > 180 and no2 <= 280):
        no2_si = 200+(no2-180)*(100/100)
    elif (no2 > 280 and no2 <= 400):
        no2_si = 300+(no2-280)*(100/120)
    elif no2 > 400:
        no2_si = 400+(no2-400)*(100/120)
    return no2_si

def co_sub_index(co):
    if co <= 1:
        co_si = co*50/1
    elif (co > 1 and co <= 2):
        co_si = 50+(co-1)*50/1
    elif (co > 2 and co <= 10):
        co_si = 100+(co-2)*100/8
    elif (co > 10 and co <= 17):
        co_si = 200+(co-10)*(100/7)
    elif (co > 17 and co <= 34):
        co_si = 300+(co-17)*(100/17)
    elif co > 34:
        co_si = 400+(co-34)*(100/17)
    return co_si

def o3_sub_index(o3):
    if o3 <= 50:
        o3_si = o3*50/50
    elif (o3 > 50 and o3 <= 100):
        o3_si = 50+(o3-50)*50/50
    elif (o3 > 100 and o3 <= 168):
        o3_si = 100+(o3-100)*100/68
    elif (o3 > 168 and o3 <= 208):
        o3_si = 200+(o3-168)*(100/40)
    elif (o3 > 208 and o3 <= 748):
        o3_si = 300+(o3-208)*(100/539)
    elif o3 > 748:
        o3_si = 400+(o3-400)*(100/539)
    return o3_si