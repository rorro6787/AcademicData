import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def marks_by_subject(df, x_string, y_string, join_string, year:int, type_graph="bars", semester=None):
    df_subset = choose_year(df, year, semester)

    x = df_subset[x_string]
    y = pd.to_numeric(df_subset[y_string], errors='coerce')
    fields = df_subset[join_string]

    unique_fields = fields.unique()
    colors = sns.color_palette("husl", len(unique_fields))  
    field_color_map = dict(zip(unique_fields, colors))
    bar_colors = fields.map(field_color_map)
    
    fig, ax = plt.subplots()

    if(type_graph == "bars"):
        ax.bar(x, y, color=bar_colors)
        handles = [plt.Rectangle((0,0),1,1, color=field_color_map[field]) for field in unique_fields]
    elif(type_graph == "lines"):
        ax.plot(x, y, marker='o', linestyle='-', color='b', alpha=0.5)  
        for i, (subject, mark, color) in enumerate(zip(x, y, bar_colors)):
            ax.plot(subject, mark, marker='o', color=color, markersize=8)
        handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, linestyle='') for color in colors]

    ax.set_ylim(0, 10)
    ax.set_ylabel(y_string)
    if semester == None:
        ax.set_title('Marks by Subject Year ' + str(year))
    else:
        ax.set_title('Marks by Subject Year ' + str(year) + ' and Semester ' + str(semester))
    plt.xticks(rotation=45, ha='right', rotation_mode='default')

    ax.legend(handles, unique_fields, title=join_string)

    fig.tight_layout()
    plt.show()

def mean_year(df, year:int, semester=None):
    df_subset = choose_year(df, year, semester)
    mean_column = pd.to_numeric(df_subset['Mark'], errors='coerce').mean()
    return mean_column

def median_year(df, year:int, semester=None):
    df_subset = choose_year(df, year, semester)
    median_column = pd.to_numeric(df_subset['Mark'], errors='coerce').median()
    return median_column

def mode_year(df, year:int, semester=None):
    df_subset = choose_year(df, year, semester)
    mode_column = pd.to_numeric(df_subset['Mark'], errors='coerce').mode()
    return mode_column
    
def choose_year(df, year:int, semester=None):
    if semester == None:
        if year == 1:
            df = df.iloc[:10]
        elif year == 2:
            df = df.iloc[10:20]
        elif year == 3:
            df = df.iloc[20:30]
        else:
            df = df.iloc[30:40]
    else:
        if year == 1 and semester == 1:
            df = df.iloc[:5]
        elif year == 1 and semester == 2:
            df = df.iloc[5:10]
        elif year == 2 and semester == 1:
            df = df.iloc[10:15]
        elif year == 2 and semester == 2:
            df = df.iloc[15:20]
        elif year == 2 and semester == 1:
            df = df.iloc[20:25]
        elif year == 2 and semester == 2:
            df = df.iloc[25:30]
        elif year == 2 and semester == 1:
            df = df.iloc[30:35]
        else:
            df = df.iloc[35:40]
    return df

def main():
    df = pd.read_excel('dataset.xlsx')
    marks_by_subject(df, "Subject", "Mark", "Field", 1, type_graph="lines", semester=1)

if __name__ == "__main__":
    main()



