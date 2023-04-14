import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import googlemaps

from sklearn.cluster import SpectralClustering
from sklearn.cluster import KMeans
from geopy.geocoders import Nominatim

def processCSV():
    data = pd.read_csv("FoodPantryDeliveriesThisweek.csv")
    names = data['Account Name'].values
    addresses0 = data['Address (Full)'].values
    addresses = []
    for address in addresses0:
        addresses.append(str(address).replace("\n"," "))
    del addresses[0]
    return names, addresses

def processAddresses(addresses, gmaps):
    coordinates = []
    for address in addresses:
        geocodeResults = gmaps.geocode(address)
        latitude = geocodeResults[0]['geometry']['location']['lat']
        longitude = geocodeResults[0]['geometry']['location']['lng'] 
        ntuple = [latitude,longitude]
        coordinates.append(ntuple)
    return coordinates

def clusterData(coordinates, drivers):
    spectral_model_rbf = SpectralClustering(n_clusters = drivers, affinity = 'nearest_neighbors')
    clusters = spectral_model_rbf.fit_predict(coordinates)
    return clusters

def createRoutes(clusters, drivers, addresses):
    routes = [[]] * drivers
    for i in range(len(clusters)):
        routeNumber = clusters[i]
        routes[routeNumber].append(addresses[i])
    return routes

def sortRoute(route, gmaps):
    FP = "REDACTED"
    distances = gmaps.distance_matrix(FP,route)
    whatIwant = distances['rows'][0]['elements'][0]
    return distances, whatIwant

def main():
    drivers = 4
    names, addresses = processCSV()
    #print(names)
    #print(addresses)
    gmaps = googlemaps.Client(key="REDACTED")
    coordinates = processAddresses(addresses, gmaps)
    #print(coordinates)
    clusters = clusterData(coordinates, drivers)
    routes = createRoutes(clusters, drivers, addresses)
    # print(routes)
    print(clusters)
    # print(type(clusters))
    testDistances, whatIwant = sortRoute(routes[1],gmaps)
    print(testDistances)
    print(whatIwant)


if __name__ == "__main__":
    main()


