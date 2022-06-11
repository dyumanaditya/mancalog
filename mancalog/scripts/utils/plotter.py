import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    sns.set()
    mode = 'timesteps'
    smooth = True
    data_path = f'/home/dyuman/Documents/Mancalog/profiling/profile_{mode}.csv'

    headers = [f'Number of {mode}', 'Time']
    df = pd.read_csv(data_path, names=headers, header=None)
    x = df[f'Number of {mode}']
    y = df['Time']
    
    if smooth:
        y = pd.Series(y).rolling(15, min_periods=1).mean()
    ax = sns.lineplot(x=x, y=y, ci=95)
    ax.axes.set_title(f'Number of {mode} vs Time', fontsize=18)
    ax.set_xlabel(f'Number of {mode}', fontsize=13)
    ax.set_ylabel('Time (seconds)', fontsize=13)
    if smooth:
        plt.savefig(f'{mode}_vs_time_smooth.png')
    else:
        plt.savefig(f'{mode}_vs_time.png')


if __name__ == '__main__':
    main()
