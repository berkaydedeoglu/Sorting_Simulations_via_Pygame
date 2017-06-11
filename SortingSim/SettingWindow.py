import tkinter as tk
import tkinter.ttk as ttk


class SettingWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x220")
        self.resizable(False, False)
        self.title("Settings")

        self.setting_list = list()

        self.add_widgets()

        tk.mainloop()

    @property
    def settings(self):
        return self.setting_list

    def add_widgets(self):

        def get_settings():
            alg_dict = {"Test Algorithm": "test",
                        "Selection Sort": "selection_sort"}
            self.setting_list = []
            self.setting_list.append(int(number_of_sticks.get()))
            self.setting_list.append(alg_dict[algorithms.get()])
            self.setting_list.append(int(speed.get()))
            self.setting_list.append(variable.get())

            self.quit()

            print(self.setting_list)

        tk.Label(self, text="Number of Sticks:", font="Helvatica").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self, text="Algorithm:", font="Helvatica").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self, text="Speed:", font="Helvatica").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self, text="Scenerio:", font="Helvatica").grid(row=3, column=0, sticky="w", padx=10, pady=10)

        number_of_sticks = tk.Spinbox(self)  # Review: Spinbox nesnelerini işlevselleştir!
        number_of_sticks.grid(row=0, column=1, sticky="e")

        algorithms = ttk.Combobox(self)
        algorithms['values'] = ("Test Algorithm", "Selection Sort")
        algorithms.current(0)
        algorithms.grid(row=1, column=1, sticky="e")

        speed = tk.Spinbox(self)
        speed.grid(row=2, column=1, sticky="e")

        variable = tk.StringVar()

        radio_frame = tk.Frame(self)
        radio_frame.grid(row=3, column=1, sticky="e")
        scenerio_best = tk.Radiobutton(radio_frame, text="Best", value="best", variable=variable)
        scenerio_best.pack(side="left")

        scenerio_worst = tk.Radiobutton(radio_frame, text="Worst", value="worst", variable=variable)
        scenerio_worst.pack(side="left")

        scenerio_random = tk.Radiobutton(radio_frame, text="Random", value="random", variable=variable)
        scenerio_random.pack(side="left")
        scenerio_random.select()

        button = tk.Button(self, text="Simulate", width=20, command=get_settings)
        button.grid(row=4, column=1, columnspan=2)


if __name__ == "__main__":
    root = SettingWindow()
