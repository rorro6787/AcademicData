import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def marks_by_subject(df, type_graph="bars", year=1, semester=None):
    df_subset = choose_year(df, year, semester)

    x = df_subset["Subject"]
    y = pd.to_numeric(df_subset["Mark"], errors='coerce')
    fields = df_subset["Field"]

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
    ax.set_ylabel("Mark")
    if semester == None:
        ax.set_title('Marks by Subject Year ' + str(year))
    else:
        ax.set_title('Marks by Subject Year ' + str(year) + ' and Semester ' + str(semester))
    plt.xticks(rotation=45, ha='right', rotation_mode='default')

    ax.legend(handles, unique_fields, title="Fielf")

    fig.tight_layout()
    plt.show()

def credit_percentage_type(df):
    type_credits = df.groupby('Type')['Credits'].sum()

    total_credits = type_credits.sum()
    type_percentage = (type_credits / total_credits) * 100

    plt.figure(figsize=(8, 8))
    pie_chart = type_percentage.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3', labels=['']*len(type_percentage))

    plt.legend(pie_chart.patches, type_percentage.index, title="Type", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title('Credit Distribution in % by Type')
    plt.ylabel('') 
    plt.show()

def credit_total_type(df):
    credits_by_type = df.groupby('Type')['Credits'].sum()

    plt.figure(figsize=(10, 6))
    credits_by_type.plot(kind='bar', color='lightgreen')

    plt.title('Total Number of Credits per Subject Type')
    plt.xlabel('Type')
    plt.ylabel('Total Number of Credits')
    plt.xticks(rotation=45, ha='right', rotation_mode='default')

    for i, v in enumerate(credits_by_type):
        plt.text(i, v + 1, f'{v}', ha='center', va='bottom')

    plt.show()

def credit_passed_type(df):
    df_approved = df[df['Mark'] != '-']

    approved_credits_by_type = df_approved.groupby('Type')['Credits'].sum()
    total_credits_by_type = df.groupby('Type')['Credits'].sum()
    percentage_approved_credits = (approved_credits_by_type / total_credits_by_type) * 100

    plt.figure(figsize=(10, 6))
    percentage_approved_credits.plot(kind='bar', color='skyblue')

    plt.title('% Distribution of Approved Credits by Type')
    plt.xlabel('Type')
    plt.ylabel('Approval % of Credits')

    plt.xticks(rotation=45, ha='right', rotation_mode='default')

    for i, v in enumerate(percentage_approved_credits):
        plt.text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom')

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
    # marks_by_subject(df, type_graph="bars", year=1)
    credit_total_type(df)

if __name__ == "__main__":
    main()



