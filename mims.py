
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

data = pd.read_csv("C:/Users/MKOUJI\Downloads/cleaned_autos.csv")

print(data.groupby('vehicleType').size())
 
# 1. Nombre de véhicules par type
df_type = data.groupby('vehicleType').size().reset_index(name='Count')
plt.bar(df_type['vehicleType'], df_type['Count'])
 
# 2  Répartition des véhicules en fonction de l'année d'immatriculation
plt.hist(data['yearOfRegistration'])
 
 
# 3. Nombre de véhicules par marque
df_brand = data.groupby('brand').size().reset_index(name='Count')
plt.bar(x=df_brand['brand'], height=df_brand['Count'])
 
#4 Prix moyen par carburant et boîte
df_fuel = data.groupby(['fuelType','gearbox'])['price'].mean().reset_index()
 
plt.figure(figsize=(10,6))
plt.bar(x='fuelType', height='price', data=df_fuel)  
plt.xticks(rotation=45)
plt.title('Prix moyen par carburant et boîte de vitesses')
plt.show()
 
 
#4 Prix marque et categorie
df_recomm = data[['brand','vehicleType','price']]
mean_price = df_recomm.groupby(['brand','vehicleType'])['price'].mean()
print(mean_price)
 
 
#5. Prix moyen par type de véhicule et boîte de vitesses
 
mean_price = data.groupby(['vehicleType','gearbox'])['price'].mean().reset_index()
 
plt.figure(figsize=(10,8))
plt.subplot(111, projection='polar')
 
sizes = mean_price.groupby('vehicleType')['price'].sum()
labels = sizes.index
 
plt.plot(sizes, labels=labels, autopct="%1.1f%%")
plt.title('Prix moyen par type de vehicule et boîte de vitesse')
 
 
# 5 Prix moyen par carburant et boîte de vitesses
 
df = data.groupby(['fuelType','gearbox'])  
mean_price = df['price'].mean().reset_index()
 
plt.figure(figsize=(10,6))
plt.bar(x='fuelType', height='price', data=mean_price)
plt.xticks(rotation=45)
plt.title('Prix moyen par carburant et boîte')
 
 
#  données sur les marques de riche
marque_CHERE = ["Mercedes", "BMW"]
data_premium = data[data['brand'].isin(marque_CHERE)]
 
# les prix moyens par marque et type
mean_price = data_premium.groupby(['brand','vehicleType'])['price'].mean()
 
print("Les 2 marques recommandées sont:", marque_CHERE)
print("Les 2 catégories  berline de luxe, SUV de luxe")
 
 
df_heatmap = mean_price.reset_index()
 
# Heatmap
 
df_heatmap = mean_price.reset_index()
 
plt.figure(figsize=(10,8))
corr = df_heatmap.corr()
plt.imshow(corr)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.colorbar()
plt.title("Prix moyens par marque et catégorie")
plt.show()









