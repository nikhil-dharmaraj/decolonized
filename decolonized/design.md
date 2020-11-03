OVERALL STRUCTURE OF THE SITE

The DE-Colonized site was constructed using the model of Flask and HTML templates. Built off a base "layout.html" file, the two main pages of the site were both templates, rendered by Flask
in a typical "application.py" file. Parameters such as a itemized-version of the CSV file were passed to these templates. The logo in the navigation bar was designed using freelogodesign.org,
and the resist-marker-icon and quote-image on the home page were both retrieved through a google search.

AESTHETICS

Aesthetics-wise, this project relied almost entirely on Bootstrap. Throughout the webpage, I made liberal use of Bootstrap's Jumbotron feature, used to display information in a coherent, grey,
lead theme. The navigation bar and footer also came directly from the Bootstrap libraries. The range-slider timeline was heavily inspired this tutorial: https://www.w3schools.com/howto/howto_js_rangeslider.asp.

DATA SOURCING

All the information for the Histories page is sourced from a single Wikipedia link: https://en.wikipedia.org/wiki/Decolonization#Timeline_of_independence. For easier use, I went through the
manual process of compiling these three tables into a CSV file, along with some manual data cleaning work for easier processing on the computational end of things. That data now lives in the
"histories.csv" file of this project.

MAP FUNCTIONALITY

The timeline/map functionality depends heavily on multiple libraries. First off, the embedding of an interactive map comes from TomTom, a visualization library that can embed all kinds of
different features in a website. I opted to use TomTom for a couple of reasons: flexibility, interactivity, and affordability (the primary alternative I was considering, Google Maps, ends
up being somewhat expensive). Within TomTom, it is possible to build the dropping marker/popup feature and customizing it with icons/styles as one might need. The "timeline" functionality simply
consists of a stylized HTML range slider, with values sourced from the years in the informative CSV file. Using a simple onchange callback, at each year, information is able to be visualized
on the map for the rows corresponding to that year in the CSV.

That's where another library comes into play: LocationIQ. Essentially, once a user selects a year, all the rows of de-colonizing events from the CSV corresponding to that year are pulled up.
For each of those rows, a marker is dropped in the centroid coordinate pair of the Decolonized state value: to do this, these coordinates are retrived from the geocoding API offered by LocationIQ
(one can simply pass in a search term in English and get in return a list of matching lat/long coordinates). For simplicity, I've simply plotted the first pair that comes back in this list,
without checking the rest. Note: I needed to space out each iteration of the loop because jmy free account with TomTom allows only 2 requests per second, and some years had more than 2 events.
Thus, I had to implement a loop-with-delay functionality, which was somewhat challenging within the constraints of JavaScript. I was able to do so eventually with a self-calling function, a
decreasing counter variable, and the setTimeout() function. I learned about this method from this tutorial: https://scottiestech.info/2014/07/01/javascript-fun-looping-with-a-delay/.

Ultimately, then, for each event that occurred in the year the user selected, a marker is dropped at the appropriate coordinate value along with the rest of the information
for that row in a popup (all done using TomTom's documentation).