# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def main(filename):
    # float is size in inches
    # set resolution to high
    fig = plt.figure(figsize = (15.0, 15.0, dpi = 300))

    # central_longitude "55.2708" is DXB longitude, centering the map on Dubai
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=55.2708))

    # make the map global
    ax.set_global()

    # set coastlines color to "FAUX-STRAWBERRY"
    # changed linewidth
    ax.coastlines(color = '#ff6188', linewidth= 0.5)

    # define the expected CSV columns
    csv_cols = ('dep_lat', 'dep_lon', 'arr_lat', 'arr_lon', 'flight_nb')

    # read the csv
    # set the data
    routes = pd.read_csv(filename, names = csv_cols, na_values=['\\N'], sep = ',', skiprows = 1)

    # put the lons and lats separated
    dep_lon, dep_lat = routes['dep_lon'], routes['dep_lat']
    arr_lon, arr_lat = routes['arr_lon'], routes ['arr_lat']

    # data to be plot
    # changed color of the line to "FAUX-SKY BLUE"
    # "Geodetic()" set the lines in the spherical shape of the world
    # changed the linewidth
    ax.plot([dep_lon, arr_lon], [dep_lat, arr_lat], color = '#78dce8', linewidth= 0.1, transform=ccrs.Geodetic())

    # display the map
    plt.show()

    # save output image of map
    #plt.savefig('output.svg', dpi=300, facecolor='black')

# to print the map
if __name__ == '__main__':
    main('dataset.csv')
