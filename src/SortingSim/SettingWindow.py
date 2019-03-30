import tkinter as tk
import tkinter.ttk as ttk


class SettingWindow(tk.Tk):
    """
    This is a setting window which you can set the SortingSimulator. Firstly runs this
    class in main.py then when you finish your settings and press simulate button, this
    window becomes useless anymore.

    This class has setting_list for sending settings. This list has four datas:
        setting_list[0] : Number of sticks (int)
        setting_list[1] : Algorithm, which SortingSimulator will use at sorting (string)
        setting_list[2] : Speed, simulation speed (float)
        setting_list[3] : Scenerio, best, worst or random (string)
    """
    def __init__(self):
        super().__init__()

        self.setting_list = list()

        # Window attributes
        self.geometry("400x220+100+110")
        self.resizable(False, False)
        self.title("Settings")
        self.add_widgets()  # Adding widgets

        self.mainloop()

    @property
    def settings(self):
        return self.setting_list

    def add_widgets(self):
        """
        This is a simple method that draws widgets (interface) for users.
        Also there is an event method in this.
        """

        def get_settings():
            """
            This is event method that appends settings to setting_list when
            user pressed the 'simulate' button.
            """

            # Translating from user to SortSticks.sort() method.
            alg_dict = {"Test Algorithm": "test",
                        "Selection Sort": "selection_sort",
                        "Bubble Sort": "bubble_sort"}

            # Append settings
            self.setting_list = []  # Guaranteed list is empty
            self.setting_list.append(int(number_of_sticks.get()))
            self.setting_list.append(alg_dict[algorithms.get()])
            self.setting_list.append(float(speed.get()))
            self.setting_list.append(variable.get())

            self.quit()

        variable = tk.StringVar()

        # All labels
        tk.Label(self, text="Number of Sticks:", font="Helvatica").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self, text="Algorithm:", font="Helvatica").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self, text="Speed:", font="Helvatica").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self, text="Scenerio:", font="Helvatica").grid(row=3, column=0, sticky="w", padx=10, pady=10)

        # All widgets
        number_of_sticks = tk.Spinbox(self, from_=2, to=500, increment=10)
        algorithms = ttk.Combobox(self)
        speed = tk.Spinbox(self, from_=0.5, to=15, increment=0.5)
        radio_frame = tk.Frame(self)
        scenerio_best = tk.Radiobutton(radio_frame, text="Best", value="best", variable=variable)
        scenerio_worst = tk.Radiobutton(radio_frame, text="Worst", value="worst", variable=variable)
        scenerio_random = tk.Radiobutton(radio_frame, text="Random", value="random", variable=variable)
        button = tk.Button(self, text="Simulate", width=20, command=get_settings)

        # Layout management
        number_of_sticks.grid(row=0, column=1, sticky="e")
        algorithms.grid(row=1, column=1, sticky="e")
        speed.grid(row=2, column=1, sticky="e")
        radio_frame.grid(row=3, column=1, sticky="e")
        scenerio_best.pack(side="left")
        scenerio_worst.pack(side="left")
        scenerio_random.pack(side="left")
        button.grid(row=4, column=1, columnspan=2)

        # Widget attributes
        number_of_sticks.delete(0, tk.END)  # Clear
        number_of_sticks.insert(tk.INSERT, 100)
        algorithms['values'] = ("Test Algorithm", "Selection Sort", "Bubble Sort")  # Review: Bu liste daha duzenli tutulabilir mi?
        algorithms.current(0)
        speed.delete(0, tk.END)   # Clear
        speed.insert(tk.INSERT, 5)
        scenerio_random.select()


if __name__ == "__main__":
    root = SettingWindow()
