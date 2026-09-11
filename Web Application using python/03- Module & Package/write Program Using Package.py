import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y=[2,4,6,8,10]

# Bar Chart
plt.bar(x, y, color='blue' , label='Bar Chart')


# Scatter Plot
plt.scatter(x, y, color='red', label='Scatter Plot')

# Labels and Title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Bar Chart and Scatter Plot')

# Legend
plt.legend()

# Show the plot
plt.show()