# Food-Pantry-Tools

Hi!

I've been volunteering at my local food pantry for almost a decade at this point. 

Over the years, I've found opportunities to tackle some of the technical challenges we've been facing by applying some of the techniques I learned at UChicago. I've uploaded a few of them.

## drivers.py: Driver delivery routes

Every Tuesday we deliver food to clients who are unable to come to us. Previously creating driver delivery routes was a manual process that involved a map of our town, a whiteboard marker, and twenty minutes of planning each week. This the goal of this tool was to completely eliminate that.

## nc.ipynb and fb.ipynb: Ingesting data from local food bank

We receive food from our local food bank denoted FB twice a month, averaging ~4000 pounds of food each time. As a food pantry, we have to document everything we receieve to multiple authorities and generate multiple types of reports.

Originally we used to manually input every single item we ordered seperately, record all of the associated data with that item, and deal with it later for our monthly reports.

First, I developed a tool (nc.ipynb) to automatically intake all the order data from FB's website and output it in a format for later transformation. This was successfully used for two years, saving an hour of work every month minimum.

Recently, I developed another tool (fb.ipynb) to automatically categorize all of our purchases into categories and product types based on a central database. This was a process that we had to do before manually with no database, which led to inconsistent results from month to month. 

In doing so, I have saved over an hour of work every single month of manual data entry, completely eliminated errors due to inconsistency, and created a central database of all of our FB orders which saves hours of time on our yearly reports.

## LS.ipynb: Ingesting data from local food rescue

A local food rescue organization named LS comes by several times a week and brings us hundreds of pounds of food from local grocery stores. As a food pantry, we have to document everything we receieve to multiple authorities and generate multiple types of reports.

Originally we used to record and label every pound of food as we receieved it on pen and paper: this included during Boston rain and snow and would slow down the deliveries by ~5 minutes. This would then be manually entered at the end of every month and put into associated reports, a process that would take upwards of thirty minutes.

After talking to LS, they were willing to send us their records each month of what they bring to us in a PDF. 

This tool ingests the data from this PDF, categorizes all the appropriate output, and outputs in the format that we reuse for all of our reports, saving over an hour of time each month.
