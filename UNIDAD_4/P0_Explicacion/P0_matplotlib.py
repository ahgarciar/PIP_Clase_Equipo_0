
x = [i for i in range(10)]
print(x)

y = [i**2 for i in x]
print(y)


from matplotlib import pyplot as plt

plt.plot(x,y)
plt.show()