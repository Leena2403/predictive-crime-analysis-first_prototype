import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import warnings
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
from shapely.geometry import Point
from sklearn.preprocessing import LabelEncoder

import crime_prediction as cp
import vulnerable_spots as vs
import criminal_prediction as c_pred
import beat_analysis as beat

# Load data
fir = pd.read_csv('Datasets/FIR_Details_Data.csv')
accused = pd.read_csv('Datasets/AccusedData (1).csv')
victim = pd.read_csv('Datasets/VictimInfoDetails (1).csv')
fir_short = fir[fir['Year']==2023]

le = LabelEncoder()
fir['Unit_ID'] = le.fit_transform(fir['Unit_ID'])

# Preprocessing

mapping_dict = {
    'POCSO': 'POCSO',
    'KARNATAKA POLICE ACT 1963': 'KP Act',
    'MOTOR VEHICLE ACCIDENTS NON-FATAL': 'Vehicle Accidents (NF)',
    'MOTOR VEHICLE ACCIDENTS FATAL': 'Vehicle Accidents (F)',
    'THEFT': 'Theft',
    'CrPC': 'CrPC',
    'CRUELTY BY HUSBAND': 'Domestic Violence',
    'ATTEMPT TO MURDER': 'Attempted Murder',
    'CHEATING': 'Cheating',
    'Karnataka State Local Act': 'KSL Act',
    'ELECTION': 'Election Offenses',
    ' REPRESENTATION OF PEOPLE ACT 1951 & 1988': 'RoP Act',
    'MOLESTATION': 'Molestation',
    'MISSING PERSON': 'Missing',
    'CASES OF HURT': 'Assault',
    'FORGERY': 'Forgery',
    'SCHEDULED CASTE AND THE SCHEDULED TRIBES ': 'ST/SC',
    'BURGLARY - NIGHT': 'Night Burglary',
    'NEGLIGENT ACT': 'Negligence',
    'MURDER': 'Murder',
    'RIOTS': 'Riots',
    'Attempting to commit offences': 'Attempted Offenses',
    'KIDNAPPING AND ABDUCTION': 'Kidnapping',
    'EXPLOSIVES': 'Explosives',
    'EXPOSURE AND ABANDONMENT OF CHILD': 'Child Abandonment',
    'ARSON': 'Arson',
    'CONSUMER': 'Consumer Offenses',
    'OFFENCES AGAINST PUBLIC SERVANTS (Public servant is a victim)': 'Offenses against Public Servants',
    'CRIMES RELATED TO WOMEN': 'Crimes against Women',
    'DEATHS DUE TO RASHNESS/NEGLIGENCE': 'Deaths due to Negligence',
    'COMMUNAL / RELIGION   ': 'Communal/Religious',
    'DOWRY DEATHS': 'Dowry Deaths',
    'CRIMINAL BREACH OF TRUST': 'Breach of Trust',
    'DACOITY': 'Dacoity',
    ' PREVENTION OF DAMAGE TO PUBLIC PROPERTY ACT 1984': 'Public Property Damage',
    'BURGLARY - DAY': 'Daytime Burglary',
    'ANIMAL': 'Animal Offenses',
    'MISCHIEF': 'Mischief',
    'INSULTING MODESTY OF WOMEN (EVE TEASING)': 'Eve Teasing',
    'CRIMINAL TRESPASS': 'Criminal Trespass',
    'CRIMINAL INTIMIDATION': 'Criminal Intimidation',
    'CRIMINAL CONSPIRACY': 'Conspiracy',
    'SUICIDE': 'Suicide',
    'NARCOTIC DRUGS & PSHYCOTROPIC SUBSTANCES': 'Drug Crime',
    'PUBLIC SAFETY': 'Public Safety',
    'CHILDREN ACT': 'Child Crime',
    'ROBBERY': 'Robbery',
    'RAPE': 'Rape',
    'ANTIQUES (CULTURAL PROPERTY)': 'Antiques',
    ' CYBER CRIME': 'Cybercrime',
    'Concealment of birth by secret disposal of Child': 'Concealment of Birth',
    'FOREST': 'Forest Crimes',
    'AFFRAY': 'Affray',
    'CULPABLE HOMICIDE NOT AMOUNTING TO MURDER': 'Culpable Homicide',
    'DEFAMATION': 'Defamation',
    'ATTEMPT TO CULPABLE HOMICIDE NOT AMOUNTING TO MURDER': 'Attempted Culpable Homicide',
    'WRONGFUL RESTRAINT/CONFINEMENT': 'Wrongful Confinement',
    'COTPA, CIGARETTES AND OTHER TOBACCO PRODUCTS': 'Tobacco Crime',
    'CRIMINAL MISAPPROPRIATION ': 'Misappropriation',
    'ASSAULT OR USE OF CRIMINAL FORCE TO DISROBE WOMAN': 'Assault on Women',
    'Disobedience to Order Promulgated by PublicServan': 'Disobedience to Public Servant',
    'UNNATURAL SEX ': 'Unnatural Sex',
    'POISONING-PROFESSIONAL': 'Professional Poisoning',
    'ASSAULT': 'Assault',
    'ARMS ACT  1959': 'Arms Act',
    'SEDITION': 'Sedition',
    'COPY RIGHT ACT 1957': 'Copyright Violations',
    'OF ABETMENT': 'Abetment',
    'OFFENCES RELATED TO MARRIAGE': 'Marraige Offenses',
    'PUBLIC NUISANCE': 'Public Nuisance',
    'FAILURE TO APPEAR TO COURT': 'Failure to Appear in Court',
    'ADULTERATION': 'Adulteration',
    ' POST & TELEGRAPH,TELEGRAPH WIRES(UNLAWFUL POSSESSION)ACT 1950': 'Unlawful Possession of Telegraph Wires',
    'IMPERSONATION ': 'Impersonation',
    'PUBLIC JUSTICE': 'Obstruction of Justice',
    'OFFENCES PROMOTING ENEMITY': 'Offenses promoting Enmity',
    'INDIAN MOTOR VEHICLE': 'IMV Act',
    'COUNTERFEITING': 'Counterfeiting',
    'DEATHS-MISCARRIAGE': 'Miscarriage Deaths',
    'PORNOGRAPHY': 'Pornography',
    'IMMORAL TRAFFIC': 'Immoral Trafficking',
    'FALSE EVIDENCE': 'False Evidence',
    'BONDED LABOUR SYSTEM': 'Bonded Labor',
    'ESCAPE FROM LAWFUL CUSTODY AND RESISTANCE': 'Escape from Custody',
    'PASSPORT ACT': 'Passport Act',
    'Human Trafficking': 'Human Trafficking',
    'OFFENCES BY PUBLIC SERVANTS (EXCEPT CORRUPTION) (Public servant is accused)': 'Offenses by Public Servants',
    'SLAVERY': 'Slavery',
    'Giving false information respecting an offence com': 'False Information',
    'FOREIGNER': 'Offenses by Foreigners',
    'RECEIVING OF STOLEN PROPERTY': 'Receiving Stolen Property',
    'OFFICIAL SECURITY RELATED ACTS': 'Security Offenses',
    'UNLAWFUL ACTIVITIES(Prevention)ACT 1967 ': 'Unlawful Activities',
    'UNNATURAL DEATH (Sec 174/174c/176)': 'Unnatural Death',
    'CINEMATOGRAPH ACT 1952': 'Cinematograph Act',
    'DOCUMENTS & PROPERTY MARKS': 'Document/Property Fraud',
    'DEFENCE FORCES OFFENCES RELATING TO (also relating to desertion)': 'Defense Forces Offenses',
    'INDIAN ELECTRICITY ACT ': 'Indian Electricity Act',
    'PREVENTION OF CORRUPTION ACT 1988': 'PoC Act',
    'INFANTICIDE': 'Infanticide',
    'NATIONAL SECURITY ACT': 'National Security Act',
    'ILLEGAL DETENTION': 'Illegal Detention',
    'RAILWAYS ACT': 'Railways Act',
    'OFFENCES AGAINST STATE': 'Offenses against State',
    'CIVIL RIGHTS ': 'Civil Rights Violation',
    'FAILURE TO APPEAR TO COURT': 'Failure to Appear in Court',
    'BUYING & SELLING MINOR FOR PROSTITUTION': 'Minor Prostitution'
}

