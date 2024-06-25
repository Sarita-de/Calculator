from tkinter import *


def get_digit(digit):
    CURRENT = result_label["text"]
    new = CURRENT+ str(digit)
    result_label.config(text= new)


def clear():
    result_label.config(text=" ")


def operator_get(op):
    global first_position,operator,second_position

    first_position = int(result_label["text"])
    operator = op
    result_label.config(text=" ")
    


def final_result():
    global first_position,operator,second_position

    second_position= int(result_label["text"])



    if operator == "+":
        result_label.config(text=str(first_position + second_position))
    elif operator == "-":
        result_label.config(text=str(first_position - second_position))
    elif operator == "*":
        result_label.config(text=str(first_position * second_position))
    else:
        if second_position == 0 :
            result_label.config(text="error")
        else:
            result_label.config(text=str(first_position / second_position))
       


root = Tk()
root.title("CALCULATOR")
root.geometry("500x500")
root.resizable(0,0)
root.config(background="sky blue")


   

result_label= Label(root,text=" ",bg="white",fg="black",)
result_label.grid(row=0,column=0,columnspan=5,pady=(40,5),sticky='w')
result_label.config(font=("times new romen",40,"bold"))


btn7= Button(root,text="7",bg="dark blue",fg="white", width=5,height=1,command= lambda : get_digit(7))
btn7.grid (row=1,column=0)
btn7.config(font= ("times new romen",30,"bold"))


btn8= Button(root,text="8",bg="dark blue",fg="white", width=5,height=1,command= lambda : get_digit(8))
btn8.grid (row=1,column=2)
btn8.config(font= ("times new romen",30,"bold"))

btn9= Button(root,text="9",bg="dark blue",fg="white", width=5,height=1,command= lambda : get_digit(9))
btn9.grid (row=1,column=3)
btn9.config(font= ("times new romen",30,"bold"))

btn_multi= Button(root,text="*",bg="light green",fg="dark blue", width=5,height=1,command= lambda :operator_get("*"))
btn_multi.grid (row=1,column=4)
btn_multi.config(font= ("times new romen",30,"bold"))


btn4= Button(root,text="4",bg="dark blue",fg="white", width=5,height=1,command= lambda : get_digit(4))
btn4.grid (row=2,column=0)
btn4.config(font= ("times new romen",30,"bold"))

btn5= Button(root,text="5",bg="dark blue",fg="white", width=5,height=1,command= lambda: get_digit(5))
btn5.grid (row=2,column=2)
btn5.config(font= ("times new romen",30,"bold"))

btn6= Button(root,text="6",bg="dark blue",fg="white", width=5,height=1,command= lambda:get_digit(6))
btn6.grid (row=2,column=3)
btn6.config(font= ("times new romen",30,"bold"))

btn_division= Button(root,text="/",bg="light green",fg="dark blue", width=5,height=1,command= lambda:operator_get("/"))
btn_division.grid (row=2,column=4)
btn_division.config(font= ("times new romen",30,"bold"))


btn1= Button(root,text="1",bg="dark blue",fg="white", width=5,height=1,command= lambda: get_digit(1))
btn1.grid (row=3,column=0)
btn1.config(font= ("times new romen",30,"bold"))

btn2= Button(root,text="2",bg="dark blue",fg="white", width=5,height=1,command= lambda:get_digit(2))
btn2.grid (row=3,column=2)
btn2.config(font= ("times new romen",30,"bold"))

btn3= Button(root,text="3",bg="dark blue",fg="white", width=5,height=1,command= lambda: get_digit(3))
btn3.grid (row=3,column=3)
btn3.config(font= ("times new romen",30,"bold"))

btn_Sub= Button(root,text="-",bg="light green",fg="dark blue", width=5,height=1,command=lambda: operator_get("-"))
btn_Sub.grid (row=3,column=4)
btn_Sub.config(font= ("times new romen",30,"bold"))

btnc= Button(root,text="C",bg="light green",fg="dark blue", width=5,height=1,command= lambda:clear())
btnc.grid (row=4,column=0)
btnc.config(font= ("times new romen",30,"bold"))

btn0= Button(root,text="0",bg="dark blue",fg="white", width=5,height=1,command=lambda:get_digit(0))
btn0.grid (row=4,column=2)
btn0.config(font= ("times new romen",30,"bold"))

btn_dot= Button(root,text=".",bg="dark blue",fg="white", width=5,height=1,command= lambda:get_digit("."))
btn_dot.grid (row=4,column=3)
btn_dot.config(font= ("times new romen",30,"bold"))

btn_add= Button(root,text="+",bg="light green",fg="dark blue", width=5,height=1,command=lambda: operator_get("+"))
btn_add.grid (row=4,column=4)
btn_add.config(font= ("times new romen",30,"bold"))

btn_equal= Button(root,text="=",bg="pink",fg="dark blue",width=21,height=1, command= final_result)
btn_equal.grid(row=5,column=0,columnspan=5)
btn_equal.config(font= ("times new romen",30,"bold"))






root.mainloop()
