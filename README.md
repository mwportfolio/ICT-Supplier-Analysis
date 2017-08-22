# ICT Supplier Analysis

*Analysis of suppliers and contracts for Australian Government ICT Panels.*

### Objective

The objective is to implement an analytics application that facilitates interactive analysis of ICT Suppliers to the Australian Government.

The application will scrape, store, transform, clean, curate and present data using various technologies and tools including: 
- Python, Pandas, urllib, BeautifulSoup, Jupyter
- HTML, JSON, Google Cloud Platform (GCP) DataStore
- Flask, GCP AppEngine, Bootstrap, d3

The approach documented below is intended to align with the levels of the Data Value Pyramid as described in Russell Jurney's book: [Agile Data Science 2.0](http://shop.oreilly.com/product/0636920051619.do)

### Records

In order for the analytics application to function as expected a number of technologies and tools must be setup and configured to work together.

This section deals with integrating the analytics stack and enabling efficient data plumbing between the technologies.

**Data Scrapes and Extracts**

The tenders.gov.au public website lists tenders and contract information that can be scraped using tools like urllib.

We want to extract the HTML data from tenders.gov.au which contains a list of ICT Suppliers and transform it into the more usable JSON format for our application.

The code in the Jupyter Notebook [scrape_ict_panel_suppliers.ipynb](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/code/scrape_ict_panel_suppliers.ipynb) performs the scraping task and produces a JSON file as output [ict_panel_suppliers.jsonl](https://github.com/mwportfolio/blob/master/datasets/ict_panel_suppliers.jsonl) containing the following elements:

- Australian Business Number (ABN),
- Supplier Name, 
- State, and
- Postcode.

Now that we have extracted our data we will store it in a NoSQL database from which our web application can read. 

**Database Integration**

There are a number of cloud platforms which offer NoSQL databases as part of a free trial, and because I've already expired my free trials on AWS and Azure we will use Google Cloud Platform (GCP) as the platform to host our database and web application.

GCP's DataStore service provides NoSQL functionality with some limitations, although they can be worked around. For example the ability to dump nested JSON into DataStore is not available, so some modelling of the data into an appropriate strucutre may need to occur before saving. 

DataStore terms:

Kind = Collection/Table
Entity = Records

Populating a new Kind with Entities is fairly straightforward in Python, as shown in the Jupyter Notebook [blah.ipynb](blah.ipynb).

The first notebook populates the **suppliers** Kind with Entities consisting of the scraped data from tenders.gov.au.

Once data can be saved to DataStore the next step is to verify that it can be read, as shown in the notebook [blah2.ipynb](blah2.ipynb).

**Web Framework & Presentation**

GCP's AppEngine allows for Flask apps developed locally to be deployed onto the Google Cloud for serving public users.

The first thing we need our app to do is connect with GCP DataStore, read data, and display it in a simple table.

The web application framework Flask is configured in the Python file [main.py](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/code/flask/main.py)

The app is configured for a route "/all_suppliers" which we will configure to list all records from our DataStore Kind "suppliers".

We setup our app to use a HTML template [layout.html](layout.html) that will include standard layout, header, footer, and styling.

The "/all_suppliers" route uses Flask's render_template function to load the [suppliers.html](suppliers.html) file, which extends our layout.html template and renders a standard HTML table iterating over the records from our DataStore Kind. 

Adding bootstrap into our layout.html and setting our table class property in suppliers.html adds some nice styling to our rendered table.

### Charts and Reports

Once the data plumbing and technologies are working in harmony the raw data can be improved, enhanced and presented in such a way that invites the user to explore.

This section deals with cleaning, aggregating and curating (mining) the raw data into more digestable formats for exploration through integrated visualisations.

- data cleaning
- curation of aggregate datasets
- visualisations
