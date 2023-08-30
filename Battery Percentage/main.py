import ttkbootstrap as tb
import psutil

root = tb.Window(themename='superhero')
root.geometry("500x300")
root.title("Battery Percentage")
root.resizable(False, False)

battery = psutil.sensors_battery()
percent = battery.percent

meter1 = tb.Meter(root,
                 bootstyle="primary",
                 subtext="Battery",
                 interactive=True,
                 textright='%',
                 subtextstyle='success',
                 amounttotal=100,
                 amountused=percent,
                 stripethickness=2,
                 )
meter1.pack(pady=20)

root.mainloop()