#!/usr/bin/env python3
def update(data):
    import pymysql

    conn = pymysql.connect(host='192.168.56.102', user='user', passwd='passwd', db='db')
    cur = conn.cursor()
    sql = "DELETE FROM `inventory` WHERE `mac_wlan` = %s" # if there's an equal mac address stored, it deletes all the row
    cur.execute(sql, (data[6])) # this executes the sql script
    conn.commit()   # makes the changes true
    sql = "DELETE FROM `inventory` WHERE `mac_eth` = %s" # if there's an equal mac address stored, it deletes all the row
    cur.execute(sql, (data[7])) # this executes the sql script
    conn.commit() # makes the changes true
    sql = "INSERT INTO inventory(last_seen,version,cpu,pc_name,arch,RAM, mac_wlan, mac_eth) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    conn.commit() # makes the changes true
    conn.close() # This closes the connection
