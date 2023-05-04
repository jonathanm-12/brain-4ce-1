import tkinter as tk
import sys
import os

sys.path.append('VirtualEnvironment')

os.environ['MY_PROJECT_MODELS'] = 'VirtualEnvironment/models'

os.environ['myConfig'] = 'VirtualEnvironment'


import main_sim


class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True)
        self.create_widgets()

    def create_widgets(self):

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(expand=True)

        self.button1 = tk.Button(self.button_frame, text="Run Virtual Environment", command=self.button1_clicked)
        self.button1.pack(side="top", pady=10)

        self.button2 = tk.Button(self.button_frame, text="Run 30s Game", command=self.button2_clicked)
        self.button2.pack(side="bottom", pady=10)

        self.button3 = tk.Button(self.button_frame, text="Run 2D Game", command=self.button1_clicked)
        self.button3.pack(side="top", pady=20)

    def button1_clicked(self):


        print("Button 1 clicked")

        run = main_sim.MyApp()
    
        run.run()



    def button2_clicked(self):
        print("Error: Not yet pushed to GitHub.")

if __name__ == '__main__':
    root = tk.Tk()

    root.title("Main Menu")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 200
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_pos, y_pos))
    app = MainMenu(master=root)
    app.mainloop()