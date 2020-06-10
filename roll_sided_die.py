from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    for i in range(rolls):
        frequencies[random.randrange(1,7) - 1] += 1
    
    plt.cla()

    axes = sns.barplot(x=values, y = frequencies, palette= 'bright')
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel = 'Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)

    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text,
    fontsize = 11, ha = 'center', va = 'bottom')

number_of_frames = int(input("How many rolls would you like?\n"))
rolls_per_frame = int(input("How many rolls per frame do you want?\n"))

sns.set_style('whitegrid')
figure = plt.figure('Rolling a Six-Sided Die')
values = list(range(1, 7))
frequencies = [0] * 6

die_animation = animation.FuncAnimation(
    figure, update, repeat = False, frames = number_of_frames - 1, interval = 33,
    fargs = (rolls_per_frame, values, frequencies))

plt.show()
