import tkinter as tk
def GetWeat

def getCityName():
    global city_Name_Input
    city_Name_Input = tk.Entry.get(input_city)
    print(city_Name_Input)
    input_city.delete(0,"end")



# Main window configure
root = tk.Tk()
root.geometry('600x700')
root.title("Weather App v1.0")

# Main Title
main_title = tk.Label(root, text="Better Weather")
main_title.pack()

# Input Related Widgets
input_city = tk.Entry(root)
submit_city = tk.Button(root, text="Enter", command=getCityName)



input_city.pack()
submit_city.pack()





# Main loop - DO NOT TOUCH
root.mainloop()