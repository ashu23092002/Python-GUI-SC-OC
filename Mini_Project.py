from tkinter import *
import math

root = Tk()
root.title("Mini Project")

# Schematic Diagram of transformer's equivalent circuit
bg = PhotoImage(file="Circuit.png")
my_label = Label(root, image=bg)
my_label.grid(row=9, column=0, columnspan=4)

label = Label(root, text="INVALID INPUT", font='20', fg="RED")


# Defining function to process the equivalent parameters
def entry():
    label.grid_forget()

    o1.config(state="normal")
    o2.config(state="normal")
    o3.config(state="normal")
    o4.config(state="normal")
    o1.delete(0, END)
    o2.delete(0, END)
    o3.delete(0, END)
    o4.delete(0, END)

    oe1.delete(0, END)
    oe2.delete(0, END)
    oe3.delete(0, END)
    oe4.delete(0, END)

    try:
        v1 = float(eoc1.get())
        i1 = float(eoc2.get())
        w1 = float(eoc3.get())

        k = w1 / (v1 * i1)
        k1 = k * i1
        k2 = math.sqrt((i1 * i1) - (k1 * k1))
        k3 = v1 / k1
        k4 = v1 / k2

        o1.insert(0, str(k3))
        o2.insert(0, str(k4))

        oe1.insert(0, str(k3))
        oe2.insert(0, str(k4))

    except:
        label.grid(row=10, column=0, columnspan=4)

    try:
        v2 = float(esc1.get())
        i2 = float(esc2.get())
        w2 = float(esc3.get())

        k5 = w2 / (i2 * i2)
        k6 = v2 / i2
        k7 = math.sqrt((k6 * k6) - (k5 * k5))

        o3.insert(0, str(k5))
        o4.insert(0, str(k7))

        oe3.insert(0, str(k5))
        oe4.insert(0, str(k7))
    except:
        label.grid(row=10, column=0, columnspan=4)

    o1.config(state="disabled")
    o2.config(state="disabled")
    o3.config(state="disabled")
    o4.config(state="disabled")


# Defining function to clear all the entries
def clear():
    eoc1.delete(0, END)
    eoc2.delete(0, END)
    eoc3.delete(0, END)
    esc1.delete(0, END)
    esc2.delete(0, END)
    esc3.delete(0, END)

    o1.config(state="normal")
    o1.delete(0, END)
    o1.config(state="disabled")

    o2.config(state="normal")
    o2.delete(0, END)
    o2.config(state="disabled")

    o3.config(state="normal")
    o3.delete(0, END)
    o3.config(state="disabled")

    o4.config(state="normal")
    o4.delete(0, END)
    o4.config(state="disabled")

    oe1.delete(0, END)
    oe2.delete(0, END)
    oe3.delete(0, END)
    oe4.delete(0, END)


# Open Circuit Test Input
oc = LabelFrame(root, text="Open Circuit Test")
oc.grid(row=0, column=0, columnspan=2)

oc1 = Label(oc, text="Voltmeter Reading (in V)")
oc1.grid(row=1, column=0, padx=10)
eoc1 = Entry(oc)
eoc1.grid(row=1, column=1, padx=10, pady=5)
oc2 = Label(oc, text="Ammeter Reading (in A)")
oc2.grid(row=2, column=0, padx=10)
eoc2 = Entry(oc)
eoc2.grid(row=2, column=1, padx=10, pady=5)
oc3 = Label(oc, text="Wattmeter Reading (in W)")
oc3.grid(row=3, column=0, padx=10)
eoc3 = Entry(oc)
eoc3.grid(row=3, column=1, padx=10, pady=10)

# Short Circuit Test Input
sc = LabelFrame(root, text="Short Circuit Test")
sc.grid(row=0, column=2, columnspan=2)

sc1 = Label(sc, text="Voltmeter Reading (in V)")
sc1.grid(row=1, column=0, padx=10)
esc1 = Entry(sc)
esc1.grid(row=1, column=1, padx=10, pady=5)
sc2 = Label(sc, text="Ammeter Reading (in A)")
sc2.grid(row=2, column=0, padx=10)
esc2 = Entry(sc)
esc2.grid(row=2, column=1, padx=10, pady=5)
sc3 = Label(sc, text="Wattmeter Reading (in W)")
sc3.grid(row=3, column=0, padx=10)
esc3 = Entry(sc)
esc3.grid(row=3, column=1, padx=10, pady=10)

# Output
ou = LabelFrame(root, text="Equivalent Circuit Parameters")
ou.grid(row=4, column=0, columnspan=4)

l1 = Label(ou, text="Ro (in ohms)")
l1.grid(row=5, column=0)
l2 = Label(ou, text="Xo (in ohms)")
l2.grid(row=5, column=1)
l3 = Label(ou, text="Ro1 (in ohms)")
l3.grid(row=5, column=2)
l4 = Label(ou, text="Xo1 (in ohms)")
l4.grid(row=5, column=3)

o1 = Entry(ou, width=25)
o1.config(state="disabled")
o1.grid(row=6, column=0, pady=3)
o2 = Entry(ou, width=25)
o2.grid(row=6, column=1, pady=3)
o2.config(state="disabled")
o3 = Entry(ou, width=25)
o3.grid(row=6, column=2, pady=3)
o3.config(state="disabled")
o4 = Entry(ou, width=25)
o4.grid(row=6, column=3, pady=3)
o4.config(state="disabled")

# Buttons
bu = LabelFrame(root)
bu.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

bu1 = Button(bu, text="Submit", height=1, width=8, command=entry)
bu1.grid(row=8, column=0)

bu2 = Button(bu, text="Clear", height=1, width=8, command=clear)
bu2.grid(row=8, column=1)

# Shows equivalent circuit parameters in circuit diagram
oe1 = Entry(root, bg="#DEDEDE", width=18)
oe1.place(x=40, y=435, anchor="w")
oe2 = Entry(root, bg="#DEDEDE", width=18)
oe2.place(x=245, y=435, anchor="w")
oe3 = Entry(root, bg="#DEDEDE", width=18)
oe3.place(x=165, y=270, anchor="w")
oe4 = Entry(root, bg="#DEDEDE", width=18)
oe4.place(x=425, y=270, anchor="w")

root.mainloop()
