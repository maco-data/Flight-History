# Flight History
My flight history as an ex-Cabin Crew plotted on a map! 1351 flights narrow down to every unique flight I ever did. 10 years over 9000 hours (DBZ pun not intended)

This project uses a dataset I build up after my flight logbook. I took the unique flights and the coordinates of the Airports and plotted the data on top of the Nasa Black Marble world map.

I chose to use Cartopy as Matplotlib Basemap Toolkit suggested to do so (it is bound to be deprecated soon).

This is a small but troublesome project that I have so much fun building up!

## Dependencies

I used Pandas, Cartopy and Matplotlib on this project. I was on Python 3.7

## Data

The dataset file is a csv that contains the following columns:
  - Latitude and Longitude of the airports (Departure / Arrival)
  - A column indexing the number of flights

I used only 3 decimals on the coordinates as it won’t make a big difference once plotted in the map.

As mentioned before this data is personal as it came from my own records but you can google a dataset with airlines routes and use it.

If preferred you can leave out the background image and use the parameters on Cartopy documentation to have the desired end results. As well as you can use any other custom images as long as you add the image information to the images.json file and keep it in the same folder too.

![Output](https://github.com/maco-data/Flight-History/blob/main/output.png)

## Final Thoughts

This was a great project and amazing memorabilia that I will print for myself. Also, I look forward to do the same for my friends once they decide to flight as Cabin Crew.

![banana_airline](https://user-images.githubusercontent.com/85826647/136094929-5bd4e7df-5160-4469-8272-348d41d9db01.png)

