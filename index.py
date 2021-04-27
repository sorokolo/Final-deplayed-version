import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import plotly.graph_objects as go
import orca
import plotly

plotly.io.orca.config.executable = 'orca'
plotly.io.orca.config.save()

import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
from sqlalchemy import Table, create_engine
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import warnings
import os
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser
# Connect to main app.py file
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
import base64
import plotly.graph_objects as go

from app import app
from app import server

from apps import logout, failed, login, tabsapps, temp

warnings.filterwarnings("ignore")
conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()
config = configparser.ConfigParser()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


Users_tbl = Table('users', Users.metadata)

app.config.suppress_callback_exceptions = True
# config
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db.init_app(server)
# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'


# Importing a stylesheet

# Creating a dropdown list
# global list_dict
class Users(UserMixin, Users):
    pass


create = html.Div([

    html.Img(src=app.get_asset_url("thou2.png"), style={
        "display": "block",
        "margin-left": "auto",
        "margin-right": "auto",
        # "width": "50%"

    }),

    html.H2("Thou shalt not pass without authentication!", style={
        "color": "#0F1328",
        "text-align": "center",
        "padding-bottom": "3%"
    }),
    html.Div([html.H1('Create User Account'),
              html.Div([
                  dcc.Location(id='create_user', refresh=True)
                  , html.Br(),
                  html.Div([
                      dcc.Input(id="username"
                                , type="text"
                                , placeholder="user name"
                                , maxLength=15)
                  ], style={"padding": "1%", "color": "black"})
                  , html.Br(),
                  html.Div(
                      dcc.Input(id="password"
                                , type="password"
                                , placeholder="password")
                      , style={"padding": "1%", "color": "black"})

                  , html.Br(),
                  html.Div(
                      dcc.Input(id="email"
                                , type="email"
                                , placeholder="email"
                                , maxLength=50)
                      , style={"padding": "1%", "color": "black"})

                  , html.Br(),
                  html.Div(
                      html.Button('Create User', id='submit-val', n_clicks=0)
                      , style={"padding": "1%"})

                  , html.Br()
                  , html.Br()
                  , html.Br()

                  , html.Div(id='container-button-basic')
              ], style={
                  # "width": "10%"

              })

              ], style={"background-color": "#1C202D", "width": "90%", "padding": "5%",
                        "padding-bottom": "2%",
                        "margin-left": "5%", "color": "white"})  # end div
], style={
    "padding-top": "3%",
    "padding-bottom": "5%"

})

app.layout = html.Div([

    html.Div([
        html.Img(src=app.get_asset_url("thelogo.png")),
        # html.Button(id='back-button1', children='Go back', n_clicks=0)

    ], style={"background-color": "#0F1328",
              "border - bottom - style": "solid"
              }),
    html.Div(id='page-content', className='content')
    , dcc.Location(id='url', refresh=False)
])

app.clientside_callback(
    '''
    function (chart_children,chart_children2,chart_children3,chart_children4,chart_children5,total_revenue,rate_of_change,data_picker,dropdown_id,dropdown_id1) {
        if (chart_children.type == "Img") {

            var doc = new PDFDocument({layout:'landscape', margin: 40});
            var stream = doc.pipe(blobStream());

            doc.fontSize(28);
            doc.font('Helvetica-Bold');
            doc.text('YOUR PRINTED REPORT: ', 20, 40);


            doc.text('Total Revenue: ', 20, 120);
            console.log(total_revenue);
            doc.text(total_revenue, 20, 160);

            doc.text('Rate of change: ', 20, 240);
            console.log(rate_of_change);
            doc.text(rate_of_change, 20, 280);

            console.log(chart_children);
            doc.addPage().fontSize(12);
            doc.image(chart_children.props.src, {width: 700});


            console.log(chart_children2);
            doc.addPage().fontSize(12);
            doc.image(chart_children2.props.src, {width: 700});

            console.log(chart_children3);
            doc.addPage().fontSize(12);
            doc.image(chart_children3.props.src, {width: 700});

            console.log(chart_children4);
            doc.addPage().fontSize(12);
            doc.image(chart_children4.props.src, {width: 700});

            console.log(chart_children5);
            doc.addPage().fontSize(12);
            doc.image(chart_children5.props.src, {width: 700});



            doc.end();

            var saveData = (function () {
                var a = document.createElement("a");
                document.body.appendChild(a);
                a.style = "display: none";
                return function (blob, fileName) {
                    var url = window.URL.createObjectURL(blob);
                    a.href = url;
                    a.download = fileName;
                    a.click();
                    window.URL.revokeObjectURL(url);
                };
            }());

            stream.on('finish', function() {

              var blob = stream.toBlob('application/pdf');
              saveData(blob, 'Report.pdf');

                // iframe.src = stream.toBlobURL('application/pdf');
            });
        }
        return 0;
    }
    ''',
    [Output('graph_img', 'n_clicks'),
     ],
    [
        Input('graph_img', 'children'),
        Input('graph_img2', 'children'),
        Input('graph_img3', 'children'),
        Input('graph_img4', 'children'),
        Input('graph_img5', 'children'),
        Input('output_container', 'children'),
        Input('output_container1', 'children')
    ]
)


