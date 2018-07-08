import Tkinter as TK
import ttk

class CONST:
    LARGE_FONT= ("Consolas", 12)

class CruciblePluginApp(TK.Tk):
    def __init__(self, *args, **kwargs):
        TK.Tk.__init__(self, *args, **kwargs)

        self.__all_frames = {}

        icon = TK.PhotoImage(file='crucible.gif')
        self.call('wm', 'iconphoto', self._w, icon)
        TK.Tk.wm_title(self, "Crucible P4 Plugin")

        self.__state = TK.IntVar()
        self.__state.trace('w', self.__change_state)

        frame = NewReview(self, self.__state)
        self.__all_frames[frame.ID] = frame

        frame = AppendToReview(self, self.__state)
        self.__all_frames[frame.ID] = frame

    def __change_state(self, *args):
        frame_id = self.__state.get()

        print self.__all_frames
        for k, v in self.__all_frames.iteritems():
            v.enable(frame_id == k)

class NewReview(TK.Frame):
    ID = 0
    def __init__(self, parent, variable):
        TK.Frame.__init__(self, parent)

        self.__radio = ttk.Radiobutton(self, text="NEW REVIEW", variable=variable, value=self.ID)
        self.__radio
        self.__radio.grid(row=0, column=0, columnspan=2, sticky=TK.W)
        # self.__radio.pack(side=TK.TOP, ipadx=3)

        label = ttk.Label(self, text="Title", font=CONST.LARGE_FONT)
        label.grid(row=1, column=0)

        self.__code_review_title = TK.StringVar()
        self.__code_review_title.set("Code review title")

        text = ttk.Entry(self, font=CONST.LARGE_FONT, textvariable=self.__code_review_title)
        text.grid(row=1, column=1)

        self.pack(anchor=TK.NW, fill=TK.X, padx=5, pady=5)

    def enable(self, isEnabled):
        state = 'enable' if isEnabled else 'disable'
        for child in self.winfo_children():
            if child is not self.__radio:
                child.configure(state=state)

    


class AppendToReview(TK.Frame):
    ID = 1
    def __init__(self, parent, variable):
        TK.Frame.__init__(self, parent)

        self.__radio = ttk.Radiobutton(self, text="Append to Review", variable=variable, value=self.ID)
        self.__radio.pack(side=TK.TOP, ipadx=3)

        treeview = ttk.Treeview(self, columns=('Date', 'Project', 'Title'), selectmode=TK.BROWSE, displaycolumns='#all')
        treeview.column('#0', stretch=0, width=5)
        treeview.column('Date', stretch=0, width=80)
        treeview.column('Project', stretch=0, width=80)
        for i in xrange(15):
            values = ['{}/01/1989'.format(i), 'Project_{}'.format(i%2), 'CR_{}'.format(i)]
            treeview.insert('', 'end', values=values)
        treeview.pack(side=TK.LEFT, fill=TK.BOTH, expand=1)

        self.pack(anchor=TK.NW, fill=TK.BOTH, padx=5, pady=5)

        

    def enable(self, isEnabled):
        state = 'enable' if isEnabled else 'disable'
        for child in self.winfo_children():
            if child is not self.__radio:
                child.configure(state=state)

if __name__ == "__main__":
    gui = CruciblePluginApp()
    gui.mainloop()