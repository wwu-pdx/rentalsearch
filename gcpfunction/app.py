import flask
from flask.views import MethodView
from index import Index
from add import Add


app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET", 'POST'] )


app.debug = True
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
