import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def marks_by_subject_bars(df, year:int):
    df_subset = choose_year(df, year)

    if year == 1:
        df_subset = df.iloc[:10]
    elif year == 2:
        df_subset = df.iloc[10:20]
    elif year == 3:
        df_subset = df.iloc[20:30]
    else:
        df_subset = df.iloc[30:40]

    x = df_subset['Subject']
    y = pd.to_numeric(df_subset['Mark'], errors='coerce')
    fields = df_subset['Field']

    unique_fields = fields.unique()
    colors = sns.color_palette("husl", len(unique_fields))  
    field_color_map = dict(zip(unique_fields, colors))
    bar_colors = fields.map(field_color_map)
    
    fig, ax = plt.subplots()
    ax.bar(x, y, color=bar_colors)

    ax.set_ylim(0, 10)
    ax.set_ylabel('Marks')
    ax.set_title('Marks by Subject Year ' + str(year))
    plt.xticks(rotation=45, ha='right', rotation_mode='default')  
    
    handles = [plt.Rectangle((0,0),1,1, color=field_color_map[field]) for field in unique_fields]
    ax.legend(handles, unique_fields, title='Field')

    fig.tight_layout()
    plt.show()

def marks_by_subject_lines(df, year:int):
    df_subset = choose_year(df, year)

    x = df_subset['Subject']
    y = pd.to_numeric(df_subset['Mark'], errors='coerce')
    fields = df_subset['Field']

    unique_fields = fields.unique()
    colors = sns.color_palette("husl", len(unique_fields))  
    field_color_map = dict(zip(unique_fields, colors))
    
    marker_colors = fields.map(field_color_map)
    
    fig, ax = plt.subplots()

    ax.plot(x, y, marker='o', linestyle='-', color='b', alpha=0.5)  

    for i, (subject, mark, color) in enumerate(zip(x, y, marker_colors)):
        ax.plot(subject, mark, marker='o', color=color, markersize=8)

    ax.set_ylim(0, 10)
    ax.set_ylabel('Marks')
    ax.set_title('Marks by Subject Year ' + str(year))
    plt.xticks(rotation=45, ha='right', rotation_mode='default')

    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, linestyle='') for color in colors]
    ax.legend(handles, unique_fields, title='Field')

    fig.tight_layout()
    plt.show()

def mean_year(df, year:int):
    df_subset = choose_year(df, year)
    media_columna = pd.to_numeric(df_subset['Mark'], errors='coerce').mean()
    print(media_columna)

def median_year(df, year:int):
    df_subset = choose_year(df, year)
    media_columna = pd.to_numeric(df_subset['Mark'], errors='coerce').median()
    print(media_columna)
    
def choose_year(df, year:int):
    if year == 1:
        df = df.iloc[:10]
    elif year == 2:
        df = df.iloc[10:20]
    elif year == 3:
        df = df.iloc[20:30]
    else:
        df = df.iloc[30:40]
    return df

def main():
    df = pd.read_excel('dataset.xlsx')
    marks_by_subject_lines(df, 1)

if __name__ == "__main__":
    main()



