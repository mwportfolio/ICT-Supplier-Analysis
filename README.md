# ICT-Supplier-Analysis

*Analysis of suppliers and contracts for multiple Australian Government ICT Panels.*

### Objective

To implement an analytics application that facilitates interactive analysis of ICT Suppliers to Australian Government.

The application will scrape, store, transform, clean, curate and present data using various technologies and tools including: 
- Apache Spark, BeautifulSoup
- Python, Pandas, Jupyter
- Parquet, JSON, MongoDB
- Flask, Bootstrap, d3

The approach documented below is intended to align with the levels of the Data Value Pyramid (from the bottom moving upwards) as described in Russell Jurny's book: [Agile Data Science 2.0](http://shop.oreilly.com/product/0636920051619.do)

### Records

In order for the analytics application to function as expected a number of technologies and tools must be setup and configured to work together.

This section deals with integrating the analytics stack and enabling efficient data plumbing between the technologies.

- data scrapes and extracts
- optimised storage
- database integration
- web framework & presentation

### Charts and Reports

Once the data plumbing and technologies are working in harmony the raw data can be improved, enhanced and presented in such a way that invites the user to explore.

This section deals with cleaning, aggregating and curating (mining) the raw data into more digestable formats for exploration through integrated visualisations.

- data cleaning
- curation of aggregate datasets
- visualisations
