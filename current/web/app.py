from flask import Flask, render_template
from get_stocks import get_stocks, get_higho_lowg, get_pic
import pandas as pd
import utils

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/display_stock_center')
def get_stock_detail():
    data = get_stocks()
    highOpen_lowGo = get_higho_lowg()

    return render_template("stock_details.html",
                           details=data.to_html(classes="table", table_id="stock"),
                           higho_lowg=highOpen_lowGo.to_html(classes="table", table_id="h_l"))

if __name__ == '__main__':
    app.run()
