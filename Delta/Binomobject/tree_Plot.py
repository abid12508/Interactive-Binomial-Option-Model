from collections import defaultdict
import math 
import numpy as np

#computations and tree creation
def calculations(starting_price, up_rate, down_rate, T, steps, ax, canvas, scatter):
    dt = T / steps
    u = math.exp(up_rate * math.sqrt(dt))
    d = math.exp(-down_rate * math.sqrt(dt))

    pricedict = defaultdict(list)
    current_prices = [starting_price]
    pricedict[0] = current_prices

    for step in range(1, steps+1):
        next_prices = []
        for price in current_prices:
            next_prices.extend([price*u, price*d])
        pricedict[step] = next_prices
        current_prices = next_prices

    scatter = sctr_Plot(steps, pricedict, ax, canvas, scatter)
    return scatter

#scatter plot with lines 
def sctr_Plot(steps, pricedict, ax, canvas, scatter):
    for line in ax.lines:
        line.remove()

    x, y = [], []
    for i in range(steps+1):
        for price in pricedict[i]:
            x.append(i)
            y.append(price)

    scatter.set_offsets(np.column_stack([x, y]))

    for i in range(steps):
        for j in range(len(pricedict[i])):
            y1 = pricedict[i][j]
            y2 = [pricedict[i+1][2*j], pricedict[i+1][2*j+1]]
            ax.plot([i+.01, i+.99], [y1-.1, y2[0]-.1], color='#FF4782', linewidth=.5)
            ax.plot([i+.01, i+.99], [y1-.1, y2[1]-.1], color='#FF4782', linewidth=.5)

    ax.set_xlabel("Step")
    ax.set_xlim(left=-0.1, right=max(x)+0.1)

    ax.set_ylabel("Price")
    ax.set_ylim(bottom=min(y)-2, top=max(y)+2)

    canvas.draw_idle()
    return scatter



