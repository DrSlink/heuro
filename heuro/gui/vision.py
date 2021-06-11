"""Simple visual representation of algorithms work."""
import tkinter as tk
import gettext


class Vision(tk.Tk):
    """Simple visual representation of algorithms work."""

    def __init__(self, master=None,
                 functions: dict = None,
                 algorithms: dict = None,
                 constr: list = None):
        """Class initialization."""
        super().__init__(master)
        en = gettext.translation('heuro', localedir='po', languages=['en'])
        ru = gettext.translation('heuro', localedir='po', languages=['ru'])
        self._ = en.gettext
        self.langs = {'en': en, 'ru': ru}
        self.lang_list = list(self.langs.keys())
        self.test_f = list(functions.values())
        self.test_f_names = list(functions.keys())
        self.test_f_trans = list(map(self._, self.test_f_names))
        self.algs = list(algorithms.values())
        self.algs_names = list(algorithms.keys())
        self.algs_trans = list(map(self._, self.algs_names))
        self.constr = constr
        self.gen = None
        self.iconphoto(False, tk.PhotoImage(file='img/logo.png'))
        self.bg = "#121222"
        self.b_p = {'bg': "#242434", 'fg': "#FFFFFF", 'font': ("Courier", 15)}
        self.config(background=self.bg)

        self.build_pic()
        self.build_control()
        self.build_setting()
        self.build_lang()
        for i in range(4):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

    def change(self, a, b):
        """Change label on menu."""
        a.set(b)
        func_idx = self.test_f_trans.index(self.variable_t.get())
        self.put_img(self.test_f_names[func_idx])

    def change_lang(self, value):
        """Change app language."""
        _ = self.langs[value].gettext

        self.best_val_l['text'] = _("Best result")
        self.current_val_l['text'] = _("Current result")
        self.b_start['text'] = _("Start")
        self.b_step['text'] = _("+1 step")
        self.b_end['text'] = _("To end")
        self.test_func['text'] = _('Testing function')
        self.algs_label['text'] = _('Algorithm')
        func_idx = self.test_f_trans.index(self.variable_t.get())
        self.test_f_trans = list(map(_, self.test_f_names))
        self.variable_t.set(_(self.test_f_names[func_idx]))
        self.test_f_menu['menu'].delete(0, 'end')
        for test_f in self.test_f_trans:
            def comm(x=self.variable_t, y=test_f):
                self.change(x, y)

            self.test_f_menu['menu'].add_command(label=test_f, command=comm)

        alg_idx = self.algs_trans.index(self.variable_a.get())
        self.algs_trans = list(map(_, self.algs_names))

        self.variable_a.set(_(self.algs_names[alg_idx]))
        self.algs_menu['menu'].delete(0, 'end')
        for alg in self.algs_trans:
            comm = tk._setit(self.variable_a, alg)
            self.algs_menu['menu'].add_command(label=alg, command=comm)

    def build_lang(self):
        """Build language frame."""
        self.lang_frame = tk.Frame(self, bg=self.bg)
        self.lang_frame.grid(column=3, row=0, sticky='EN')

        self.variable_l = tk.StringVar(self)
        self.variable_l.set(self.lang_list[0])

        self.lang_frame.lang = tk.OptionMenu(self.lang_frame,
                                             self.variable_l,
                                             *self.lang_list,
                                             command=self.change_lang)
        self.lang_frame.lang.config(**self.b_p)
        self.lang_frame.lang['menu'].config(**self.b_p)
        self.lang_frame.lang.grid(column=0, row=0)

    def draw_point(self, coords, color):
        """Draw point on canvas."""
        w = int(self.canvas.cget("width"))
        h = int(self.canvas.cget("height"))
        self.canvas.create_oval(int(w / 2 * coords[0]),
                                int(h / 2 * coords[1]),
                                int(w / 2 * coords[0] + 1),
                                int(h / 2 * coords[1] + 1),
                                width=2, outline=color)

    def draw_arrow(self, coords):
        """Draw arrow on canvas."""
        w = int(self.canvas.cget("width"))
        h = int(self.canvas.cget("height"))
        self.canvas.create_line(int(w / 2 * coords[0]),
                                int(h / 2 * coords[1]),
                                int(w / 2 * coords[2]),
                                int(h / 2 * coords[3]),
                                arrow=tk.LAST,
                                width=1, fill='white')

    def on_start(self):
        """Start algorithm."""
        alg_idx = self.algs_trans.index(self.variable_a.get())
        self.alg = self.algs[alg_idx]
        func_idx = self.test_f_trans.index(self.variable_t.get())
        self.gen = self.alg.fit(self.test_f[func_idx], self.constr)
        self.put_img(self.test_f_names[func_idx])
        self.on_step()

    def on_step(self):
        """Make next step of algorithm."""
        if self.gen:
            try:
                res = next(self.gen)
                if res[4]:
                    self.draw_arrow(list(map(lambda x: 1 + x / 5,
                                             res[0] + res[2])))
                not_worse = res[1] >= res[3]
                self.current_val['text'] = str(round(res[3], 3))
                if not_worse:
                    self.best_val['text'] = str(round(res[3], 3))
                color = 'white' if not_worse else 'black'
                self.draw_point((1 + res[2][0] / self.constr[0][1],
                                 1 + res[2][1] / self.constr[1][1]), color)
            except StopIteration:
                self.gen = None

    def on_end(self):
        """Delete generator of ended algorithm."""
        if self.gen:
            try:
                while self.gen:
                    self.on_step()
            except StopIteration:
                self.gen = None

    def put_img(self, img_name):
        """Upload function image."""
        img_name = self.langs['en'].gettext(img_name)
        self.img = tk.PhotoImage(file=f'img/{img_name}.png')
        self.canvas.create_image((250, 250), image=self.img)

    def build_pic(self):
        """Build canvas with image."""
        self.left_pic_frame = tk.Frame(self, bg=self.bg)
        self.left_pic_frame.grid(column=0, row=0)
        self.canvas = tk.Canvas(self.left_pic_frame,
                                width=500, height=500, bg=self.bg)
        self.put_img('rastrigin')
        self.canvas.grid(column=0, row=0)
        self.left_pic_frame.columnconfigure(0, weight=1)
        self.left_pic_frame.rowconfigure(0, weight=1)

    def build_control(self):
        """Build execution control panel."""
        self.middle_control_frame = tk.Frame(self, bg=self.bg)
        self.middle_control_frame.grid(column=1, row=0)
        for i in range(5):
            self.middle_control_frame.rowconfigure(i, weight=1)
            self.middle_control_frame.columnconfigure(i, weight=1)

        self.best_val_l = tk.Label(self.middle_control_frame,
                                   text=self._("Best result"), **self.b_p)
        self.best_val_l.grid(column=0, row=0, sticky='NEWS')

        self.best_val = tk.Label(self.middle_control_frame,
                                 text="-", **self.b_p)
        self.best_val.grid(column=0, row=1, sticky='NEWS')

        self.current_val_l = tk.Label(self.middle_control_frame,
                                      text=self._("Current result"),
                                      **self.b_p)
        self.current_val_l.grid(column=0, row=2, sticky='NEWS')

        self.current_val = tk.Label(self.middle_control_frame,
                                    text="-", **self.b_p)
        self.current_val.grid(column=0, row=3, sticky='NEWS')

        self.b_start = tk.Button(self.middle_control_frame,
                                 text=self._("Start"), command=self.on_start,
                                 **self.b_p)
        self.b_start.grid(column=0, row=4, sticky='NEWS')

        self.b_step = tk.Button(self.middle_control_frame,
                                text=self._("+1 step"), command=self.on_step,
                                **self.b_p)
        self.b_step.grid(column=0, row=5, sticky='NEWS')

        self.b_end = tk.Button(self.middle_control_frame,
                               text=self._("To end"), command=self.on_end,
                               **self.b_p)
        self.b_end.grid(column=0, row=6, sticky='NEWS')

    def build_setting(self):
        """Build functions and algorithms setting panel."""
        self.rigth_setting_frame = tk.Frame(self, bg=self.bg)
        self.rigth_setting_frame.grid(column=2, row=0)
        self.test_func = tk.Label(self.rigth_setting_frame,
                                  text=self._('Testing function'),
                                  **self.b_p)
        self.test_func.grid(column=0, row=0)
        self.variable_t = tk.StringVar(self)
        self.variable_t.set(self.test_f_trans[0])
        self.test_f_menu = tk.OptionMenu(
            self.rigth_setting_frame, self.variable_t, *self.test_f_trans,
            command=lambda x: self.put_img(self.variable_t.get()))
        self.test_f_menu.config(**self.b_p)
        self.test_f_menu['menu'].config(**self.b_p)
        self.test_f_menu.grid(column=0, row=1)

        self.algs_label = tk.Label(self.rigth_setting_frame,
                                   text=self._('Algorithm'), **self.b_p)
        self.algs_label.grid(column=0, row=2)

        self.variable_a = tk.StringVar(self)
        self.variable_a.set(self.algs_trans[0])

        self.algs_menu = tk.OptionMenu(self.rigth_setting_frame,
                                       self.variable_a,
                                       *self.algs_trans)
        self.algs_menu.config(**self.b_p)
        self.algs_menu['menu'].config(**self.b_p)
        self.algs_menu.grid(column=0, row=3)
