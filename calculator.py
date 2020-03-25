from tkinter import *
box = Tk()
box.title('InfiniCalcV4 with GUI')
summ = Entry(box, width=50, borderwidth=20)
summ.grid(row=0, column=0, columnspan = 6)
def insertnum(num):
    summ.insert(END, num)
    # alternative way of doing stuff!
    #sum3 = summ.get()
    #clearcom()
    #summ.insert(0,sum3 + num)
def clearcom():
    summ.delete(0, END)
def dothething():
    sumnumbers = []
    operators = []
    for a in summ.get().split(' '):
        try:
            sumnumbers.append(int(a))
        except:
            operators.append(a)
    newnewsum = list(zip(operators,sumnumbers[1:]))
    sum2 = sumnumbers[0]
    for a in range(0, len(newnewsum)):
        if a == len(newnewsum)-1:
            if newnewsum[a][0] == '*':
                sum2 *= newnewsum[a][1]
            elif newnewsum[a][0] == '/':
                sum2 /= newnewsum[a][1]
            elif newnewsum[a][0] == '+':
                sum2 += newnewsum[a][1]
            elif newnewsum[a][0] == '-':
                sum2 -= newnewsum[a][1]
        elif newnewsum[a][0] == '*':
            sum2 *= newnewsum[a][1]
        elif newnewsum[a][0] == '/':
            sum2 /= newnewsum[a][1]
        elif newnewsum[a][0] == '+':
            sum2 += newnewsum[a][1]
        elif newnewsum[a][0] == '-':
            sum2 -= newnewsum[a][1]
    clearcom()
    summ.insert(0, str(sum2))
add = Button(box, text='+', padx=16, pady=10,command=lambda: insertnum(' + ')).grid(row=1,column=3)
subtract = Button(box, text='-',padx=18, pady=10, command=lambda: insertnum(' - ')).grid(row=2, column=3)
multiply = Button(box, text='*',padx=18, pady=10, command=lambda: insertnum(' * ')).grid(row=1, column=5)
divide = Button(box, text='/',padx=17, pady=10, command=lambda: insertnum(' / ')).grid(row=1, column=4)
clear = Button(box, text = 'C',padx=44, pady=10, command = clearcom).grid(row=2, column=4, columnspan=2)
resolve = Button(box, text = '=',padx=44, pady=10, command = dothething).grid(row=3, column=4,columnspan=2)
button_1 = Button(box, text='1', padx=18, pady=10, command = lambda: insertnum('1'))
button_2 = Button(box, text='2', padx=18, pady=10, command = lambda: insertnum('2'))
button_3 = Button(box, text='3', padx=18, pady=10, command = lambda: insertnum('3'))
button_4 = Button(box, text='4', padx=18, pady=10, command = lambda: insertnum('4'))
button_5 = Button(box, text='5', padx=18, pady=10, command = lambda: insertnum('5'))
button_6 = Button(box, text='6', padx=18, pady=10, command = lambda: insertnum('6'))
button_7 = Button(box, text='7', padx=18, pady=10, command = lambda: insertnum('7'))
button_8 = Button(box, text='8', padx=18, pady=10, command = lambda: insertnum('8'))
button_9 = Button(box, text='9', padx=18, pady=10, command = lambda: insertnum('9'))
button_0 = Button(box, text='0', padx=17, pady=10, command = lambda: insertnum('0'))
buttons = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_0]
i, j = 1, 0
def makebuttons(l, m):
    global i, j
    for a in buttons[l:m]:
        a.grid(row=i,column=j)
        j += 1
    j -= 3
makebuttons(0,3);i += 1
makebuttons(3,6);i += 1
makebuttons(6,10)
