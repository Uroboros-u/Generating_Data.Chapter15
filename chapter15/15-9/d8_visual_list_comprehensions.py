"""15-9. Die Comprehensions: For clarity, the listings in this section use the long
form of for loops. If you’re comfortable using list comprehensions, try writing a
comprehension for one or both of the loops."""

import plotly.express as px

from d8 import Dice


die_1 = Dice(8)
die_2 = Dice(8)

results = []
frequencies = []
max_results = die_1.sides + die_2.sides

results = [die_1.roll() + die_2.roll() for x in range(1000)]
possible_res = range(2, max_results + 1)
frequencies = [results.count(x) for x in possible_res]

title = "Results of Rolling two  D8, 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x= possible_res, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()