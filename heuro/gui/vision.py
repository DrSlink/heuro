import tkinter as tk


class Vision(tk.Tk):
    def __init__(self, master=None,
                 functions: dict = None,
                 algorithms: dict = None,
                 constr: list = None):
        super().__init__(master)
        self.test_f = functions
        self.test_f_list = list(functions.keys())
        self.algs = algorithms
        self.algs_list = list(algorithms.keys())
        self.constr = constr
        self.gen = None
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
        self.canvas.create_oval(int(w / 2 * coords[0]),
                                int(h / 2 * coords[1]),
                                int(w / 2 * coords[0] + 1),
                                int(h / 2 * coords[1] + 1),
                                width=2, outline=color)

    def draw_arrow(self, coords):
        w = int(self.canvas.cget("width"))
        h = int(self.canvas.cget("height"))
        self.canvas.create_line(int(w / 2 * coords[0]),
                                int(h / 2 * coords[1]),
                                int(w / 2 * coords[2]),
                                int(h / 2 * coords[3]),
                                arrow=tk.LAST,
                                width=1, fill='white')

    def on_start(self):
        self.alg = self.algs[self.variable_a.get()]
        self.gen = self.alg.fit(self.test_f[self.variable_t.get()],
                                self.constr)
        self.put_img(self.variable_t.get())
        self.on_step()

    def on_step(self):
        if self.gen:
            try:
                res = next(self.gen)
                if res[4]:
                    self.draw_arrow(list(map(lambda x: 1 + x / 5,
                                             res[0] + res[2])))
                not_worse = res[1] >= res[3]
                color = 'white' if not_worse else 'black'
                self.draw_point((1 + res[2][0] / 5, 1 + res[2][1] / 5), color)
            except StopIteration:
                self.gen = None

    def on_end(self):
        if self.gen:
            try:
                while self.gen:
                    self.on_step()
            except StopIteration:
                self.gen = None

    def put_img(self, img_name):
        self.img = tk.PhotoImage(file=f'img/{img_name}.png')
        self.canvas.create_image((250, 250), image=self.img)

    def build_pic(self):
        self.left_pic_frame = tk.Frame(self, bg=self.bg)
        self.left_pic_frame.grid(column=0, row=0)
        self.canvas = tk.Canvas(self.left_pic_frame,
                                width=500, height=500, bg=self.bg)
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

        self.middle_control_frame.best_val = tk.Label(
            self.middle_control_frame,
            text="Best result", **self.b_p)
        self.middle_control_frame.best_val.grid(column=0, row=0)

        self.middle_control_frame.current_val = tk.Label(
            self.middle_control_frame,
            text="Current result", **self.b_p)
        self.middle_control_frame.current_val.grid(column=0, row=1)

        self.middle_control_frame.b_start = tk.Button(
            self.middle_control_frame,
            text="Start", command=self.on_start, **self.b_p)
        self.middle_control_frame.b_start.grid(column=0, row=2)

        self.middle_control_frame.b_start = tk.Button(
            self.middle_control_frame,
            text="+1 step", command=self.on_step, **self.b_p)
        self.middle_control_frame.b_start.grid(column=0, row=3)

        self.middle_control_frame.b_start = tk.Button(
            self.middle_control_frame,
            text="To end", command=self.on_end, **self.b_p)
        self.middle_control_frame.b_start.grid(column=0, row=4, sticky='NEWS')

    def build_setting(self):
        self.rigth_setting_frame = tk.Frame(self, bg=self.bg)
        self.rigth_setting_frame.grid(column=2, row=0)
        self.rigth_setting_frame.test_func = tk.Label(self.rigth_setting_frame,
                                                      text='Testing function',
                                                      **self.b_p)
        self.rigth_setting_frame.test_func.grid(column=0, row=0)
        self.variable_t = tk.StringVar(self)
        self.variable_t.set(self.test_f_list[0])
        self.rigth_setting_frame.test_funcs = tk.OptionMenu(
            self.rigth_setting_frame, self.variable_t, *self.test_f_list,
            command=lambda x: self.put_img(self.variable_t.get()))
        self.rigth_setting_frame.test_funcs.config(**self.b_p)
        self.rigth_setting_frame.test_funcs['menu'].config(**self.b_p)
        self.rigth_setting_frame.test_funcs.grid(column=0, row=1)

        self.rigth_setting_frame.algs_label = tk.Label(
            self.rigth_setting_frame, text='Algorithm',
            **self.b_p)
        self.rigth_setting_frame.algs_label.grid(column=0, row=2)

        self.variable_a = tk.StringVar(self)
        self.variable_a.set(self.algs_list[0])

        self.rigth_setting_frame.algs = tk.OptionMenu(self.rigth_setting_frame,
                                                      self.variable_a,
                                                      *self.algs_list)
        self.rigth_setting_frame.algs.config(**self.b_p)
        self.rigth_setting_frame.algs['menu'].config(**self.b_p)
        self.rigth_setting_frame.algs.grid(column=0, row=3)
