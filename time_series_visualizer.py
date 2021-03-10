import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True)
df.set_index("date", inplace=True)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))] 

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(df)

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.DataFrame(df.copy()).reset_index()
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month_name()
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year

    # Draw bar plot    
    months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig, ax = plt.subplots(1, figsize=(8, 6))
    sns.barplot(x='year', y='value', hue='month', hue_order=months, data=df_bar, ci=None)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left', title='Months')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box.date, format='%Y-%m-%d')

    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(12,6), ncols=2)

    ax0 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    ax0.set_xlabel('Year')
    ax0.set_ylabel('Page Views')
    ax0.set_title('Year-wise Box Plot (Trend)')

    months = ['Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    ax1 = sns.boxplot(x='month', y='value', order=months, data=df_box, ax=axes[1])
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
