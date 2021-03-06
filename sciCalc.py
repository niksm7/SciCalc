from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np
window = Tk()
window.geometry('800x420')

#<====GLOBAL VARIABLES====>

is_binary = 0
counter = 0

#<====Functions====>

def number(num):
    entry.config(state="normal")
    entry.insert("end",num)
    entry.config(state="readonly")

def operation(opr):
    global is_binary,counter
    if opr=="add":
        entry.config(state="normal")
        entry.insert("end","+")
        entry.config(state="readonly")

    if opr=="sub":
        entry.config(state="normal")
        entry.insert("end","-")
        entry.config(state="readonly")

    if opr == "mul":
        entry.config(state="normal")
        entry.insert("end", "*")
        entry.config(state="readonly")

    if opr == "div":
        entry.config(state="normal")
        entry.insert("end", "/")
        entry.config(state="readonly")

    if opr == "intdiv":
        entry.config(state="normal")
        entry.insert("end", "//")
        entry.config(state="readonly")

    if opr == "power":
        entry.config(state="normal")
        entry.insert("end", "**")
        entry.config(state="readonly")

    if opr == "leftbrack":
        entry.config(state="normal")
        entry.insert("end", "(")
        entry.config(state="readonly")

    if opr == "rightbrack":
        entry.config(state="normal")
        entry.insert("end", ")")
        entry.config(state="readonly")

    if opr == "sqrtf":
        entry.config(state="normal")
        entry.insert("end", "sqrt(")
        entry.config(state="readonly")

    if opr=="pif":
        entry.config(state="normal")
        entry.insert("end", "π")
        entry.config(state="readonly")

    if opr=="factf":
        entry.config(state="normal")
        entry.insert("end", "factorial(")
        entry.config(state="readonly")

    if opr=="dotf":
        entry.config(state="normal")
        entry.insert("end", ".")
        entry.config(state="readonly")

    if opr=="jf":
        entry.config(state="normal")
        entry.insert("end", "j")
        entry.config(state="readonly")

    try:
        if opr=="equals":
            if is_binary==1:
                entry.config(state="normal")
                x = eval(entry.get())
                entry.delete(0, "end")
                entry.insert(0, x.replace("0b",""))
                entry.config(state="readonly")
                is_binary=0
            else:
                entry.config(state="normal")
                g = entry.get().replace("π","pi")
                if counter==0:
                    q = eval(g.replace("cosec(","1/sin(").replace("sec(","1/cos(").replace("cot(","1/tan(").replace("ln(","np.log("))
                else:
                    q = eval(g.replace("acosec(","1/asin(").replace("asec(","1/acos(").replace("acot(","1/atan(").replace("ln(","np.log("))
                entry.delete(0,"end")
                if len(list(map(str,str(q))))<30:
                    entry.insert(0,q)
                else:
                    entry.insert(0,'ERROR')
                entry.config(state="readonly")

    except Exception:
        messagebox.showwarning("WARNING", "PLEASE ENTER VALID INPUTS")
        entry.config(state="readonly")

    if opr=="clear":
        entry.config(state="normal")
        entry.delete(0,"end")
        entry.config(state="readonly")

    if opr=="backspace":
        entry.config(state="normal")
        entry.delete(len(entry.get())-1,"end")
        entry.config(state="readonly")

    if opr=="poweroff":
        exit()

