from tkinter import *
import tkinter.ttk as ttk
import pymysql
root = Tk()
tree = ttk.Treeview(root)
conn = pymysql.connect("192.168.56.101", "clients", "inventory", "inventory")
e1 = Entry(root)
e1.place
ysb = ttk.Scrollbar(orient='vertical', command=tree.yview)

xsb = ttk.Scrollbar(orient='horizontal', command=tree.xview)
cur = conn.cursor(pymysql.cursors.DictCursor)
tree.place(x=822, y=240)
ysb.place(x=822, y=240, height=440)
xsb.place(x=10, y=678, width=813)

tree["columns"] = ("id","last_seen","version","cpu","pc_name","product_name","arch","RAM", "mac_wlan", "mac_eth", "oem_key")
tree.heading("#0", text='ID')
tree.column("#0",minwidth=0,width=50)
tree.heading("#1", text="last seen")
tree.column("#1",minwidth=0,width=140)
tree.heading("#2", text="version")
tree.column("#2",minwidth=0,width=100)
tree.heading("#3", text="cpu")
tree.column("#3",minwidth=0,width=50)
tree.heading("#4", text="pc_name")
tree.column("#4",minwidth=0,width=50)
tree.heading("#5", text="product_name")
tree.column("#5",minwidth=0,width=50)
tree.heading("#6", text="arch")
tree.column("#6",minwidth=0,width=50)
tree.heading("#7", text="RAM")
tree.column("#7",minwidth=0,width=50)
tree.heading("#8", text="mac_Wlan")
tree.column("#8",minwidth=0,width=135)
tree.heading("#9", text="mac_eth")
tree.column("#9",minwidth=0,width=135)
tree.heading("#10", text="oem_key")
tree.column("#10",minwidth=0,width=50)
tree.configure(yscroll=ysb.set, xscroll=xsb.set)
tree.grid()
ysb.grid(row=0, column=1, sticky='ns')
xsb.grid(row=1, column=0, sticky='ew')
root.grid()
sql = "SELECT * FROM `inventory`"
cur.execute(sql)
conn.commit()

cmd1=""


def update_tree():
    cmd1 = mEntry.get()
    print("caca")
    sql = "SELECT * FROM `inventory` where mac_wlan =%s"
    cur.execute(sql,cmd1)
    conn.commit()
    if cmd1 == "":
        print("caca2")
        cmd1= "*"
        cur.execute(sql,cmd1)
        conn.commit()



def on_tree_select(event):
    curItem = tree.focus()
    print(tree.item(curItem))

tree.bind('<ButtonRelease-1>', on_tree_select)
for row in cur:
       tree.insert("", "end",text=row["id"],values=(row["last_seen"],row["version"],row["cpu"],row["pc_name"],row["product_name"],row["arch"],row["RAM"], row["mac_wlan"], row["mac_eth"], row["oem_key"]))

root.mainloop()
