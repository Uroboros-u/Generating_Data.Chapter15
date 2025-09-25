import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(dpi=128)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth= 1, color='gray')
ax.set_aspect('equal')

ax.scatter(0,0, c='red', s=30)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=30)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()