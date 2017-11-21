from tkinter import *
import tkinter.ttk as ttk
import pymysql

root = Tk()


tree = ttk.Treeview(root)

conn = pymysql.connect(host=ip, user=user, passwd=passwd, db=database)
cur = conn.cursor(pymysql.cursors.DictCursor)

tree["columns"] = ("last_seen","version","cpu","pc_name","product_name","arch","RAM", "mac_wlan", "mac_eth", "oem_key")



text =1047
text2= ""
text3=""

for i in range(1, 6):
    sql = "SELECT * FROM `inventory`"
    cur.execute(sql)
    conn.commit()
    print(text)


    for row in cur:
       
       tree.insert("", "end",values=(row["id"],row["last_seen"],row["version"],row["cpu"],row["pc_name"],row["product_name"],row["arch"],row["RAM"], row["mac_wlan"], row["mac_eth"], row["oem_key"]))
       print(row)

tree.pack()
root.mainloop()