# Replace the values in the 'CrimeGroup_Name' column using the mapping dictionary
fir['CrimeGroup_Name'] = fir['CrimeGroup_Name'].map(mapping_dict)


def crime_per_year_district(district, year, df):
    data = df[(df['Year'] == year) & (df['District_Name'] == district)]
    crime_counts = data['CrimeGroup_Name'].value_counts().head(17)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(crime_counts.index, crime_counts.values, color='seagreen')
    ax.set_title("Top Crimes in {} during {}".format(district, year))
    ax.set_xlabel("Top Crimes", fontsize=20)
    ax.set_ylabel("Frequency of Crimes", fontsize=20)
    ax.tick_params(axis='x', rotation=90)
    ax.grid(True)
    st.pyplot(fig)

def crime_per_year(year, df=fir):
    data = df[df['Year'] == year]
    crime_counts = data['CrimeGroup_Name'].value_counts().head(17)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(crime_counts.index, crime_counts.values, color='seagreen')
    ax.set_title("Frequency of Crimes in {}".format(year))
    ax.set_xlabel("Top Crimes", fontsize=20)
    ax.set_ylabel("Frequency of Crimes", fontsize=20)
    ax.tick_params(axis='x', rotation=90)
    ax.grid(True)
    st.pyplot(fig)

