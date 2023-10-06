import pandas as pd



# Fungsi untuk melakukan transformasi DataFrame
def transform_dataframe():

    df = pd.read_csv('/opt/airflow/data/P2M3_rais_yufli_data_raw.csv')
    # Merubah nama kolom yang awalnya uppercase menjadi lowercase
    df.columns = df.columns.str.lower()

    # Rename kolom 
    df_clean = df.rename(columns={'bedrooms': 'bed_rooms','bathrooms': 'bath_rooms','mainroad': 'main_road','guestroom':'guest_room',
                       'hotwaterheating': 'hot_water_heating','airconditioning': 'air_conditioning','furnishingstatus':'furnishing_status'})
    
    df_clean.to_csv('/opt/airflow/data/P2M3_rais_yufli_data_clean.csv', index=False)