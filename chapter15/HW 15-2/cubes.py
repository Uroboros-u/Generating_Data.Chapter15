'''15-2. Colored Cubes: Apply a colormap to your cubes plot.'''

import matplotlib.pyplot as plt

number = range(1, 5001)
cubes = [x**3 for x in number]

plt.style.use('ggplot')
fig , ax = plt.subplots()
ax.scatter(number, cubes, c=cubes, cmap=plt.cm.get_cmap('magma'))
ax.set(xlabel='Number', ylabel='Cubes', title='Cubes')
plt.show()