def trigoperations(opr):
    global counter
    if counter==0:
        if opr == "sinf":
            entry.config(state="normal")
            entry.insert("end", "sin(")
            entry.config(state="readonly")

        if opr=="cosf":
            entry.config(state="normal")
            entry.insert("end", "cos(")
            entry.config(state="readonly")

        if opr=="tanf":
            entry.config(state="normal")
            entry.insert("end", "tan(")
            entry.config(state="readonly")

        if opr=="cosecf":
            entry.config(state="normal")
            entry.insert("end", "cosec(")
            entry.config(state="readonly")

        if opr=="secf":
            entry.config(state="normal")
            entry.insert("end", "sec(")
            entry.config(state="readonly")

        if opr=="cotf":
            entry.config(state="normal")
            entry.insert("end", "cot(")
            entry.config(state="readonly")

        if opr=="logf":
            entry.config(state="normal")
            entry.insert("end", "log10(")
            entry.config(state="readonly")

        if opr=="lnf":
            entry.config(state="normal")
            entry.insert("end", "ln(")
            entry.config(state="readonly")

    else:
        if opr == "sinf":
            entry.config(state="normal")
            entry.insert("end", "degrees(asin(")
            entry.config(state="readonly")

        if opr == "cosf":
            entry.config(state="normal")
            entry.insert("end", "degrees(acos(")
            entry.config(state="readonly")

        if opr == "tanf":
            entry.config(state="normal")
            entry.insert("end", "atan(")
            entry.config(state="readonly")

        if opr == "cosecf":
            entry.config(state="normal")
            entry.insert("end", "acosec(")
            entry.config(state="readonly")

        if opr == "secf":
            entry.config(state="normal")
            entry.insert("end", "asec")
            entry.config(state="readonly")

        if opr == "cotf":
            entry.config(state="normal")
            entry.insert("end", "acot")
            entry.config(state="readonly")

        if opr == "logf":
            entry.config(state="normal")
            entry.insert("end", "log10(")
            entry.config(state="readonly")

        if opr == "lnf":
            entry.config(state="normal")
            entry.insert("end", "ln(")
            entry.config(state="readonly")

def binoperations(opr):
    global is_binary
    if opr=="binf":
        entry.config(state="normal")
        entry.insert("end", "bin(")
        entry.config(state="readonly")
        is_binary=1

    if opr=="hexf":
        entry.config(state="normal")
        entry.insert("end", "hex(")
        entry.config(state="readonly")
        is_binary=1


    if opr=="octf":
        entry.config(state="normal")
        entry.insert("end", "oct(")
        entry.config(state="readonly")
        is_binary=1

def bitwiseoperations(opr):
    if opr=="andf":
        entry.config(state="normal")
        entry.insert("end", "&")
        entry.config(state="readonly")

    if opr=="orf":
        entry.config(state="normal")
        entry.insert("end", "|")
        entry.config(state="readonly")

    if opr=="exorf":
        entry.config(state="normal")
        entry.insert("end", "^")
        entry.config(state="readonly")

def inverse():
    global counter
    if counter==0:
        inv_button.config(highlightbackground='#c5dfe8')
        sin_button.config(text="sin-1")
        cos_button.config(text="cos-1")
        tan_button.config(text="tan-1")
        cosec_button.config(text="cosec-1")
        sec_button.config(text="sec-1")
        cot_button.config(text="cot-1")
        counter+=1
    else:
        inv_button.config(highlightbackground='white')
        sin_button.config(text="sin")
        cos_button.config(text="cos")
        tan_button.config(text="tan")
        cosec_button.config(text="cosec")
        sec_button.config(text="sec")
        cot_button.config(text="cot")
        counter -= 1

#<=============CREATING AND PLACING OBJECTS=============>

large_font = ('Verdana',27)
entry = Entry(window,width=50,font=large_font)
entry.pack()
entry.config(state="readonly")


#<====PANEL ONE====>

one_button = Button(window,text="1",command=lambda:number(1))
one_button.place(x=10,y=100,width=50,height=50)

two_button = Button(window,text="2",command=lambda:number(2))
two_button.place(x=70,y=100,width=50,height=50)

three_button = Button(window,text="3",command=lambda:number(3))
three_button.place(x=130,y=100,width=50,height=50)

four_button = Button(window,text="4",command=lambda:number(4))
four_button.place(x=10,y=160,width=50,height=50)

five_button = Button(window,text="5",command=lambda:number(5))
five_button.place(x=70,y=160,width=50,height=50)

six_button = Button(window,text="6",command=lambda:number(6))
six_button.place(x=130,y=160,width=50,height=50)

seven_button = Button(window,text="7",command=lambda:number(7))
seven_button.place(x=10,y=220,width=50,height=50)

eight_button = Button(window,text="8",command=lambda:number(8))
eight_button.place(x=70,y=220,width=50,height=50)

nine_button = Button(window,text="9",command=lambda:number(9))
nine_button.place(x=130,y=220,width=50,height=50)

zero_button = Button(window,text="0",command=lambda:number(0))
zero_button.place(x=70,y=280,width=50,height=50)

bracket_left_button = Button(window,text="(",command=lambda:operation("leftbrack"))
bracket_left_button.place(x=10,y=280,width=50,height=50)

bracket_right_button = Button(window,text=")",command=lambda:operation("rightbrack"))
bracket_right_button.place(x=130,y=280,width=50,height=50)


#<====PANEL TWO====>

