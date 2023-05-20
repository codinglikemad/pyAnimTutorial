import numpy as np
import matplotlib
# matplotlib.use("Agg") # You can uncomment this line to have a totally non-gui experience - useful for webserver use where the file is rendered and shown to a user.
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, PillowWriter

# This will need to be changed to match your directory.
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\spsha\\Desktop\\ffmpeg-4.4-full_build\\bin\\ffmpeg.exe'

# To make sure your example looks like mine, set the random seed. Helps with fine tuning the graph too.
np.random.seed(102434201)

metadata = dict(title='Movie', artist='codinglikemad')
# writer = PillowWriter(fps=15, metadata=metadata)
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
plt.xlim(-8, 8)
plt.ylim(-8, 8)

# Generate some random linear data to fit:
def func(x):
    return x*1.2 + 0.1 + np.random.normal(0,2, x.shape)

x = np.random.uniform(-7,7,10)
x = np.sort(x) # Sort the x values here so we get a nice left to right progression in the animation
y = func(x)

coeff = np.polyfit(x,y,1)
print(coeff)
xline = np.linspace(-6,6,40) # This controls how long the animation takes below.
yline = np.polyval(coeff, xline)

lPnt, = plt.plot(x, y, 'o')
l, = plt.plot(xline, yline, 'k-', linewidth=3)

plt.show()
# You need to close the figure for the 2nd half of the script to run - remove the plotting above if you want to generate without intervention.


fig = plt.figure()
plt.xlim(-10, 10)
plt.ylim(-10, 10)

lPnt, = plt.plot([], [], 'o')
l, = plt.plot([], [], 'k-', linewidth=3)

xLineList = []
yLineList = []

xPntList = []
yPntList = []

# We generate each plot sequentially here
with writer.saving(fig, "fitPlot.mp4", 100):

    # First show the data points
    for xval,yval in zip(x,y):

        xPntList.append(xval)
        yPntList.append(yval)

        lPnt.set_data(xPntList,yPntList)
        l.set_data(xLineList,yLineList)

        # Double up the frames to slow things down a bit here.
        writer.grab_frame()
        writer.grab_frame()

    # Add the line fit
    for xval,yval in zip(xline,yline):

        xLineList.append(xval)
        yLineList.append(yval)

        lPnt.set_data(xPntList,yPntList)
        l.set_data(xLineList,yLineList)

        writer.grab_frame()

    # We pad at the end to create some "pauseing space"
    for ii in range(10):
        writer.grab_frame()
