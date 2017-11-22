from tkinter import *
import tkinter.ttk as ttk
import pymysql
root = Tk()
tree = ttk.Treeview(root)
conn = pymysql.connect(ip, user, passwd, dbname)
cur = conn.cursor(pymysql.cursors.DictCursor)
ysb = ttk.Scrollbar(orient='vertical', command=tree.yview)
xsb = ttk.Scrollbar(orient='horizontal', command=tree.xview)
ysb.place(x=822, y=240, height=440)
xsb.place(x=10, y=678, width=813)
tree["columns"] = ("id","last_seen","version","cpu","pc_name","product_name","arch","RAM", "mac_wlan", "mac_eth", "oem_key")
tree.heading("#0", text='ID', anchor='w')
tree.heading("#1", text="last seen")
tree.heading("#2", text="version")
tree.heading("#3", text="cpu")
tree.heading("#4", text="pc_name")
tree.heading("#5", text="product_name")
tree.heading("#6", text="arch")
tree.heading("#7", text="RAM")
tree.heading("#8", text="mac_Wlan")
tree.heading("#9", text="mac_eth")
tree.heading("#10", text="oem_key")
tree.configure(yscroll=ysb.set, xscroll=xsb.set)

sql = "SELECT * FROM `inventory`"
cur.execute(sql)
conn.commit()
for row in cur:
       tree.insert("", "end",text=row["id"],values=(row["last_seen"],row["version"],row["cpu"],row["pc_name"],row["product_name"],row["arch"],row["RAM"], row["mac_wlan"], row["mac_eth"], row["oem_key"]))
tree.pack()
root.mainloop()
