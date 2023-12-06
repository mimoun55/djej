import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
 
data = pd.read_csv('C:/Users/MKOUJI/Downloads/cleaned_autos.csv')
print(data.head(20))
 
print(data.groupby('vehicleType').size())
 
#1. Nombre de véhicules par type
df_type = data.groupby('vehicleType').size().reset_index(name='Count')
plt.title("Nombre de véhicules par type")
plt.bar(df_type['vehicleType'], df_type['Count'])

 
#2  Répartition des véhicules en fonction de l'année d'immatriculation


nombre_de_vehicules_par_annee = data.groupby('yearOfRegistration')['name'].count()

plt.bar(nombre_de_vehicules_par_annee.index, nombre_de_vehicules_par_annee.values)


plt.xlabel("Année d'immatriculation")
plt.ylabel("Nombre de véhicules")
plt.title("Répartition par année d'immatriculation")
plt.show()


# 3. Nombre de véhicules par marque
df_brand = data.groupby('brand').size().reset_index(name='Count')
plt.bar(x=df_brand['brand'], height=df_brand['Count'])
plt.xticks(rotation=45, ha="right")
plt.title(" Nombre de véhicules par marque")
plt.show()
#4 Prix moyen par carburant et boîte
df_fuel_gearbox = data.groupby(['fuelType','gearbox'])['price'].mean().reset_index()
 
plt.figure(figsize=(10,6))
plt.bar(x='fuelType', height='price', data=df_fuel_gearbox)  
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
plt.title(" Prix moyen par type de véhicule et boîte de vitesses")
plt.show()
sizes = mean_price.groupby('vehicleType')['price'].sum()
labels = sizes.index
 
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title('Prix moyen par type de vehicule et boîte de vitesse')
 
 
# 5 Prix moyen par carburant et boîte de vitesses
 
df = data.groupby(['fuelType','gearbox'])  
mean_price = df['price'].mean().reset_index()
 
plt.figure(figsize=(10,6))
plt.bar(x='fuelType', height='price', data=mean_price)
plt.xticks(rotation=45)
plt.title('Prix moyen par carburant et boîte')
plt.show()
 
#  données sur les marques de riche
marque_CHERE = ["Mercedes", "BMW"]
data_premium = data[data['brand'].isin(marque_CHERE)]
 
# # les prix moyens par marque et type
mean_price = data_premium.groupby(['brand','vehicleType'])['price'].mean()
 
print("Les 2 marques recommandées sont:", marque_CHERE)
print("Les 2 catégories  berline de luxe, SUV de luxe")
 
 
df_heatmap = mean_price.reset_index()
 





import seaborn as sns
import matplotlib.pyplot as plt

# Créer un heatmap pour visualiser le prix moyen des véhicules par type de véhicule et marque
mean_prices = data.groupby(['brand','vehicleType'])['price'].mean().reset_index()
 
 
top_brands = mean_prices.groupby('brand')['price'].mean().sort_values(ascending=False)[:2]

fig, ax = plt.subplots(figsize=(10,6))
 
heatmap_data = mean_prices[mean_prices['brand'].isin(top_brands.index)]  
sns.heatmap(heatmap_data[['price']], cmap="YlGnBu", annot=True, fmt='.0f', ax=ax)
 
 
 
# Recommandation des types de véhicules correspondant aux marques
print(f"Les marques à privilégier sont {', et '.join(top_brands.index)} ")
print(f"Les types de véhicules associés sont les berlines et SUV")
plt.show()