def plot_temporal_separate(df, label):
    crime_groups = df.groupby(['CrimeGroup_Name', label]).size().reset_index(name='Frequency')
    top_15_crime_groups = crime_groups.groupby('CrimeGroup_Name')['Frequency'].sum().nlargest(15).index
    crime_groups_filtered = crime_groups[crime_groups['CrimeGroup_Name'].isin(top_15_crime_groups)]

    for crime_group in top_15_crime_groups:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_title(f"Frequency of {crime_group} by {label}", fontsize=15)

        crime_group_data = crime_groups_filtered[crime_groups_filtered['CrimeGroup_Name'] == crime_group]

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sns.lineplot(data=crime_group_data, x=label, y='Frequency', ax=ax)

        ax.set_xlabel(label.capitalize(), fontsize=20)
        ax.set_ylabel("Frequency of Crimes", fontsize=20)
        ax.tick_params(axis='x', rotation=90)
        ax.grid(True)

        # Display the plot in Streamlit
        st.pyplot(fig)

def crime_per_month_beat_wise(crimes, dataset, beat_name):
    if not crimes:
        print("No crime selected.")
        return

    import calendar

    for crime in crimes:
        crime_data = dataset[dataset['CrimeGroup_Name'] == crime]
        crime_data = crime_data[crime_data['Beat_Name'] == beat_name]

        print("Filtered Crime Data:")
        print(crime_data)

        # Plotting or any other analysis you want to perform for each crime
        plot_temporal_separate(crime_data, 'Month')

        crime_data_grouped = crime_data.groupby('Month').size().reset_index(name='Frequency')

        total_freq = crime_data_grouped['Frequency'].sum()
        monthly = crime_data_grouped.groupby('Month')['Frequency'].sum()

        sorted_months = monthly.sort_values(ascending=False).index

        # month numbers to month names
        top_months = [calendar.month_name[month] for month in sorted_months[:3]]

        print("Top Months:")
        print(top_months)

        analysis_text = f"The crime '{crime}' in beat '{beat_name}' is likely to occur more frequently in the months of {', '.join(top_months)}."
        print(analysis_text)

## Top 10 vulnerable details
def find_vulnerable_victims_pivot(crime, dataset):
    crime_data = dataset[dataset['Crime_No'] == crime]

    if crime_data.empty:
        return "No victim found for the given crime number"

    top_victims = crime_data['Victim_ID'].value_counts().head(5)

    victim_details = dataset[dataset['Victim_ID'].isin(top_victims.index)]

    pivot_table = pd.pivot_table(victim_details,
                                 values=['age'],
                                 index=['Sex', 'Profession', 'Caste'],
                                 aggfunc={'age': 'count'})

    pivot_table = pivot_table.sort_values(by='age', ascending=False)
    pivot_table_top_10 = pivot_table.head(10)

    # Display the pivot table in Streamlit app
    st.write("Top 10 Vulnerable Victims:")
    st.dataframe(pivot_table_top_10)

## Top crime related instances
def find_accused_pivot(crime, dataset):
    crime_data = dataset[dataset['CrimeGroup_Name'] == crime]

    if crime_data.empty:
        return "No victim found for the given crime number"

    top_criminals = crime_data['FIR_ID'].value_counts().head(5)

    criminal_details = dataset[dataset['FIR_ID'].isin(top_criminals.index)]

    pivot_table = pd.pivot_table(criminal_details,
                                 values=['Place of Offence'],
                                 index=['Beat_Name', 'Distance from PS', 'Month'],
                                 aggfunc={'Place of Offence': 'count'})

    pivot_table = pivot_table.sort_values(by='Place of Offence', ascending=False)

    pivot_table_top_10 = pivot_table.head(10)

    st.write("Top 10 Accused Pivot:")
    st.dataframe(pivot_table_top_10)

