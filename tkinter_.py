from tkinter import *


window = Tk()

def calc_weather():
    try:
        temp = float(temp_entry.get())
    except:
        adv.set("Invalid input. \nPlease enter a number.")
        return
    if temp > 56 or temp < -82:
        adv.set("That's a record! Are you sure \nthat's the correct temperature?")
        return
    if temp < 0 or temp > 38:
        adv.set("Stay at home!")
    else:
        if temp > 30:
            adv.set("Enjoy the nice weather!")
        else:
            adv.set("Enjoy your day!")

adv = StringVar()

window.title("Weather Advice")
window.minsize(350, 100)
forecast_label = Label(window, text="Temperature Forecast:")
forecast_label.grid(row=0, column=0, padx=(10,20), pady=(25,15))
temp_entry = Entry(window)
temp_entry.grid(row=0, column=1, padx=(30,25))
calc_button = Button(window, text="Calculate", command=calc_weather)
calc_button.grid(row=1, column=0, pady=(0,25))
advice_label = Label(window, textvariable=adv)
advice_label.grid(row=1, column=1)
window.mainloop()