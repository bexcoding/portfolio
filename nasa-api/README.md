# NASA API Program

This program works with an API from NASA called APOD (Astronomy Picture of the Day). After getting an API key from the NASA website, you can plug it into this program and request the picture of the day. The picture is always astronomy related and is often a large picture of stars or galaxies. You can make as many calls to the API as you want in a day, but the picture only changes once per day.

# Code Setup

1. Download or copy this python code into it's own folder with a name like "Space Pictures"
2. Go to the [NASA API website](https://api.nasa.gov) and generate an API key
3. Insert your API key directly in the python file if no one else has access to the file. Otherwise, store the API in a seperate file and import it into this file.
4. Run the file with the python command from the command line.

# Advanced

While you can go to the command line and run this file every day, it is possible to automate this task. Follow all of the steps above so that the code is set up and ready to run. Once you know that the code runs the way you want, create a batch file that runs this API and stores the picture in the folder. Then create a scheduled task that runs this program once a day at the same time every day.
To take it one step beyond that, set the desktop background to choose a random picture from the folder every couple hours. Over time, your collection of space photos will grow and you will always have an interesting desktop background. This code was written to save only the photo that is obtained from the JSON response, but an old version also saved the description and date of each photo into a text file. That way, if you were ever curious about what a certain photo was, you could search its description by date in the text file.
