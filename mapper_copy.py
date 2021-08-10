# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def main(filename):

    fig = plt.figure(figsize = (30.0, 20.0))
    # add_subplot(nrows, ncols, index, **kwargs)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    # make the map global
    ax.set_global()

    ax.coastlines(color = '#ff6188')

    # define the expected CSV columns
    csv_cols = ('dep_lat', 'dep_lon', 'arr_lat', 'arr_lon', 'flight_nb')

    #read the csv
    routes = pd.read_csv(filename, names = csv_cols, na_values=['\\N'], sep = ',', skiprows = 1)

    #for i, route in enumarate(routes.sort_values(by = 'flight_nb', ascending = True).iterrows()):

        #route = route[1]

        # need to rewrap column in Series to apply key function
    ax.plot(routes['dep_lat'], transform=ccrs.PlateCarree())
    ax.plot(routes['dep_lon'], transform=ccrs.PlateCarree())
    ax.plot(routes['arr_lat'], transform=ccrs.PlateCarree())
    ax.plot(routes['arr_lon'], transform=ccrs.PlateCarree())

    # save the map
    plt.show()

# to print the map
if __name__ == '__main__':
    main('flight_map.csv')
