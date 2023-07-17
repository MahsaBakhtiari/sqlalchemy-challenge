![HAwaii](https://www.hawaiimagazine.com/content/uploads/2020/12/Maui-sunset-MattAnderson-GettyImages-967082682.jpg)
# Climate Analysis and Climate App 

This repository contains a project that focuses on climate analysis and the development of a climate application using Flask. The goal is to perform a basic climate analysis and explore climate data for the city of Honolulu, Hawaii. Dive into the documentation and code files to unlock the secrets of Honolulu's weather patterns. Aloha! 🌴🌞🌺


## Project Overview


Welcome to the "Hawaii Climate Explorer" project! Let's analyze the climate before your trip to Honolulu, ensuring you're prepared for paradise.

### Part 1: Climate Analysis & Data Exploration

Using Python, SQLAlchemy, and visualizations, we'll explore the climate database. Highlights include:

- Precipitation: Plotting rainfall trends over the past 12 months.

![line](https://github.com/MahsaBakhtiari/sqlalchemy-challenge/blob/main/SurfsUp/plot_pic/rain_barplot.png)
*The most recent observed year's precipitation lacks discernible patterns.*

- Super Station: Identifying the most active weather station and its temperature extremes.
- Temperature Time Machine: Visualizing the temperature observations at the most active station over the last 12 months.

![hist](https://github.com/MahsaBakhtiari/sqlalchemy-challenge/blob/main/SurfsUp/plot_pic/temp_hist.png)
*The temperature predominantly hovers around 75 degrees throughout the year.*

### Part 2: Flask Climate App

We're building a fun climate app using Flask. It offers:

- Homepage: Start your journey here.
  * Routes: Discover available routes in our app.
- Precipitation Analysis: Retrieve the last 12 months of precipitation data.
- Station List: Explore the list of weather stations.
- Temperature Observations: Access the previous year's temperature records.
- Custom Date Range: Get minimum, maximum, and average temperatures for specific date ranges.

This repository is organized as follows:

- `SurfsUp`: This directory contains the code files and the resource databases.
- `climate.ipynb`: This file contains ipython code for analyzing data and plots.
- `app.py`: This file contains a climate app written using Flask.
- `Resources`: This directory contains the necessary databases used in the project.
- `README.md`: This file, which you are currently reading, provides an overview of the project.


## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please submit a pull  request or open an issue on the GitHub repository.

## Resources

- https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
- https://matplotlib.org/stable/gallery/ticks/tick-formatters.html
- https://stackoverflow.com/questions/29525808/sqlalchemy-orm-conversion-to-pandas-dataframe
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html


