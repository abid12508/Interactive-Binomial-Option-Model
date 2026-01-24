import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Binomobject.tree_Plot as co
import tkinter as tk
import tkinter.ttk as ttk
import math


#Update func
def update_plot(val=None):
    S0 = S_slider.get()
    u_rate = u_slider.get() / 100
    d_rate = d_slider.get() / 100
    steps = steps_slider.get()
    T = T_slider.get()
    global scatter
    scatter = co.calculations(S0, u_rate, d_rate, T, steps, ax, canvas, scatter)

#window and widgets
win = tk.Tk()

win.geometry("1600x800")
win.title("Interactive Binomial Tree Model")

control_frame = ttk.Frame(win)
control_frame.pack(side=tk.LEFT, padx=10, pady=10)

S_slider = tk.Scale(control_frame, from_=0, to=200, length=400, label="Starting Price", orient=tk.HORIZONTAL, command=update_plot)
S_slider.set(100)
S_slider.pack(side="top")

u_slider = tk.Scale(control_frame, from_=0, to=100, length=400, label="Up Rate (%)", orient=tk.HORIZONTAL, command=update_plot)
u_slider.set(20)
u_slider.pack(side="top")

d_slider = tk.Scale(control_frame, from_=0, to=100, length=400, label="Down Rate (%)", orient=tk.HORIZONTAL, command=update_plot)
d_slider.set(20)
d_slider.pack(side="top")

steps_slider = tk.Scale(control_frame, from_=1, to=12, length=400, label="Steps", orient=tk.HORIZONTAL, command=update_plot)
steps_slider.set(3)
steps_slider.pack(side="top")

T_slider = tk.Scale(control_frame, from_=0.1, to=10, length=400, resolution=0.1, label="Time to Expiration", orient=tk.HORIZONTAL, command=update_plot)
T_slider.set(1)
T_slider.pack(side="top")

#subplot for mpl
fig, ax = plt.subplots(figsize=(12,8))
canvas = FigureCanvasTkAgg(fig, master=win)
canvas.get_tk_widget().pack(side=tk.RIGHT)

#small box for each plot's info
annot = ax.annotate(
    "",
    xy=(0, 0),
    xytext=(10, 10),
    textcoords="offset points",
    bbox=dict(boxstyle="round", fc="w")
)
annot.set_visible(False)

def on_Hover(event):
    if event.inaxes != ax:
        annot.set_visible(False)
        canvas.draw_idle()
        return
    
    xdata, ydata = scatter.get_offsets().T
    if(len(xdata)==0): return

    distances = (xdata-event.xdata)**2 + (ydata - event.ydata)**2
    for i in range(len(distances)):
        distances[i] = math.sqrt(distances[i])
    idx = distances.argmin()
    colors = ['#FF4782'] * len(xdata)
    
    if distances[idx] < math.sqrt(5):
        annot.xy = [xdata[idx], ydata[idx]]
        colors[idx] = '#05A3FF'
        annot.set_text(f"Step: {int(xdata[idx])}\nPrice: {ydata[idx]:.2f}")
        annot.set_visible(True)
        canvas.draw_idle()
    else:
        annot.set_visible(False)
        canvas.draw_idle()
    scatter.set_facecolor(colors)

#Connect plot to tkinter and mainloop window
fig.canvas.mpl_connect("motion_notify_event", on_Hover)
scatter = ax.scatter([], [], color='#FF4782')
scatter = co.calculations(S_slider.get(), u_slider.get()/100, d_slider.get()/100, T_slider.get(), steps_slider.get(), ax, canvas, scatter)
win.mainloop()