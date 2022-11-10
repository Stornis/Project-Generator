from tkinter import *


def q():
    Tk.quit(cal_btn)


def fc():
    if first_bt.get().isdigit():
        first_count = first_bt.get()
    else:
        first_count = 0
    return first_count


def sc():
    if second_bt.get().isdigit():
        second_count = second_bt.get()
    else:
        second_count = 0
    return second_count


def tc():
    if third_bt.get().isdigit():
        third_count = third_bt.get()
    else:
        third_count = 0
    return third_count


window = Tk()
window.title('Генератор уравнений')
window.geometry('500x400')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

first = Label(
    frame,
    text="Введите кол-во ур-ий первого уровня:  "
)
first.grid(row=3, column=1)

second = Label(
    frame,
    text="Введите кол-во ур-ий второго уровня:  ",
)
second.grid(row=4, column=1)

third = Label(
    frame,
    text="Введите кол-во ур-ий третьего уровня:  ",
)
third.grid(row=5, column=1)

first_bt = Entry(
    frame,
)
first_bt.grid(row=3, column=2, pady=5)

second_bt = Entry(
    frame,
)
second_bt.grid(row=4, column=2, pady=5)

third_bt = Entry(
    frame,
)
third_bt.grid(row=5, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Сгенерировать',
    command=q
)
cal_btn.grid(row=6, column=2)
window.mainloop()


first_level = int(fc())
second_level = int(sc())
third_level = int(tc())
