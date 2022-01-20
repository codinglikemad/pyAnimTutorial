import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

# This needs to be changed for your code
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\spsha\\Desktop\\ffmpeg-4.4-full_build\\bin\\ffmpeg.exe'

# This is the final example I showed in the code - notice I have 2 "cursor marks" not shown in the video
fig = plt.figure()
l, = plt.plot([], [], 'k-')
l2, = plt.plot([], [], 'm--')
p1, = plt.plot([], [], 'ko')
p2, = plt.plot([], [], 'mo')

plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

def func(x):
    return np.sin(x)*3

def func2(x):
    return np.cos(x)*3

metadata = dict(title='Movie', artist='codinglikemad')
writer = FFMpegWriter(fps=15, metadata=metadata)


xlist = []
xlist2 = []
ylist = []
ylist2 = []

with writer.saving(fig, "sinWave2.mp4", 100):

    # Plot the first line and cursor
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))

        l.set_data(xlist,ylist)
        l2.set_data(xlist2,ylist2)

        p1.set_data(xval,func(xval))

        writer.grab_frame()

    # plot the second line and cursor
    for xval in np.linspace(-5,5,100):
        xlist2.append(xval)
        ylist2.append(func2(xval))

        l.set_data(xlist,ylist)
        l2.set_data(xlist2,ylist2)

        p2.set_data(xval,func2(xval))

        writer.grab_frame()
