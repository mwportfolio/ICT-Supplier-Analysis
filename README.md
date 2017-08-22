# ICT Supplier Analysis

*Analysis of suppliers and contracts for Australian Government ICT Panels.*

### Objective

The objective is to build & deploy an analytics application that enables analysis of ICT Suppliers to the Australian Government.

The app should be able to answer questions such as:
- which supplier has the largest government footprint? (ie is represented across the highest number of agencies)
- which supplier has the largest total / individual contract value?
- which agency has the largest total / individual contract?
- how does an agencies budget/expenses compare with current contracts?

To allow these questions to be answered the app will need to present visualisations and tables that allow users to explore and interact with the data.

The app will scrape, store, transform, clean, curate and present data using various technologies and tools across the full stack including: 
- Python, Pandas, urllib, BeautifulSoup, Jupyter
- HTML, JSON, Google Cloud Platform (GCP) DataStore
- Flask, GCP AppEngine, Bootstrap, d3

The approach documented below is intended to align with the levels of the Data Value Pyramid as described in Russell Jurney's book: [Agile Data Science 2.0](http://shop.oreilly.com/product/0636920051619.do)

### Records

In order for the app to function as expected a number of technologies and tools must be configured to work together, thereby forming our stack.

This section deals with integrating the stack and enabling efficient data plumbing between the technologies.

**Data Scrapes and Extracts**

The tenders.gov.au public website lists tenders (business opportunities) for the Australian Government, as well as supplier and contract information that can all be extracted (scraped) using tools like the Python library urllib.

The first dataset we want to extract from tenders.gov.au is a list of ICT Suppliers.

We will be extracting the HTML data and transforming it into the more usable JSON format for our application.

The code in the Jupyter Notebook [scrape_ict_panel_suppliers.ipynb](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/jupyter_notebooks/scrape_ict_panel_suppliers.ipynb) performs this first task, and producing a JSON file as output [ict_panel_suppliers.jsonl](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/datasets/ict_panel_suppliers.jsonl) containing the following elements:

- Australian Business Number (ABN),
- Supplier Name, 
- State, and
- Postcode.

The second dataset we want to extract is a list of contracts for each supplier.

To extract the contract information for each supplier we will perform a search against tenders.gov.au using the supplier's ABN. The code in the Jupyer Notebook [TODO.ipynb](https://github.com/mwportfolio/blob/master/jupyter_notebooks/TODO.ipynb) performs this task.

Now that we have extracted our base data we will store it in a NoSQL database from which our web application can read. 

**Database Integration**

Google Cloud Platform (GCP) was the platform chosen to host our database and web application for no other reason than the author's free trials had already expired for both AWS and Azure.

GCP's DataStore service provides NoSQL functionality with some limitations. For example the ability to dump nested JSON into DataStore is not available, so some modelling of the data into an appropriate strucutre may need to occur before saving. 

DataStore terms:
- Kind = Collection/Table
- Entity = Records

Since we already have our base data extracts we can now save these as new Kinds. Our list of suppliers will be saved into the 'suppliers' Kind, and our list of contracts will be saved into the 'supplier_contracts' Kind.

The code in Jupyter Notebook [blah.ipynb](blah.ipynb) performs this task.

Once data can be saved to DataStore the next step is to verify that it can be read, as shown in the notebook [blah2.ipynb](blah2.ipynb).

With the data now readable from our database the next step is to present the records to the user.

**Web Framework & Presentation**

Flask was the web framework chosen to run our app pages. It runs on Python and has Jinja2 templating features which make developing pages a more streamlined process.

GCP's AppEngine allows for Flask apps developed locally to be deployed onto the Google Cloud for serving public users.

The first thing our app needs to do is connect with GCP DataStore, read data, and display it in a simple table.

The flask app is configured per the code in [main.py](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/code/python/main.py).

The app is configured for a route named "/all_suppliers" which we will configure to list all records from our DataStore Kind "suppliers".

We setup our app pages to use a HTML template [layout.html](layout.html) that will include standard layout, header, footer, and styling.

The "/all_suppliers" route uses Flask's render_template function to load the [suppliers.html](suppliers.html) file, which extends our layout.html template and renders a standard HTML table iterating over the records from our DataStore Kind. 

Adding bootstrap into our layout.html and setting our table class property in suppliers.html adds some nice styling to our rendered table.

### Charts and Reports

Enhancements to the presentation can be made once the data plumbing and technologies are working in harmony.

Enhancements could include visualisations, integrating additional datasets, and developing interactive analytical features.

This section deals with cleaning, aggregating and curating (mining) the raw data into more digestable formats for exploration through integrated visualisations.

- data cleaning
- curation of aggregate datasets
- visualisations
