import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_GPA(means, mean_expedient):
    years = ['Year 1', 'Year 2', 'Year 3', 'Year 4']

    plt.figure(figsize=(10, 6))
    plt.bar(years, means, color='blue', label='Mean Year')
    plt.bar('GPA', mean_expedient, color='green', label='Median Expedient')

    plt.axhline(y=mean_expedient, color='red', linestyle='--', label='GPA')

    plt.title('GPA over the Years')
    plt.ylabel('Mean Value')
    #plt.yticks(range(0, 10, 1))  
    plt.yticks(np.arange(0, 10, 0.5))  
    plt.legend()
    plt.show()

def marks_by_subject(df, type_graph="bars", year=0, semester=None):
    df_subset = choose_year(df, year, semester)

    x = df_subset["Subject"]
    y = pd.to_numeric(df_subset["Mark"], errors='coerce')
    fields = df_subset["Field"]

    unique_fields = fields.unique()
    colors = sns.color_palette("husl", len(unique_fields))  
    field_color_map = dict(zip(unique_fields, colors))
    bar_colors = fields.map(field_color_map)
    
    sns.set_style("darkgrid")
    plt.rcParams.update({
        "axes.facecolor": "#A8B8C5", 
        "figure.facecolor": "#141321",
        "axes.labelcolor": "white",
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.edgecolor": "white",
        "grid.color": "#555555"
    })

    fig, ax = plt.subplots(figsize=(30, 12))

    if(type_graph == "bars"):
        ax.bar(x, y, color=bar_colors)
        handles = [plt.Rectangle((0,0),1,1, color=field_color_map[field]) for field in unique_fields]
    elif(type_graph == "lines"):
        ax.plot(x, y, marker='o', linestyle='-', color='b', alpha=0.5)  
        for i, (subject, mark, color) in enumerate(zip(x, y, bar_colors)):
            ax.plot(subject, mark, marker='o', color=color, markersize=8)
        handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, linestyle='') for color in colors]

    ax.set_ylim(0, 10)
    ax.set_ylabel("Mark", fontsize=20)
    if year < 1 or year > 4:
        ax.set_title('Marks by Subject in the Degree', fontsize=24)
    else:
        if semester == None:
            ax.set_title('Marks by Subject Year ' + str(year), fontsize=24)
        else:
            ax.set_title('Marks by Subject Year ' + str(year) + ' and Semester ' + str(semester), fontsize=24)
    plt.xticks(rotation=45, ha='right', rotation_mode='default', fontsize=16)
    plt.yticks(fontsize=16)

    ax.legend(handles, unique_fields, title="Field", fontsize=16, title_fontsize='20')

    fig.tight_layout()
    plt.show()
    
    # fig.savefig("graph marks", dpi=300, bbox_inches='tight')
    # plt.close(fig)  # Close the figure to free up memory

def credit_percentage_type(df):
    type_credits = df.groupby('Type')['Credits'].sum()

    total_credits = type_credits.sum()
    type_percentage = (type_credits / total_credits) * 100

    sns.set_style("darkgrid")
    plt.rcParams.update({
        "axes.facecolor": "#A8B8C5", 
        "figure.facecolor": "#A8B8C5",
        "axes.labelcolor": "white",
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.edgecolor": "white",
        "grid.color": "#555555"
    })

    plt.figure(figsize=(8, 8))
    pie_chart = type_percentage.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3', labels=['']*len(type_percentage))

    plt.legend(pie_chart.patches, type_percentage.index, title="Type", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title('Credit Distribution in % by Type')
    plt.ylabel('') 
    plt.show()

def credit_total_type(df):
    credits_by_type = df.groupby('Type')['Credits'].sum()

    sns.set_style("darkgrid")
    plt.rcParams.update({
        "axes.facecolor": "#A8B8C5", 
        "figure.facecolor": "#141321",
        "axes.labelcolor": "white",
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.edgecolor": "white",
        "grid.color": "#555555"
    })

    plt.figure(figsize=(10, 4))
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

    sns.set_style("darkgrid")
    plt.rcParams.update({
        "axes.facecolor": "#A8B8C5", 
        "figure.facecolor": "#141321",
        "axes.labelcolor": "white",
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.edgecolor": "white",
        "grid.color": "#555555"
    })

    plt.figure(figsize=(10, 4))
    percentage_approved_credits.plot(kind='bar', color='skyblue')

    plt.title('% Distribution of Approved Credits by Type')
    plt.xlabel('Type')
    plt.ylabel('Approval % of Credits')

    plt.xticks(rotation=45, ha='right', rotation_mode='default')

    for i, v in enumerate(percentage_approved_credits):
        plt.text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom')

    plt.show()

def credit_percentage_denomination(df):
    type_credits = df.groupby('Denomination')['Credits'].sum()

    total_credits = type_credits.sum()
    type_percentage = (type_credits / total_credits) * 100

    sns.set_style("darkgrid")
    plt.rcParams.update({
        "axes.facecolor": "#A8B8C5", 
        "figure.facecolor": "#A8B8C5",
        "axes.labelcolor": "white",
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.edgecolor": "white",
        "grid.color": "#555555"
    })

    plt.figure(figsize=(8, 8))
    pie_chart = type_percentage.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3', labels=['']*len(type_percentage))

    plt.legend(pie_chart.patches, type_percentage.index, title="Denomination", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title('Credit Distribution in % by Type')
    plt.ylabel('') 
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
    if year < 1 or year > 4:
        return df
    start_row = (year - 1) * 10
    if semester is not None:
        start_row += (semester - 1) * 5
        end_row = start_row + 5
    else:
        end_row = start_row + 10
    df = df.iloc[start_row:end_row]
    return df

def main():
    df = pd.read_excel('dataset.xlsx')
    marks_by_subject(df, type_graph="bars", year=3, semester=2)
    # credit_passed_type(df)
    # credit_percentage_type(df)
    # credit_total_type(df)

if __name__ == "__main__":
    main()



