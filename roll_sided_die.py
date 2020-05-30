import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

number_of_sides = int(input('How many sides of the die are there?'))
number_of_rolls = int(input('How many rolls do you want to roll?'))

if number_of_sides >= 2:
    rolls = [random.randrange(1,number_of_sides) for i in range(number_of_rolls)]
    values, frequencies = np.unique(rolls, return_counts=True)
    title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=values, y = frequencies, palette= 'bright')

    axes.set_title(title)
    axes.set(xlabel='Die Value', ylabel = 'Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)

    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
        axes.text(text_x, text_y, text,
                  fontsize = 11, ha = 'center', va = 'bottom')

    plt.show()
 else:
    print('There has to be more than 1 side to the die')