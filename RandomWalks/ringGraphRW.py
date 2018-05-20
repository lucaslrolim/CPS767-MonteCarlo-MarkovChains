from markovChain import *
import matplotlib.pyplot as plt

states = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
lazy = 0.5
eps = pow(10,-6)

print("LIST OF STATES: ", states)

GraphMixtureResults = []
objs = [RingGraphRW(states[i],lazy) for i in range(len(states))]
for i in range(len(states)):
    GraphMixtureResults.append(objs[i].calculateMixingTime(eps))

print(GraphMixtureResults)
x_axis = states
y_axis = GraphMixtureResults
plt.plot(x_axis, y_axis, 'b-')
plt.savefig('ringRandomWalk.png')