def find_accused_victim_pivot(crime, dataset):
    crime_data = dataset[dataset['crime_no'] == crime]

    if crime_data.empty:
        return "No accused found for the given crime number"

    top_accused = crime_data['Arr_ID'].value_counts().head(10)

    accused_details = dataset[dataset['Arr_ID'].isin(top_accused.index)]

    accused_age_counts = accused_details.groupby('Arr_ID')['age'].value_counts().reset_index(name='count')

    top_accused_age_counts = accused_age_counts.groupby('Arr_ID')['count'].sum().sort_values(ascending=False).head(10)

    top_10_accused_mean_age = accused_age_counts[accused_age_counts['Arr_ID'].isin(top_accused_age_counts.index)].groupby('Arr_ID')['age'].mean()

    # Create DataFrame with top accused and their mean ages
    top_10_accused_df = pd.DataFrame(
        {'Arr_ID': top_10_accused_mean_age.index, 'Mean_Age': top_10_accused_mean_age.values})

    # Merge with original details to get additional information
    top_10_accused_info = pd.merge(top_10_accused_df, accused_details.drop_duplicates('Arr_ID'), on='Arr_ID')

    # Display the top 10 accused with their mean ages
    st.write("Top 10 Accused based on Crime Number:")
    st.dataframe(top_10_accused_info)


# Example usage:
# top_accused = find_accused_victim_pivot(crime, dataset)


lat_locators = {
    'Bagalkot':16.1850,
    'Ballari':15.1394,
    'Belagavi City':15.8497,
    'Belagavi Dist':16.1681,
    'Bengaluru City':12.9716,
    'Bengaluru Dist':12.58207912,
    'Bidar':17.9104,
    'Chamarajanagar':11.9261,
    'Chickballapura':13.4355,
    'Chikkamagaluru':13.3161,
    'Chitradurga':14.2251,
    'CID':12.9814,
    'Coastal Security Police':14.830648,
    'Dakshina Kannada':12.8438,
    'Davanagere':14.4644,
    'Dharwad':15.4589,
    'Gadag':15.4315,
    'Hassan':13.0033,
    'Haveri':14.7951,
    'Hubballi Dharwad City':15.3647,
    'ISD Bengaluru':12.9688,
    'K.G.F':12.9585,
    'Kalaburagi':17.3297
    }
long_locators = {
    'Bagalkot':75.700,
    'Ballari':76.9214,
    'Belagavi City':74.4977,
    'Belagavi Dist':74.7805,
    'Bengaluru City':77.5946,
    'Bengaluru Dist':77.34503148,
    'Bidar':77.5199,
    'Chamarajanagar':76.9437,
    'Chickballapura':77.7315,
    'Chikkamagaluru':75.7720,
    'Chitradurga':76.3980,
    'CID':77.5855,
    'Coastal Security Police':74.126346,
    'Dakshina Kannada':75.2479,
    'Davanagere':75.9218,
    'Dharwad':75.0078,
    'Gadag':75.6355,
    'Hassan':76.1004,
    'Haveri':75.3991,
    'Hubballi Dharwad City':75.1240,
    'ISD Bengaluru':77.6160,
    'K.G.F':78.2710,
    'Kalaburagi':76.8343}

lat_long_dict = {
    'Bagalkot': (16.1850, 75.700),
    'Ballari': (15.1394, 76.9214),
    'Belagavi City': (15.8497, 74.4977),
    'Belagavi Dist': (16.1681, 74.7805),
    'Bengaluru City': (12.9716, 77.5946),
    'Bengaluru Dist': (12.58207912, 77.34503148),
    'Bidar': (17.9104, 77.5199),
    'Chamarajanagar': (11.9261, 76.9437),
    'Chickballapura': (13.4355, 77.7315),
    'Chikkamagaluru': (13.3161, 75.7720),
    'Chitradurga': (14.2251, 76.3980),
    'CID': (12.9814, 77.5855),
    'Coastal Security Police': (14.830648, 74.126346),
    'Dakshina Kannada': (12.8438, 75.2479),
    'Davanagere': (14.4644, 75.9218),
    'Dharwad': (15.4589, 75.0078),
    'Gadag': (15.4315, 75.6355),
    'Hassan': (13.0033, 76.1004),
    'Haveri': (14.7951, 75.3991),
    'Hubballi Dharwad City': (15.3647, 75.1240),
    'ISD Bengaluru': (12.9688, 77.6160),
    'K.G.F': (12.9585, 78.2710),
    'Kalaburagi': (17.3297, 76.8343)
}