add_button = Button(window,text="+",command=lambda:operation("add"))
add_button.place(x=200,y=160,width=50,height=50)

sub_button = Button(window,text="-",command=lambda:operation("sub"))
sub_button.place(x=260,y=160,width=50,height=50)

mul_button = Button(window,text="X",command=lambda:operation("mul"))
mul_button.place(x=320,y=160,width=50,height=50)

div_button = Button(window,text="/",command=lambda:operation("div"))
div_button.place(x=200,y=220,width=50,height=50)

intdiv_button = Button(window,text="//",command=lambda:operation("intdiv"))
intdiv_button.place(x=260,y=220,width=50,height=50)

power_button = Button(window,text="**",command=lambda:operation("power"))
power_button.place(x=320,y=220,width=50,height=50)

backspace_button = Button(window,text="<==",command=lambda:operation("backspace"))
backspace_button.place(x=320,y=100,width=50,height=50)

clear_button = Button(window,text="C",command=lambda:operation("clear"))
clear_button.place(x=260,y=100,width=50,height=50)

poweroff_button = Button(window,text="AC",command=lambda:operation("poweroff"))
poweroff_button.place(x=200,y=100,width=50,height=50)

equal_button = Button(window,text="=",command=lambda:operation("equals"))
equal_button.place(x=260,y=280,width=50,height=50)

fact_button = Button(window,text="!",command=lambda:operation("factf"))
fact_button.place(x=320,y=280,width=50,height=50)

sqrt_button = Button(window,text="√",command=lambda:operation("sqrtf"))
sqrt_button.place(x=200,y=280,width=50,height=50)


#<====PANEL THREE====>

        #<====TO INVERSE THE TRIGO FUNCTIONS====>

inv_button = Button(window,text="INV",command=inverse)
inv_button.place(x=380,y=100,width=50,height=50)

        #<==TRIGNOMETRIC operations==>

sin_button = Button(window,text="sin",command=lambda:trigoperations("sinf"))
sin_button.place(x=380,y=160,width=50,height=50)

cos_button = Button(window,text="cos",command=lambda:trigoperations("cosf"))
cos_button.place(x=440,y=160,width=50,height=50)

tan_button = Button(window,text="tan",command=lambda:trigoperations("tanf"))
tan_button.place(x=500,y=160,width=50,height=50)

cosec_button = Button(window,text="cosec",command=lambda:trigoperations("cosecf"))
cosec_button.place(x=380,y=220,width=50,height=50)

sec_button = Button(window,text="sec",command=lambda:trigoperations("secf"))
sec_button.place(x=440,y=220,width=50,height=50)

cot_button = Button(window,text="cot",command=lambda:trigoperations("cotf"))
cot_button.place(x=500,y=220,width=50,height=50)

log_button = Button(window,text="log",command=lambda:trigoperations("logf"))
log_button.place(x=380,y=280,width=50,height=50)

pi_button = Button(window,text="π",command=lambda:operation("pif"))
pi_button.place(x=440,y=280,width=50,height=50)

ln_button = Button(window,text="ln",command=lambda:trigoperations("lnf"))
ln_button.place(x=500,y=280,width=50,height=50)

#<====PANEL FOUR====>

        #<==BINARY operations==>

binary_button = Button(window,text="bin",command=lambda:binoperations("binf"))
binary_button.place(x=560,y=160,width=50,height=50)

hexa_button = Button(window,text="hex",command=lambda:binoperations("hexf"))
hexa_button.place(x=620,y=160,width=50,height=50)

octa_button = Button(window,text="oct",command=lambda:binoperations("octf"))
octa_button.place(x=680,y=160,width=50,height=50)

        #<==bitwise operations==>

and_button = Button(window,text="&",command=lambda:bitwiseoperations("andf"))
and_button.place(x=560,y=220,width=50,height=50)

or_button = Button(window,text="|",command=lambda:bitwiseoperations("orf"))
or_button.place(x=620,y=220,width=50,height=50)

exor_button = Button(window,text="^",command=lambda:bitwiseoperations("exorf"))
exor_button.place(x=680,y=220,width=50,height=50)

dot_button = Button(window,text=".",command=lambda:operation("dotf"))
dot_button.place(x=560,y=280,width=50,height=50)

j_button = Button(window,text="j",command=lambda:operation("jf"))
j_button.place(x=620,y=280,width=50,height=50)


window.mainloop()
