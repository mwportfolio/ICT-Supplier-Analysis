import logging

from flask import Flask, render_template, request
from google.cloud import datastore
import jsonlines, json
import pandas as pd

app = Flask(__name__)


def getSupplierContracts(ABN):
    client = datastore.Client()
    collection = 'supplier_contracts'
    query = client.query(kind=collection)
    query.add_filter('ABN', '=', ABN)
    query.order = ['-Value']

    results = list(query.fetch())
    contracts = []
    for r in results:
        s = datastore.Entity(r)
        contract = {}
        contract['ContractID'] = s.key.key.name
        contract['Title'] = s.key.get('Title')
        contract['Agency'] = s.key.get('Agency')
        contract['Category'] = s.key.get('Category')
        contract['Value'] = s.key.get('Value')
        contracts.append(contract)
    return contracts


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route("/data/supplier/<ABN>/contracts_by_category")
def supplier_contracts_by_category(ABN):
    contracts = getSupplierContracts(ABN)

    df = pd.DataFrame(contracts)
    sorted_df = df[['Category', 'Value']].groupby('Category').sum().sort_values('Value', ascending=True)
    #sorted_df.reset_index().to_dict('records')
    #t = {'name': 'IT Services', 'value': 6644},{'name': 'Project Management', 'value': 9998}
    return json.dumps(sorted_df.reset_index().to_dict('records'))

@app.route("/data/supplier/<ABN>/contracts_by_agency")
def supplier_contracts_by_agency(ABN):
    contracts = getSupplierContracts(ABN)

    df = pd.DataFrame(contracts)
    sorted_df = df[['Agency', 'Value']].groupby('Agency').sum().sort_values('Value', ascending=True)
    #sorted_df.reset_index().to_dict('records')
    #t = {'name': 'IT Services', 'value': 6644},{'name': 'Project Management', 'value': 9998}
    return json.dumps(sorted_df.reset_index().to_dict('records'))



@app.route("/contracts/supplier/<ABN>")
def supplier_contracts(ABN):

    client = datastore.Client()
    collection = 'supplier_contracts'
    query = client.query(kind=collection)
    query.add_filter('ABN', '=', ABN)
    query.order = ['Title']

    results = list(query.fetch())
    contract_count = len(results)


    contracts = []
    for r in results:
        s = datastore.Entity(r)
        contract = {}
        contract['ContractID'] = s.key.key.name
        contract['Title'] = s.key.get('Title')
        contract['Agency'] = s.key.get('Agency')
        contract['Category'] = s.key.get('Category')
        contract['Value'] = s.key.get('Value')
        contracts.append(contract)

    query_suppliername = client.query(kind='suppliers')
    query_suppliername.add_filter('ABN', '=', ABN)
    results_suppliername = list(query_suppliername.fetch(limit=1))
    supplier_name = datastore.Entity(results_suppliername[0]).key.get('Name')


    return render_template('contracts.html',
        contracts=contracts,
        ABN=ABN,
        supplier_name=supplier_name,
        contract_count=contract_count)



@app.route("/all_suppliers")
def suppliers():

    client = datastore.Client()
    collection = 'suppliers'

    query = client.query(kind=collection)
    query.order = ['Name']

    results = list(query.fetch())
    supplier_count = len(results)


    suppliers = []
    for r in results:
        s = datastore.Entity(r)
        supplier = {}
        supplier['ABN'] = s.key.key.name
        supplier['Name'] = s.key.get('Name')
        supplier['State'] = s.key.get('State')
        supplier['Postcode'] = s.key.get('Postcode')
        suppliers.append(supplier)


    return render_template('suppliers.html', suppliers=suppliers, supplier_count=supplier_count)



if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
