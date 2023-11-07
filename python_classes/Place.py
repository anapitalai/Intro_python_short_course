# Modules to be used in creating the class objects
import pandas as pd

class Place():
    """Describe our place and show it"""
    def __init__(self, names,  longitudes, latitudes):
        # Create variables for the names, longitudes and latitudes
        self.names = names
        self.longitudes = longitudes
        self.latitudes = latitudes

    def dataTable(self):
        # Create a dataframe from the above variables of names, longitudes, and latitudes
        self.dataTable = pd.DataFrame({
            'Name': [self.names],
            'Longitude': [self.longitudes], 
            'Latitude': [self.latitudes]})
        
    def showDataFrame(self):
        # Print the dataframe
        print(self.dataTable)

# Create an object of Place class called place1
place1 = Place("vasco", 40.1276701, -3.2236304)

# Create a dataframe from the coordinates of place1
place1.dataTable()

print(place1.showDataFrame())
