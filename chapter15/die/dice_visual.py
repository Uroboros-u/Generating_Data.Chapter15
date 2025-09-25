import plotly.express as px

from die import Die

die_1 = Die(6)
die_2 = Die(10)

results =[]

for roll in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_results = die_1.sides + die_2.sides
possible_results = range(2, max_results +1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=possible_results, y=frequencies)
fig.update_layout(xaxis_dtick=1)

fig.show()





