from tkinter import *
import tkinter.ttk as ttk
import pymysql
root = Tk()
tree = ttk.Treeview(root)
conn = pymysql.connect(ip, user, passwd, dbname)
cur = conn.cursor(pymysql.cursors.DictCursor)
tree["columns"] = ("last_seen","version","cpu","pc_name","product_name","arch","RAM", "mac_wlan", "mac_eth", "oem_key")
sql = "SELECT * FROM `inventory`"
cur.execute(sql)
conn.commit()
for row in cur:
       tree.insert("", "end",values=(row["id"],row["last_seen"],row["version"],row["cpu"],row["pc_name"],row["product_name"],row["arch"],row["RAM"], row["mac_wlan"], row["mac_eth"], row["oem_key"]))
tree.pack()
root.mainloop()