def folium_map(map, width=1000, height=500):
    components.html(map._repr_html_(), width=width, height=height)

# Replace the district_crimes function
def district_crimes(district_name):
    global lat_locators, long_locators, fir_short

    df_dist = fir_short[fir_short['District_Name']==district_name]

    crimes_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(crimes_map)

    for index, row in df_dist.iterrows():
        popup = "<br> PS name: " + str(row['UnitName']) + "<br> Beat Name: " + str(row['Beat_Name']) + "<br> Date/Time: " + str(row['Offence_From_Date'])   + "<br> Address: " + row['Place of Offence'] + "</p>"
        folium.Marker([lat_locators[district_name], long_locators[district_name]], popup=popup).add_to(marker_cluster)

    return crimes_map

# def crime_maps(crime_name, year, df):
#     global lat_long_dict, fir_short
#     df_a_crimes = df[(df['CrimeHead_Name'] == crime_name) & (df['Year'] == year)]
#
#     crime_counts = df_a_crimes['District_Name'].value_counts()
#
#     top_5_districts = crime_counts.head(5).index.tolist()
#     df_filtered = df_a_crimes[df_a_crimes['District_Name'].isin(top_5_districts)]
#
#     crimes_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
#     marker_cluster = MarkerCluster().add_to(crimes_map)
#
#     for index, row in df_filtered.iterrows():
#         district_name = row['District_Name']
#         latitude, longitude = lat_long_dict[district_name]
#         popup = "<br> PS name: " + str(row['UnitName']) + "<br> Beat Name: " + str(
#             row['Beat_Name']) + "<br> Date/Time: " + str(row['Offence_From_Date']) + "<br> Address: " + row[
#                     'Place of Offence'] + "</p>"
#         folium.Marker([latitude, longitude], popup=popup).add_to(marker_cluster)
#
#     # html_file = f'{crime_name}.html'
#     # crimes_map.save(html_file)
#     return crimes_map

## Crime maps based on crime and year selected
def crime_maps(crime_name, year, df):
    global lat_long_dict, fir_short

    df_a_crimes = df[(df['CrimeHead_Name'] == crime_name) & (df['Year'] == year)]  # Filter by crime name and year

    crime_count_in_year = len(df_a_crimes)  # Count of occurrences of the selected crime in the selected year

    crime_counts = df_a_crimes['District_Name'].value_counts()

    top_5_districts = crime_counts.head(5).index.tolist()
    df_filtered = df_a_crimes[df_a_crimes['District_Name'].isin(top_5_districts)]

    crimes_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(crimes_map)

    for index, row in df_filtered.iterrows():
        district_name = row['District_Name']
        latitude, longitude = lat_long_dict[district_name]
        popup = "<br> PS name: " + str(row['UnitName']) + "<br> Beat Name: " + str(
            row['Beat_Name']) + "<br> Date/Time: " + str(row['Offence_From_Date']) + "<br> Address: " + row[
                    'Place of Offence'] + "</p>"
        folium.Marker([latitude, longitude], popup=popup).add_to(marker_cluster)

    # Add text to display crime count in the selected year
    text = f"Total {crime_name} crimes in {year}: {crime_count_in_year}"
    folium.Marker(
        location=[15.5, 75.5],  # Adjust location as needed
        icon=folium.map.Icon(),
        popup=text
    ).add_to(crimes_map)

    return crimes_map


## time wise mapping
def year_wise(year, df):
    global lat_long_dict, fir
    df_a_crimes = df[df['Year'] == year]

    crime_counts = df_a_crimes['District_Name'].value_counts()

    top_5_districts = crime_counts.head(5).index.tolist()
    df_filtered = df_a_crimes[df_a_crimes['District_Name'].isin(top_5_districts)]

    crimes_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(crimes_map)

    for index, row in df_filtered.iterrows():
        district_name = row['District_Name']
        latitude, longitude = lat_long_dict[district_name]
        popup = "<br> PS name: " + str(row['UnitName']) + "<br> Beat Name: " + str(row['Beat_Name']) + "<br> Date/Time: " + str(row['Offence_From_Date']) + "<br> Address: " + row['Place of Offence'] + "</p>"
        folium.Marker([latitude, longitude], popup=popup).add_to(marker_cluster)

    # crimes_map.save(f'{year}.html')

    return crimes_map