@app.callback(
    [Output('graph_img', 'children'),
     Output('graph_img2', 'children'),
     Output('graph_img3', 'children'),
     Output('graph_img4', 'children'),
     Output('graph_img5', 'children'),

     ],
    [
        Input('button', 'n_clicks')
    ],
    [
        State('product', 'figure'),
        State('location', 'figure'),
        State('month_year', 'figure'),
        State('paiement', 'figure'),
        State('predict', 'figure'),

    ]
)
def figure_to_image(n_clicks, figure_dict, figure_dict2, figure_dict3, figure_dict4, figure_dict5):
    if n_clicks:
        # Higher scale = better resolution but also takes longer/larger size
        figure = go.Figure(figure_dict)
        img_uri = figure.to_image(format="png", scale=1)
        src = "data:image/png;base64," + base64.b64encode(img_uri).decode('utf8')

        figure2 = go.Figure(figure_dict2)
        img_uri2 = figure2.to_image(format="png", scale=1)
        src2 = "data:image/png;base64," + base64.b64encode(img_uri2).decode('utf8')

        figure3 = go.Figure(figure_dict3)
        img_uri3 = figure3.to_image(format="png", scale=1)
        src3 = "data:image/png;base64," + base64.b64encode(img_uri3).decode('utf8')

        figure4 = go.Figure(figure_dict4)
        img_uri4 = figure4.to_image(format="png", scale=1)
        src4 = "data:image/png;base64," + base64.b64encode(img_uri4).decode('utf8')

        figure5 = go.Figure(figure_dict5)
        img_uri5 = figure5.to_image(format="png", scale=1)
        src5 = "data:image/png;base64," + base64.b64encode(img_uri5).decode('utf8')

        return html.Img(src=src), html.Img(src=src2), html.Img(src=src3), html.Img(src=src4), html.Img(src=src5)
    return ''


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.callback(
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return create
    elif pathname == '/login':
        return login.login
    elif pathname == '/success':
        if current_user.is_authenticated:
            return tabsapps.success
        else:
            return failed.failed
            # return login
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return logout.logout
        else:
            return logout.logout
    else:
        return '404'


@app.callback(
    [Output('container-button-basic', "children")]
    , [Input('submit-val', 'n_clicks')]
    , [State('username', 'value'), State('password', 'value'), State('email', 'value')])
def insert_users(n_clicks, un, pw, em):
    hashed_password = generate_password_hash(pw, method='sha256')
    if un is not None and pw is not None and em is not None:
        ins = Users_tbl.insert().values(username=un, password=hashed_password, email=em, )
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return [login.login]
    else:
        return [html.Div([html.H2('Already have a user account?'), dcc.Link('Click here to Log In', href='/login')])]


@app.callback(
    Output("url_login", 'pathname')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def successful(n_clicks, input1, input2):
    user = Users.query.filter_by(username=input1).first()
    if user:
        if check_password_hash(user.password, input2):
            login_user(user)
            return '/success'
        else:
            pass
    else:
        pass


@app.callback(
    Output('output-state', 'children')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = Users.query.filter_by(username=input1).first()
        if user:
            if check_password_hash(user.password, input2):
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''


@app.callback(
    Output('url_login_success', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'


@app.callback(
    Output('url_login_df', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'


# Create callbacks
@app.callback(
    Output('url_logout', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'


if __name__ == '__main__':
    app.run_server(debug=False)
