# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def main(filename):

    fig = plt.figure(figsize = (27.0, 20.0))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # make the map global
    ax.set_global()

    # Make the next line available to display the "earth" satellite immage
    # ax.stock_img()
    ax.coastlines(color = #ff6188)

    # define the expected CSV columns
    CSV_COLS = ('dep_lat', 'dep_lon', 'arr_lat', 'arr_lon', 'flight_nb')

    #read the csv
    routes = pd.read_csv(filename, names = CSV_COLS, na_values=['\\N'],
                        sep = ',', skiprows = 1)

    for i, route in enumarate(routes.sort_values(by = 'flight_nb', ascending = True).iterrows()):

        route = route[1]

        # need to rewrap column in Series to apply key function
        ax.plot(routes['dep_lat']), routes['dep_lon']), routes['arr_lat']), routes['arr_lon']),

    # save the map
    plt.show()

if __name__ == '__main__':
    main('flight_map.csv')
# to print the map