def get_criminal(district, Unit_Name, Crime_No, month, year=2024, gender='MALE'):
    print("Filtering by:", district, "Crime No.", Crime_No, "Month:", month, year, gender)
    data = accused[(accused['District_Name'] == district) &
                   (accused['UnitName'] == Unit_Name) &
                   (accused['Month'] == month) &
                   (accused['Year'] == year) &
                   (accused['Sex'] == gender)]

    data = data[data['crime_no'] == Crime_No]
    group = data.groupby("Person_Name").size()
    return data

def get_freq_table(data):
    group = data.groupby("Person_Name").size()
    return group


def get_probability(data):
    crime_list = data['crime_no'].tolist()
    prob = accused[accused['crime_no'].isin(crime_list)]

    person_list = data['Person_Name'].tolist()
    prob = prob[prob['Person_Name'].isin(person_list)]

    group = prob.groupby('Person_Name').size()
    return group


def compute_confidence_matrix(district, Unit_name, Crime_No, month, year=2024, gender='MALE', top_n=5):
    data = get_criminal(district, Unit_name, Crime_No, month, year, gender)
    if data.empty:
        st.write("No data found for the given criteria.")
        return

    freq = get_freq_table(data)
    if freq.empty:
        st.write("No frequency data found for the given criteria.")
        return

    past_data = get_probability(data)
    if past_data.empty:
        st.write("No past data found for the given criteria.")
        return

    confidence_values = (past_data / freq).sort_values(ascending=False).head(top_n)

    if confidence_values.empty:
        st.write("No confidence values computed.")
        return

    # Normalize confidence values
    normalized_confidence_values = confidence_values / confidence_values.sum()

    top_criminals = normalized_confidence_values.index.tolist()
    top_confidences = normalized_confidence_values.values.tolist()

    for criminal, confidence in zip(top_criminals, top_confidences):
        st.write(f"Criminal: {criminal}, Confidence: {confidence:.2f}")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=normalized_confidence_values.index, y=normalized_confidence_values.values, ax=ax, color='Coral')
    ax.set_title('Confidence Matrix for Top Criminals')
    ax.set_xlabel('Criminals')
    ax.set_ylabel('Confidence Value')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)


## Criminals based on Arrest IDs

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def criminal(Arr_ID, name=None, age=None, crime_no=None):
    filters = {'Arr_ID': Arr_ID}
    if name is not None:
        filters['Person_Name'] = name
    if age is not None:
        filters['age'] = age
    if crime_no is not None:
        filters['crime_no'] = crime_no

    data = accused[(accused['Arr_ID'] == Arr_ID) &
                   ((name is None) or (accused['Person_Name'] == name)) &
                   ((age is None) or (accused['age'] == age)) &
                   ((crime_no is None) or (accused['crime_no'] == crime_no))
                   ]
    if data.empty:
        st.write("No data found")
    else:
        if name is not None and age is not None or crime_no is not None:
            bg_details(data)
            if get_injury(data, fir) is None:
                pass
            else:
                return data

        else:
            pie_chart(fir, 'CrimeGroup_Name')
            # get_injury(data, fir)
            return data

def pie_chart(data, category):
    group = data.groupby(category).size().nlargest(15)
    fig, ax = plt.subplots(figsize=(8, 8))
    group.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title('Top 15 Crimes Committed under Selected Arrest ID')
    ax.set_ylabel('')
    st.pyplot(fig)

def bg_details(data):
    crime_list = data['crime_no'].tolist()
    age_list = data['age'].tolist()
    prob = accused[accused['crime_no'].isin(crime_list)]
    prob = accused[accused['age'].isin(crime_list)]

    grouped_data = prob.groupby(['age', 'crime_no']).size().reset_index(name='count')

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=grouped_data, x='age', y='count', hue='crime_no', ax=ax)
    ax.set_title("People of Different Ages Committing Crimes")
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title='Crime No', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

def get_injury(data, fir):
    arr_list = data['Arr_ID'].tolist()
    injury = fir[fir['FIR_ID'].isin(arr_list)]

    injury = injury.drop(columns=['District_Name', 'RI', 'Accused Count', 'Unit_ID'])
    if injury.empty:
        st.write("Unavailable Arrest ID in FIR ID")
    else:
        pie_chart(injury, 'CrimeGroup_Name')
    return injury


## Crime analysis based on month

