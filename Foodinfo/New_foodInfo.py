import csv
import tkinter as tk
import tkinter.ttk

# read the food info
csvfile = open('Foodinfo.csv', newline='', encoding="utf-8")
rows = csv.reader(csvfile)

# create the gui
root = tk.Tk()
canvas1 = tk.Canvas(root, width=900, height=1300)
canvas1.create_window(400, 200, window=tkinter.ttk.Separator(canvas1, orient='vertical').grid(row=0, column=2))

# get all the info of the ingredient
count=0
for row in rows:
    # all the info are on the second row of the csv
    if count==1:
        row=str(row)
        data = row.split(",")
        nutrition = []
        unit = []
        for nu in data[1::]:
            if len(nu)>=2:
                # if the info has units
                if '(' in nu:
                    nutrition.append(nu[2:nu.index('(')])
                    tmp = nu[::-1]
                    unit.append(nu[len(nu)-tmp.index('('):-2])
                else:
                    nutrition.append(nu[2:-1])
        break
    count+=1

# get the food info the user wants to know
label1 = tk.Label(root, text="The food Info you want to know")
label1.config(font=('helvetica', 14))
canvas1.create_window(400, 200, window=label1.grid(row=0, column=0, columnspan=5))
#label1.grid(row=0, column=2)

entry1 = tk.Entry(root)
# canvas1.create_window(200, 50, window=entry1)
entry1.grid(row=1, column=0, columnspan=5)
canvas1.create_window(200, 25, window=entry1.grid(row=1, column=0, columnspan=5))

def nutrition_Select():
    selection=[]
    for i in checkboxes:
        if checkboxes[i].get()==True:
            selection.append(nutrition[i])
    food = entry1.get()
    newWindow = tk.Toplevel(root)
    newWindow.geometry("750x250")
    count = 0
    csvfile2 = open('Foodinfo.csv', newline='', encoding="utf-8")
    rows2 = csv.reader(csvfile2)

    for row in rows2:
        if row[2]==food or row[3]==food:
            found=row
            for x in selection:
                if x in nutrition:
                    if nutrition.index(x)>=5:
                        tk.Label(newWindow, text=x+" "+row[nutrition.index(x)+1]+" "+unit[nutrition.index(x)-4], font='helvetica').grid(row=count)
                    else:
                        tk.Label(newWindow, text=x+" "+row[nutrition.index(x)+1], font='helvetica').grid(row=count)
                count+=1
            break
    
    csvfile2.close()

checkboxes = {}
for i in range(len(nutrition)-1):
    checkboxes[i] = tk.BooleanVar()
    Cb = tk.Checkbutton(root, text=nutrition[i], variable=checkboxes[i])
    Cb.grid(row=i//5+2, column=(i%5))
    # canvas1.create_window(100+100*(i%8),75+50*(i//8), window=Cb)

btn = tk.Button(root, text="Enter", width=10, command=nutrition_Select)
btn.grid(row=24, column=2)

# used to loop the window
root.mainloop()
# close the csv after using
# csvfile.close()