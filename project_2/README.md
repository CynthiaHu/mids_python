# Project 2

The final project will consist of an analysis of a dataset, using the numpy and pandas tools we covered in class.

## The Setup & Instructions
- 2 to 3 people (no exceptions)

#### The Data Analysis
- The exercise is unguided.  You will come up with your own interesting questions that you can answer using the variables in your dataset, then perform an analysis based on those questions.
- You can analyze either an *instructor approved dataset of your finding* or one that we have preapproved. You may join several datasets together.  For example, you might combine two datasets to answer questions like, after 2 days of rain, is felony crime higher in NYC?
- The project emphasizes the exploratory and descriptive techniques covered in class.  Although some of you have a background in statistics, we ask that you avoid any statistical inference or other advanced techniques.  In particular, this means that you should confine your analysis to the sample of data you have, and avoid making statements about the population that the sample comes from.

#### The Proposal

With your group come up with a 1 - 2 page proposal about the questions that you intend to ask of the data. 
This should include:
- Initial plots, figures or tables. 
- References to column names and the analysis that they may provide. 
- Additional datasets that you plan on including in your analysis like the weather data. This means links, columns that you'll join on, etc.
- What you plan to cover in the final report and how you plan on organizing it.

#### The Report

The report will be 8+ pages (including appropriately sized figures) and will be a report on what you found out from the data. This should focus on telling stories and explaining the narrative of the exploration and challenges associated with that. The report should not include any code - all code should be included in a sub-folder in either plain python files or in jupyter notebooks.

For the report, any graph, table, or figure should be annotated with why it is included. This is really to enforce just slapping graphs in your report that have no meaning.

One thing to note, using github to share jupyter notebook is a **nightmare**. Be sure to create copies of notebooks when you make an edit and as code gets stable, you'll likely find it easier to just put it into a python file and import it.

## Instructor Pre-Approved Datasets
- [Political Ad Archive](http://politicaladarchive.org/data/)
- [Open Food Facts](http://world.openfoodfacts.org/data)
- [NYPD 7 Major Felony Incidents](https://catalog.data.gov/dataset/nypd-7-major-felony-incidents)
- [MYC Parking Violations](https://data.cityofnewyork.us/dataset/Parking-Violations-Issued-Fiscal-Year-2015/c284-tqph)
- [Chicago Crime Incidents](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2)
- [US Gov't Web Logs](https://analytics.usa.gov/)
- [Citi Bike Share NYC](http://www.citibikenyc.com/system-data)
- [SF Bay Area Bike Share Data](http://www.bayareabikeshare.com/open-data)
- The airlines dataset that we explored in class and any subsets thereof (so you may choose to analyze several years for example). Obviously a repeat of the analysis that I performed would not be appropriate :).

## Potential Locations for Other Datasets
**REMEMBER NONE OF THESE HAVE BEEN APPROVED, YOU HAVE TO TALK TO YOUR INSTRUCTOR TO GET THEM APPROVED.**

- [Historical Weather Data](https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-ghcn)
  - This can be a bit difficult to figure out what to download. [In this discussion](https://news.ycombinator.com/item?id=10465342) there seem to be some pointers on how to get at it. This is dataset is pre-approved as a **supplemental** dataset, but please come to me if your group would like this to be their focus. I imagine there are some good resources for how best to download this data across the web but I just haven't had the time to search for them.
- [Data is Plural](http://tinyletter.com/data-is-plural/archive)
  - I got the pre-approved datasets primarily from here. Pretty extensive list.
- [Awesome Public Datasets](https://github.com/caesar0301/awesome-public-datasets)
  - Awesome list that's worth saving for future reference. Be sure to actually download and explore the data before sending me the link because sometimes it's harder than it appears. There are some awesome datasets here like the NYC taxi dataset.
- [Data.gov](http://data.gov/)
  - All gov't data, which is good!
- [OpenDataCache.com](http://www.opendatacache.com/)
  - Cache of the above link - can sometimes speed up downloads.
- [Reddit/r/Datasets](https://www.reddit.com/r/datasets)
  - Community generated and definitely some potential for good datasets. Worth searching.

#### To get a dataset approved:
1. Send me a description of the data including a link to the exact dataset or a place where I can download it in one click w/o registering or anything like that. 
    - The data needs to be in a raw text file format like json or csv (or at least very easy to convert to that format).
    - Please report the size of the dataset or the subset you plan on looking at. This is **not** a big data project.
2. Show that you've done some preliminary research that there will be enough interesting questions to answer in the data. This will include column names, information about missing data
