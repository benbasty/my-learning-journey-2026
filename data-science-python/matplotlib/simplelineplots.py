import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

#we start creating a figure and axes.
#in their simplest form
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
apns = ax.plot(x, np.sin(x));
ppns = plt.plot(x, np.sin(x));
ppnc = plt.plot(x, np.cos(x));

# Adjusting the Plot: Line Colors and Styles
ppncb = plt.plot(x, np.sin(x - 0), color='blue') #specify color by name
# we can also specify color nname by short color code, grayscale between 0 and 1, hex code, rgb, or html color names

# adjusting the linestyle
ppxl = plt.plot(x, x + 0, linestyle='solid')
# linestyle can also be dashed,dashdot, dotted
# or u can also use these codes: '-' solid, '--' dashed, '-.' dashdot, ':' dotted

# u can combinne both colors and linestyles as well
plt.plot(x, x + 0, '-g') # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r'); # dotted red

# Adjusting the Plot: Axes Limits

# if u want to have control over the axes limits of your plots,
# the most basic way to adjust the limits is to use plt.xlim, plt.ylim functions

plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);

# another method is plt.axis to have more qualitatibe specifications for axis limits
# you can tighten the bounds around the content for example
plt.plot(x, np.sin(x))
plt.axis('tight');

# you can specify that you want equal axis ratio: one unit in x is visually equal to one unit in y
plt.plot(x, np.sin(x))
plt.axis('equal');

# labelling plots
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");






