# Modules to be used in creating the class objects

# Classes using contextily
import contextily as cx
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

class Place():
    """Describe our place and show it"""
    def __init__(self, names,  longitudes, latitudes): # Everything in the brackets is an argument. Self is always the first argument in a class method defintion
        self.names = names
        self.longitudes = longitudes
        self.latitudes = latitudes

    def dataTable(self):
        self.dataTable = pd.DataFrame({
            'Name': self.names,
            'Longitude': self.longitudes, 
            'Latitude': self.latitudes})
        
    def showDataFrame(self):
        print(self.dataTable)
    
class GeoSpatial(Place):
    def __init__(self, names, longitudes, latitudes, crs):
        # This class is to take the arguments from Place class and use them to create a geodataframe
        super().__init__(names, longitudes, latitudes)
        self.crs = crs
        print("Name: ", self.names, "\nLongitudes: ", self.longitudes, "\nLatitudes: ", self.latitudes, "\nCRS: ", crs)
            
    def geoDataFrame(self):
        self.geoDataFrame = gpd.GeoDataFrame(self.names, 
                         geometry=gpd.points_from_xy(self.longitudes, self.latitudes), 
                         crs= self.crs)
        
    def showGeoDataFrame(self):
        print(self.geoDataFrame)
        
    def webMap(self):
        fig, ax = plt.subplots(figsize=(4,8))
        webMap = self.geoDataFrame.plot(ax=ax)
        # for name, lon, lat in zip(self.names, self.longitudes, self.latitudes):
            # self.geoDataFrame.annotate(name, xy=(lon, lat), xytext=(-4, 2), textcoords='offset points')
        cx.add_basemap(ax, crs=self.geoDataFrame.crs, source=cx.providers.OpenStreetMap.Mapnik)
        plt.show()

places_names = ['Vasco', 'Gedi']
places_longitudes = [146.9945936204649,146.99604274319182]
places_latitudes = [-6.669844987478228,-6.665460847640375,]
places_crs = "EPSG:4326"
        
 # Create GeoDataFrame
many_places = GeoSpatial(places_names, places_longitudes, places_latitudes, places_crs)
many_places.geoDataFrame()
# Print the geodataframe
many_places.showGeoDataFrame()
# Show webmap
many_places.webMap()
