# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def main(filename):
    #Float is size in inches
    fig = plt.figure(figsize = (30.0, 30.0))

    # add_subplot(nrows, ncols, index, **kwargs)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # make the map global
    ax.set_global()

    # changed color to subtle pink
    ax.coastlines(color = '#ff6188')

    # define the expected CSV columns
    csv_cols = ('dep_lat', 'dep_lon', 'arr_lat', 'arr_lon', 'flight_nb')

    #read the csv
    routes = pd.read_csv(filename, names = csv_cols, na_values=['\\N'], sep = ',', skiprows = 1)

    # dep and arr aggregate in two plots
    # line color changed to cyan
    # Geodetic projection gives the curve to the line
    ax.plot(routes['dep_lat'], routes['dep_lon'], color = '#78dce8', transform=ccrs.Geodetic())
    ax.plot(routes['arr_lat'], routes['arr_lon'], color = '#78dce8',transform=ccrs.Geodetic())

    #display the map
    plt.show()

# to print the map
if __name__ == '__main__':
    main('flight_map.csv')
