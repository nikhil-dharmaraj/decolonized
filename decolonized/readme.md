TO USE THIS PROJECT:

Download the directory of this app into an IDE of some sort. Then, open the IDE and navigate to the project's directory (/decolonized) In the terminal, export a personal API key that you can use
to run Flask. From there, simply type "flask run" and click the link that is outputted in the "Running on..." line. That will take you to the home page of my project. All other links and such are
accessible from there.

TO TEST THIS PROJECT:

The entire web project only has two main pages: the homepage (which you will be taken to when you click the aforementioned link from "flask run"), and the histories page. The home page simply
describes the function and goal of this project (no user-interactivity component); the histories page allows users to click on an interactive timeline and thus explore the history of decolonization
on an animated map.

To start, the user simply has to pick a point, corresponding to a year, on the range slider timeline below the map on the Histories page. At any year that the user clicks, the map will drop
a fist-shaped marker corresponding to each country that was decolonized this year, along with a popup with some information about the event. These popups can be dismissed by a click of the "x"
at the top of the icon, and they can be re-opened thereafter by clicking on the marker (which stays on the map once dropped). In this way, the user can explore the history and context surrounding
the various de-colonization movements. The only way to "reset" the map, per se, is to reload the page. All the information is sourced from a Wikipedia table, converted into a CSV file.