# -*- coding: utf-8 -*-

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd
import os

# set the path for custom background image
current_directory = os.getcwd()
os.environ["CARTOPY_USER_BACKGROUNDS"] = os.path.join(current_directory, 'data', 'CARTOPY_IMGS')
os.path.join(current_directory, 'data', 'CARTOPY_IMGS')


def main(filename):
    # float is size in inches
    # set resolution to high
    fig = plt.figure(figsize=(10.0, 5.0,), dpi=300)

    # centering the map on Dubai, central_longitude "55.2708" is DXB longitude
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=55.2708))

    # make the map global
    ax.set_global()

    # background
    ax.background_img(name='Nasa', resolution='high')

    # define the expected CSV columns
    csv_cols = ('dep_lat', 'dep_lon', 'arr_lat', 'arr_lon', 'flight_nb')

    # read the csv
    routes = pd.read_csv(filename, names=csv_cols, na_values=['\\N'], sep=',', skiprows=1)

    # put the lons and lats separated
    dep_lon, dep_lat = routes['dep_lon'], routes['dep_lat']
    arr_lon, arr_lat = routes['arr_lon'], routes['arr_lat']

    # data to be plot
    ax.plot([dep_lon, arr_lon], [dep_lat, arr_lat], color='#f9ba00', linewidth=0.1, transform=ccrs.Geodetic())

    # save output image of map
    plt.savefig('output.png', bbox_inches='tight', transparent=True, pad_inches=0)

    # display the map
    plt.show()


# to print the map
if __name__ == '__main__':
    main('dataset.csv')
