import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_random_points(num_points=1000):
    x_coords = np.random.randint(0, 1000, num_points)
    y_coords = np.random.randint(0, 1000, num_points)
    df = pd.DataFrame({'x': x_coords, 'y': y_coords})
    return df

def plot_points(df, size, filename):
    df['grid_x'] = (df['x'] // size) * size
    df['grid_y'] = (df['y'] // size) * size

    unique_grids = list(set(zip(df['grid_x'], df['grid_y'])))
    colors = plt.cm.get_cmap('tab20', len(unique_grids))

    color_map = {grid: colors(i) for i, grid in enumerate(unique_grids)}
    df['color'] = df.apply(lambda row: color_map[(row['grid_x'], row['grid_y'])], axis=1)

    plt.figure(figsize=(10, 10))
    plt.scatter(df['x'], df['y'], color=df['color'])
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.title(f'Rastgele Koordinatlar - {size}x{size} Izgara')
    plt.xlabel('X Koordinatları')
    plt.ylabel('Y Koordinatları')

    for i in range(0, 1001, size):
        plt.axhline(i, color='grey', linewidth=0.5)
        plt.axvline(i, color='grey', linewidth=0.5)

    plt.savefig(f'static/{filename}')
    plt.close()

def create_new_plot(size=100):
    df = generate_random_points()
    plot_points(df, size, 'plot.jpeg')
