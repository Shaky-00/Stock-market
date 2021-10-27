from flask import Flask, render_template
from get_stocks import get_stocks, get_higho_lowg
from get_stocks import get_rise_limit, get_drop_limit
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/rise')
def get_rise():
    return utils.get_rise()


@app.route('/drop')
def get_drop():
    return utils.get_drop()


@app.route('/display_stock_center')
def get_stock_detail():
    data = get_stocks()
    highOpen_lowGo = get_higho_lowg()
    rise_limit_stock = get_rise_limit()
    drop_limit_stock = get_drop_limit()

    return render_template("stock_details.html",
                           details=data.to_html(classes="table",
                                                table_id="table1"),
                           higho_lowg=highOpen_lowGo.to_html
                           (classes="table", table_id="table2"),
                           rise_limit=rise_limit_stock.to_html
                           (classes="table", table_id="table3"),
                           drop_limit=drop_limit_stock.to_html
                           (classes="table", table_id="table4"))


if __name__ == '__main__':
    app.run()
