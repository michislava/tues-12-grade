for timestamp, value, color in zip(timestamps, values, colors):
    plt.plot([timestamp], [value], marker='o', linestyle='-', color=color, markeredgecolor='black', label='Sensor')
