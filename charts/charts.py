import matplotlib.pyplot as plt


def generate_pie_char():
    labels = ['A','B','C']
    values = ['120','140','160']

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()