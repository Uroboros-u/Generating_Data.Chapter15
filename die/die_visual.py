import plotly.express as px

from die import Die

die = Die()

results =[]

for roll in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []

possible_results = range(1, die.sides + 1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=possible_results, y=frequencies)
fig.show()





