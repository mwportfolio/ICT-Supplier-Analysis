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

The code in [scrape_ict_panel_suppliers.ipynb](https://github.com/mwportfolio/ICT-Supplier-Analysis/blob/master/code/scrape_ict_panel_suppliers.ipynb) scrapes and saves the HTML to a [local file](), then extracts the following supplier data into a Pandas DataFrame:

- Australian Business Number (ABN),
- Supplier Name, 
- State, and
- Postcode.

The DataFrame is cleaned and saved in JSONLines format as [ict_supplier_analysis.jsonl](file).

Now there is a clean list of ICT Suppliers in a portable format which can be used for further enrichment and ultimately presentation to our users.

**Database Integration**

**Web Framework & Presentation**

### Charts and Reports

Once the data plumbing and technologies are working in harmony the raw data can be improved, enhanced and presented in such a way that invites the user to explore.

This section deals with cleaning, aggregating and curating (mining) the raw data into more digestable formats for exploration through integrated visualisations.

- data cleaning
- curation of aggregate datasets
- visualisations
