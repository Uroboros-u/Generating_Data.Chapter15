"""15-1. Cubes: A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5,000 cubic numbers."""

import matplotlib.pyplot as plt

# values = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 125]
#
# fig , ax = plt.subplots()
# ax.plot(values, cubes)
# plt.show()


values2 = range(1, 5001)
cubes2 = [x**3 for x in values2]

plt.style.use('ggplot')
fig2, ax2 = plt.subplots()
ax2.plot(values2, cubes2)
ax2.set_title('Cube Numbers', fontsize=20)
ax2.set_xlabel('Number')
ax2.set_ylabel('Cube Number')
plt.show()

