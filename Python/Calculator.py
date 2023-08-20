import tkinter as tk

#Basic calutcation string
calcuation = ""

def add_to_calulation(symbol):
    global calcuation
    calcuation+= str(symbol)

    text_result.delete(1.0,"end")
    text_result.insert(1.0, calcuation)

def evaluate_calculation():
    global calcuation
    try:
        calcuation =str(eval(calcuation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calcuation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calcuation
    calcuation = " "
    text_result.delete(1.0, "end")

#have to build a gui
#creates the gui
root = tk.Tk()
root.title("Tunde Cal")
#Makes background color
root.config(bg ="skyblue")
#adjust the width of border
root.config(borderwidth =1)
root.geometry("300x275") #How big the window will be
#adding text field for results
text_result =tk.Text(root,height = 2, width = 16, font= ("Arial",24))
text_result.grid(columnspan= 5)
#Creat indival buttons                     #Lamba referece to a function
btn_1 =tk.Button(root, text="1", command=lambda: add_to_calulation(1), width=5, font =("Arial" , 14))
btn_1.grid(row=2, column=1)
btn_2 =tk.Button(root, text="2", command=lambda: add_to_calulation(2), width=5, font =("Arial" , 14))
btn_2.grid(row=2, column=2)
btn_3 =tk.Button(root, text="3", command=lambda: add_to_calulation(3), width=5, font =("Arial" , 14))
btn_3.grid(row=2, column=3)
btn_4 =tk.Button(root, text="4", command=lambda: add_to_calulation(4), width=5, font =("Arial" , 14))
btn_4.grid(row=3, column=1)
btn_5 =tk.Button(root, text="5", command=lambda: add_to_calulation(5), width=5, font =("Arial" , 14))
btn_5.grid(row=3, column=2)
btn_6 =tk.Button(root, text="6", command=lambda: add_to_calulation(6), width=5, font =("Arial" , 14))
btn_6.grid(row=3, column=3)
btn_7 =tk.Button(root, text="7", command=lambda: add_to_calulation(7), width=5, font =("Arial" , 14))
btn_7.grid(row=4, column=1)
btn_8 =tk.Button(root, text="8", command=lambda: add_to_calulation(8), width=5, font =("Arial" , 14))
btn_8.grid(row=4, column=2)
btn_9 =tk.Button(root, text="9", command=lambda: add_to_calulation(9), width=5, font =("Arial" , 14))
btn_9.grid(row=4, column=3)
btn_0 =tk.Button(root, text="0", command=lambda: add_to_calulation(0), width=5, font =("Arial" , 14))
btn_0.grid(row=5, column=2)
# where the operations are down
btn_plus =tk.Button(root, text="+", command=lambda: add_to_calulation("+"), width=5, font =("Arial" , 14))
btn_plus.grid(row=2, column=4)
btn_minus =tk.Button(root, text="-", command=lambda: add_to_calulation("-"), width=5, font =("Arial" , 14))
btn_minus.grid(row=3, column=4)
btn_multiple =tk.Button(root, text="*", command=lambda: add_to_calulation("*"), width=5, font =("Arial" , 14))
btn_multiple.grid(row=4, column=4)
btn_division =tk.Button(root, text="/", command=lambda: add_to_calulation("/"), width=5, font =("Arial" , 14))
btn_division.grid(row=5, column=4)
btn_open =tk.Button(root, text="(", command=lambda: add_to_calulation("("), width=5, font =("Arial" , 14))
btn_open.grid(row=5, column=1)
btn_close =tk.Button(root, text=")", command=lambda: add_to_calulation(")"), width=5, font =("Arial" , 14))
btn_close.grid(row=5, column=3)
#We are able to remove lmba and p() because now we passing the actuallying function with () it means calling the function with parameter have to use lamba
btn_clear =tk.Button(root, text="CLEAR", command=clear_field, width=12, font =("Arial" , 14))
btn_clear.grid(row=6, column=1 ,columnspan= 2)
btn_equals =tk.Button(root, text="=", command=evaluate_calculation, width=12, font =("Arial" , 14))
btn_equals.grid(row=6, column=3,columnspan =2)
root.mainloop()