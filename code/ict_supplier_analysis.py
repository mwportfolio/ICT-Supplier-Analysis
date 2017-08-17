from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='/data/all_suppliers'>All Suppliers</a>"

@app.route("/data/all_suppliers")
def all_suppliers():
    f = open("c:/Users/user/ict_panel_suppliers.jsonl", "r")
    suppliers_text = f.read()
    f.close()
    return suppliers_text
