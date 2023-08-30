import time
import tkinter as tk

class Stopwatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.pack()

        self._start_time = None
        self._elapsed_time = 0
        self._running = False

        self._update()

    def create_widgets(self):
        self._elapsed_time_var = tk.StringVar(value='00:00:00')
        self._elapsed_time_label = tk.Label(self, textvariable=self._elapsed_time_var, font=('Courier', 30))
        self._elapsed_time_label.pack(pady=10)

        self._start_button = tk.Button(self, text='Start', command=self.start)
        self._start_button.pack(side='left', padx=5)
        self._stop_button = tk.Button(self, text='Stop', command=self.stop)
        self._stop_button.pack(side='left', padx=5)
        self._reset_button = tk.Button(self, text='Reset', command=self.reset)
        self._reset_button.pack(side='left', padx=5)

    def start(self):
        if not self._running:
            self._start_time = time.monotonic()
            self._running = True

    def stop(self):
        if self._running:
            self._elapsed_time += time.monotonic() - self._start_time
            self._start_time = None
            self._running = False

    def reset(self):
        self._start_time = None
        self._elapsed_time = 0
        self._running = False
        self._update()

    def _update(self):
        if self._running:
            elapsed_time = self._elapsed_time + time.monotonic() - self._start_time
        else:
            elapsed_time = self._elapsed_time

        minutes, seconds = divmod(int(elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)

        self._elapsed_time_var.set('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        self.after(50, self._update)

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