def crime_per_month(crimes, df=fir):
    import calendar

    # for crime in crimes:
    crime_data = df[df['CrimeGroup_Name'] == crime]
    plot_temporal_separate(crime_data, 'Month')

    crime_data_grouped = crime_data.groupby('Month').size().reset_index(name='Frequency')
    total_freq = crime_data_grouped['Frequency'].sum()
    monthly = crime_data_grouped.groupby('Month')['Frequency'].sum()

    sorted_months = monthly.sort_values(ascending=False).index
        # month numbers to month names
    top_months = [calendar.month_name[month] for month in sorted_months[:3]]

    analysis_text = f"The crime '{crime}' is likely to occur more frequently in the months of {', '.join(top_months)}."
    st.write(analysis_text)

import warnings


def plot_temporal_feature(df, label):
    fig = plt.figure(figsize=(12, 8))

    crime_groups = df.groupby(['CrimeGroup_Name', label]).size().reset_index(name='Frequency')
    top_15_crime_groups = crime_groups.groupby('CrimeGroup_Name')['Frequency'].sum().nlargest(15).index
    crime_groups_filtered = crime_groups[crime_groups['CrimeGroup_Name'].isin(top_15_crime_groups)]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sns.lineplot(data=crime_groups_filtered, x=label, y='Frequency', hue='CrimeGroup_Name')

    plt.ylabel("Frequency of Crime", fontsize=12)
    plt.xlabel("Month", fontsize=12)
    plt.title(f"Frequency of Top 15 Crimes by Crime Group and {label}", fontsize=15)
    plt.legend(title='Top Crimes', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.grid(True)
    st.pyplot(fig)  # Display the plot using Streamlit's st.pyplot() function

st.markdown("# Predictive Crime Analysis")
# Display buttons and corresponding forms
option = st.selectbox(
    "Select Analysis:",
    ["District Analysis", "Crime Analysis","Time Analysis", "Victim Analysis", "Criminal Analysis", "Police Analysis"]
)

labels = ['Year', 'Month']

st.markdown("</br>", unsafe_allow_html=True)
st.markdown("</br>", unsafe_allow_html=True)

if option == "District Analysis":
    st.image("images/1district.jpg", use_column_width=True)
    st.subheader("District Analysis")

    form = st.form(key="crime_form")
    district = form.selectbox("Select District:", options=fir['District_Name'].unique())

    if form.form_submit_button(label="District Map"):
        crimes_map = district_crimes(district)
        folium_map(crimes_map)
    year = form.selectbox("Select Year:", options=fir['Year'].unique())

    if form.form_submit_button(label="District Crime Anlaysis"):
        crime_per_year_district(district, year, fir)


    try:
        if form.form_submit_button(label="District Heat Map"):
            fir_short['Latitude'] = fir_short['District_Name'].map(lat_locators)
            fir_short['Longitude'] = fir_short['District_Name'].map(long_locators)
            fir_short['geometry'] = [Point(xy) for xy in zip(fir_short['Longitude'], fir_short['Latitude'])]

            crime_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
            crime_locations = [[point.y, point.x] for point in fir_short['geometry']]
            heat_map = HeatMap(crime_locations, radius=15)
            crime_map.add_child(heat_map)

            # Get HTML representation of Folium map
            folium_map_html = crime_map._repr_html_()

            # Render Folium map in Streamlit
            st.components.v1.html(folium_map_html, width=800, height=400)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif option == "Crime Analysis":
    st.image("images/2crime.jpg", use_column_width=True)
    st.subheader("Crime Analysis")

    col1, col2 = st.columns(2)
    with col1:
        crime = st.selectbox("Select Crime:", options=fir['CrimeHead_Name'].unique())
    with col2:
        year = st.selectbox("Select Year:", options=fir['Year'].unique())

    if st.button("Crime Map"):
        crimes_map = crime_maps(crime, year, fir)
        folium_map(crimes_map)

    form = st.form(key="crime_form")
    crime = form.selectbox("Select Crime:", options=fir['CrimeHead_Name'].unique())
    # year = form.selectbox("Select Year:", options=fir['Year'].unique())

    if form.form_submit_button(label="Crime Hotspots"):
        # best_model, best_accuracy, top_districts, mymap = vs.train_model_for_crime(crime, fir)
        best_model, best_accuracy, top_districts, y_pred, mymap= vs.generate_top_districts_map(crime, fir)
        # map = vs.vulnerable_spots_map(crime)
        folium_map(mymap)

    if form.form_submit_button(label="Crime Predictions"):
        cp.crime_prediction_yearwise(crime, fir)


elif option == "Victim Analysis":
    st.image("images/6victim.jpeg", use_column_width=True)
    st.subheader("Victim Analysis")
    form = st.form(key="victim_form")

    crime = form.selectbox("Select Crime:", options=fir['CrimeHead_Name'].unique())
    if form.form_submit_button(label="Vulnerable Areas"):
        # best_model, best_accuracy, top_districts, mymap = vs.train_model_for_crime(crime, fir)
        best_model, best_accuracy, top_districts, y_pred, mymap= vs.generate_top_districts_map(crime, fir)
        # map = vs.vulnerable_spots_map(crime)
        folium_map(mymap)

    crime = form.selectbox("Select Crime:", options=victim['Crime_No'].unique())
    if form.form_submit_button(label="Vulnerable Details"):
        find_vulnerable_victims_pivot(crime, victim)


elif option == "Time Analysis":
    st.image("images/3time.jpg", use_column_width=True)
    st.subheader("Time Analysis")
    form = st.form(key="time_form")

    crime = form.selectbox("Select Crime:", options=fir['CrimeGroup_Name'].unique())

    if form.form_submit_button(label="Crime per Month"):
        crime_per_month(crime, fir)

    label = form.selectbox("Select Label:", options=labels)

    if form.form_submit_button(label="Top Crimes"):
        plot_temporal_feature(fir, label)

    year = form.selectbox("Select Year:", options=fir['Year'].unique())
    if form.form_submit_button(label="Top Crimes Map"):
        crimes_map = year_wise(year, fir)
        folium_map(crimes_map)

    label = form.selectbox('Select Label:', options=['Offence_From_Date', 'Offence_To_Date'])
    if form.form_submit_button(label="Time Analysis"):
        beat.top_time_instants_count(fir, label, 10)

elif option == "Criminal Analysis":
    st.image("images/5accused.jpg", use_column_width=True)
    st.subheader("Criminal Analysis")

    form = st.form(key="criminal_form")
    district = form.selectbox("Select District:", options=fir['District_Name'].unique())
    Unit = form.selectbox("Select Unit Name:", options=fir['UnitName'].unique())
    Crime_No = form.selectbox("Select Crime No.:", options=accused['crime_no'].unique())
    month = form.selectbox("Select Month:", options=fir['Month'].unique())
    year = form.selectbox("Select Year:", options=fir['Year'].unique())

    if form.form_submit_button(label="Compute Confidence Matrix"):
        compute_confidence_matrix(district, Unit, Crime_No, month, year)

    arrest = form.selectbox("Select Arrest ID:", options=accused['Arr_ID'].unique())
    if form.form_submit_button(label="Arrest IDs Data"):
        criminal(arrest)

    # crime = form.selectbox("Choose Crime:", options=fir['CrimeGroup_Name'].unique())
    firid = form.selectbox("Choose FIR ID:", options=fir['FIR_ID'].unique())
    unitid = form.selectbox("Choose Unit ID:", options=fir['Unit_ID'].unique())
    crimeno = form.selectbox("Choose Crime No:", options=accused['crime_no'].unique())
    if form.form_submit_button(label="Criminal Prediction Analysis"):
        c_pred.train_and_predict_fir_crime_model(fir, firid, unitid, Crime_No)

    # crime = form.selectbox("Select Crime Name:", options=fir['CrimeGroup_Name'].unique())
    if form.form_submit_button(label="Criminal Analysis"):
        # find_accused_pivot(crime, fir)
        find_accused_victim_pivot(crimeno, accused)

elif option == "Police Analysis":
    st.image("images/3police.jpg", use_column_width=True)
    st.subheader("Police Analysis")
    # labels_police = ['UnitName', 'Beat_Name']
    form = st.form(key="police_form")

    unit = form.selectbox("Select Unit Name:", options=fir['UnitName'].unique())
    if form.form_submit_button(label="Top Crimes Per Unit Name}"):
        beat.plot_top_crimes_per_unit(fir, 'UnitName', unit)

    beat_name = form.selectbox("Select Beat Name:", options=fir['Beat_Name'].unique())
    if form.form_submit_button(label="Top Crimes Per Beat Name}"):
        beat.plot_top_crimes_per_unit(fir, 'Beat_Name', beat_name)

    crimes = form.selectbox("Select Crime:", options=fir['CrimeGroup_Name'].unique())
    if form.form_submit_button(label="Crimes Per Beat Analysis"):
        beat.crime_per_month_beat_wise(crimes, fir, beat_name)
        beat.plot_crime_counts_by_beat(fir, beat_name)






