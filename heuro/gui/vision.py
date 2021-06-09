import tkinter as tk


class Vision(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.iconphoto(False, tk.PhotoImage(file='img/logo.png'))
        self.bg = "#121222"
        self.b_p = {'bg': "#242434", 'fg': "#FFFFFF", 'font': ("Courier", 15)}
        self.config(background=self.bg)

        self.build_pic()
        self.build_control()
        self.build_setting()
        for i in range(3):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

    def draw_point(self, coords, color):
        w = int(self.canvas.cget("width"))
        h = int(self.canvas.cget("height"))
        self.canvas.create_oval(int(w / 2 + w * coords[0]), int(h / 2 + h * coords[1]),
                                int(w / 2 + w * coords[0] + 1), int(h / 2 + h * coords[1] + 1),
                                width=100, fill=color)

    def put_img(self, img_name):
        self.img = tk.PhotoImage(file=f'img/{img_name}.png')
        self.canvas.create_image((250, 250), image=self.img)

    def build_pic(self):
        self.left_pic_frame = tk.Frame(self, bg=self.bg)
        self.left_pic_frame.grid(column=0, row=0)
        self.canvas = tk.Canvas(self.left_pic_frame, width=500, height=500, bg=self.bg)
        self.put_img('rastrigin')
        self.canvas.grid(column=0, row=0)
        self.left_pic_frame.columnconfigure(0, weight=1)
        self.left_pic_frame.rowconfigure(0, weight=1)

    def build_control(self):
        self.middle_control_frame = tk.Frame(self, bg=self.bg)
        self.middle_control_frame.grid(column=1, row=0)
        for i in range(5):
            self.middle_control_frame.rowconfigure(i, weight=1)
            self.middle_control_frame.columnconfigure(i, weight=1)

        self.middle_control_frame.best_val = tk.Label(self.middle_control_frame,
                                                      text="Best result", **self.b_p)
        self.middle_control_frame.best_val.grid(column=0, row=0)

        self.middle_control_frame.current_val = tk.Label(self.middle_control_frame,
                                                         text="Current result", **self.b_p)
        self.middle_control_frame.current_val.grid(column=0, row=1)

        self.middle_control_frame.b_start = tk.Button(self.middle_control_frame,
                                                      text="Start", **self.b_p)
        self.middle_control_frame.b_start.grid(column=0, row=2)

        self.middle_control_frame.b_start = tk.Button(self.middle_control_frame,
                                                      text="+1 step", **self.b_p)
        self.middle_control_frame.b_start.grid(column=0, row=3)

        self.middle_control_frame.b_start = tk.Button(self.middle_control_frame,
                                                      text="To end", **self.b_p)
        self.middle_control_frame.b_start.grid(column=0, row=4, sticky='NEWS')

    def build_setting(self):
        test_f = ['Rastrigin', 'Rosenbrock', 'Sphere']
        self.rigth_setting_frame = tk.Frame(self, bg=self.bg)
        self.rigth_setting_frame.grid(column=2, row=0)
        self.rigth_setting_frame.test_func = tk.Label(self.rigth_setting_frame, text='Testing function',
                                                      **self.b_p)
        self.rigth_setting_frame.test_func.grid(column=0, row=0)
        variable_t = tk.StringVar(self)
        variable_t.set(test_f[0])
        self.rigth_setting_frame.test_funcs = tk.OptionMenu(self.rigth_setting_frame, variable_t, *test_f,
                                                            command=lambda x: self.put_img(variable_t.get()))
        self.rigth_setting_frame.test_funcs.config(**self.b_p)
        self.rigth_setting_frame.test_funcs['menu'].config(**self.b_p)
        self.rigth_setting_frame.test_funcs.grid(column=0, row=1)

        alg = ['Simple Hill Climbing', 'Shotgun Hill Climbing', 'Genetic Algorithm']
        self.rigth_setting_frame.algs_label = tk.Label(self.rigth_setting_frame, text='Algorithm',
                                                       **self.b_p)
        self.rigth_setting_frame.algs_label.grid(column=0, row=2)

        variable_a = tk.StringVar(self)
        variable_a.set(alg[0])

        self.rigth_setting_frame.algs = tk.OptionMenu(self.rigth_setting_frame, variable_a, *alg)
        self.rigth_setting_frame.algs.config(**self.b_p)
        self.rigth_setting_frame.algs['menu'].config(**self.b_p)
        self.rigth_setting_frame.algs.grid(column=0, row=3)
