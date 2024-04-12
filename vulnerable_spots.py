import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import folium

# Load data
fir = pd.read_csv('Datasets/FIR_Details_Data.csv')
accused = pd.read_csv('Datasets/AccusedData (1).csv')
victim = pd.read_csv('Datasets/VictimInfoDetails (1).csv')
fir_short = fir[fir['Year'] == 2023]

def generate_top_districts_map(crime_name, df):
    # df = pd.read_csv('FIR_Details_Data.csv')
    df_crime = df[df['CrimeHead_Name'] == crime_name]

    X = df_crime.drop(columns=['CrimeHead_Name', 'District_Name'])
    y = df_crime['District_Name']

    encoder = OneHotEncoder()
    X_encoded = encoder.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    models = {
        'RandomForest': RandomForestClassifier(),
        'LogisticRegression': LogisticRegression()
    }
    accuracies = {}

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies[model_name] = accuracy
    best_model = max(accuracies, key=accuracies.get)
    best_accuracy = accuracies[best_model]

    top_districts = df_crime['District_Name'].value_counts().head(5)
    top_districts.to_csv('top_districts.csv', index=False)

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
    map_center = [12.9716, 77.5946]
    mymap = folium.Map(location=map_center, zoom_start=10)

    for district, crime_count in top_districts.items():
        latitude, longitude = lat_long_dict.get(district, (0, 0))
        folium.Marker([latitude, longitude], popup=f'{district}<br>Crime Count: {crime_count}').add_to(mymap)

    mymap.save('top_districts_map.html')

    return best_model, best_accuracy, top_districts, y_pred, mymap


# crime_name = 'Street Gambling (87)'
# best_model, best_accuracy, top_districts, y_pred, mymap= generate_top_districts_map(crime_name, fir)