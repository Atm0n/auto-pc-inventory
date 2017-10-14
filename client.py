#!/usr/bin/env python3
def update(data):
    import pymysql # the used module

    conn = pymysql.connect(host='ip or domain', user='user!!!', passwd='passwd', db='Data base!!!') # change this
    cur = conn.cursor()
    sql = "INSERT INTO inventory(last_seen,version,cpu,pc_name,arch,RAM, mac_wlan, mac_eth) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" #sql 
    cur.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])) # where the data is...
    conn.commit() # commit changes
    conn.close() # close connection

