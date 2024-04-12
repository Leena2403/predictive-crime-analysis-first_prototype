import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

def plot_top_crimes_per_unit(df, unit_name_column, value):
    # Filter DataFrame based on the specific value of unit_name_column
    df_filtered = df[df[unit_name_column] == value]

    if df_filtered.empty:
        st.write(f"No data available for {value}.")
        return

    # Calculate top 15 crimes for the specified unit
    category_counts = df_filtered['CrimeGroup_Name'].value_counts().head(15)
    data = {'Crime Group': category_counts.index, 'Total_crimes': category_counts.values}
    count_df = pd.DataFrame(data)

    # Plotting
    plt.figure(figsize=(12, 6))
    ax = category_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.title(f"Top 15 Crimes for {value}")
    plt.xticks(rotation=45)

    max_count_index = category_counts.idxmax()
    bars = ax.patches
    for i in range(len(bars)):
        if i == category_counts.index.get_loc(max_count_index):
            bars[i].set_color('red')

    for i, count in enumerate(category_counts):
        ax.text(i, count + 0.5, str(count), ha='center', va='bottom')

    # Display plot and DataFrame using Streamlit
    st.pyplot(plt)
    st.dataframe(count_df)

# Example usage:
# Assuming 'fir' is your DataFrame containing crime data
# plot_top_crimes_per_unit(fir, 'unit name', 'Amengad PS')


import calendar

def crime_per_month_beat_wise(crimes, dataset, beat_name):
    if not crimes:
        st.write("No crime selected.")
        return

    crime_data = dataset[dataset['CrimeGroup_Name'] == crimes]
    crime_data = crime_data[crime_data['Beat_Name'] == beat_name]

    st.write("Filtered Crime Data:")
    st.write(crime_data)

    crime_data_grouped = crime_data.groupby('Month').size().reset_index(name='Frequency')

    total_freq = crime_data_grouped['Frequency'].sum()

    monthly = crime_data_grouped.groupby('Month')['Frequency'].sum()
    sorted_months = monthly.sort_values(ascending=False).index

    top_months = [calendar.month_name[month] for month in sorted_months[:3]]

    st.write("Top Months:")
    st.write(top_months)

    analysis_text = f"The crime '{crimes}' in beat '{beat_name}' is likely to occur more frequently in the months of {', '.join(top_months)}."
    st.write(analysis_text)

    # Line chart
    chart = alt.Chart(crime_data_grouped).mark_line().encode(
        x='Month:T',  # Assuming 'Month' is datetime column
        y='Frequency:Q',
        tooltip=['Month:T', 'Frequency:Q']
    ).properties(
        width=800,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

## Crime counts per beat!

def plot_crime_counts_by_beat(dataset, beat_name):
    category_counts = dataset.loc[dataset['Beat_Name'] == beat_name, 'Year'].value_counts().sort_index()
    data = {'Year': category_counts.index, 'Total_crimes': category_counts.values}
    count_df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(category_counts.index, category_counts.values, color='skyblue')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Count')
    ax.set_title(f"Crime Counts for Beat: {beat_name}")
    ax.set_xticks(category_counts.index)
    ax.set_xticklabels(category_counts.index, rotation=45)

    max_count_index = category_counts.idxmax()
    for i, count in enumerate(category_counts):
        if category_counts.index[i] == max_count_index:
            ax.get_children()[i].set_color('red')
        ax.text(i, count + 0.5, str(count), ha='center', va='bottom')

    st.pyplot(fig)
    st.dataframe(count_df)

# Example usage:
# Assuming 'dataset' is your DataFrame and 'beat_name' is the selected beat name
# plot_crime_counts_by_beat(dataset, beat_name)


## Top time instants [Offence_From_Date] [Offence To Data]
def top_time_instants_count(dataset, column, top_n=10):
    dataset = dataset.drop(dataset.index[0])

    top_time_instants = dataset[column].value_counts().head(top_n)

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(x=column, data=dataset[dataset[column].isin(top_time_instants.index)],
                  palette='viridis', ax=ax)
    ax.set_title(f'Top {top_n} Count of Time Instants: {column}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)

    # Display the plot using Streamlit
    st.pyplot(fig)









