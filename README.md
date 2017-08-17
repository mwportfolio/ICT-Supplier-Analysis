# ICT Supplier Analysis

*Analysis of suppliers and contracts for Australian Government ICT Panels.*

### Objective

The objective is to implement an analytics application that facilitates interactive analysis of ICT Suppliers to the Australian Government.

The application will scrape, store, transform, clean, curate and present data using various technologies and tools including: 
- Python, Pandas, urllib, Jupyter
- HTML, JSON, MongoDB
- Flask, Bootstrap, d3

The approach documented below is intended to align with the levels of the Data Value Pyramid (from the bottom moving upwards) as described in Russell Jurney's book: [Agile Data Science 2.0](http://shop.oreilly.com/product/0636920051619.do)

### Records

In order for the analytics application to function as expected a number of technologies and tools must be setup and configured to work together.

This section deals with integrating the analytics stack and enabling efficient data plumbing between the technologies.

**Data Scrapes and Extracts**

The tenders.gov.au website lists tenders and contract information for the public to view that can be scraped using tools like urllib.

We want to extract the HTML data from tenders.gov.au and transform it into a more usable format for our application: JSONLines.

The code in the Jupyter Notebook [scrape_ict_panel_suppliers.ipynb](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/code/scrape_ict_panel_suppliers.ipynb) performs this task and produces the JSON file [ict_panel_suppliers.jsonl](https://github.com/mwportfolio/blob/master/datasets/ict_panel_suppliers.jsonl) containing the following elements:

- Australian Business Number (ABN),
- Supplier Name, 
- State, and
- Postcode.

**Database Integration**



**Web Framework & Presentation**

The web application framework Flask is configured in the Python file [ict_supplier_analysis.py](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/code/ict_supplier_analysis.py)

![](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/screenshots/screenshot_run_flask_app.PNG?raw=true)

Getting list of all suppliers as JSON text using API endpoint

![](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/screenshots/screenshot_app_all_suppliers_json.PNG?raw=true)

### Charts and Reports

Once the data plumbing and technologies are working in harmony the raw data can be improved, enhanced and presented in such a way that invites the user to explore.

This section deals with cleaning, aggregating and curating (mining) the raw data into more digestable formats for exploration through integrated visualisations.

- data cleaning
- curation of aggregate datasets
- visualisations
