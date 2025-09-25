"""Two D8s: Create a simulation showing what happens when you roll two
eight-sided dice 1,000 times. Try to picture what you think the visualization will
look like before you run the simulation, then see if your intuition was correct.
Gradually increase the number of rolls until you start to see the limits of your
system’s capabilities."""

import plotly.express as px

from d8 import Dice


die_1 = Dice(8)
die_2 = Dice(8)

results = []
frequencies = []
max_results = die_1.sides + die_2.sides

for roll in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
possible_res = range(2, max_results + 1)
for i in possible_res:
    frequency = results.count(i)
    frequencies.append(frequency)

title = "Results of Rolling two  D8, 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x= possible_res, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()