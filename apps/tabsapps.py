import warnings
import itertools
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import statsmodels.api as sm
import statistics
from datetime import date
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from pandas import Timestamp
import io
import base64
import pandas as pd
import dash
from dash.dependencies import Input, Output, State
import warnings
import dash_daq as daq
from app import app



tab_selected_style = {
    'borderTop': '#FBEF3C',
    'borderRight': 'None',
    'backgroundColor': '#FBEF3C',
    'color': 'black',
    'fontWeight': 'bold'

}
tab_style = {
    'backgroundColor': '#0F1328',
    'fontWeight': 'bold',
    'color': 'white',
    # 'borderTop': '#FBEF3C',
    'borderBottom': 'None',
    # 'borderLeft': 'None',
    'borderRight': 'None',

}

tab_selected_style1 = {
    'borderTop': '#FBEF3C',
    'borderLeft': 'None',
    'borderRight': 'None',
    'backgroundColor': '#FBEF3C',
    'color': 'black',
    'fontWeight': 'bold'

}
tab_style1 = {
    'backgroundColor': '#0F1328',
    'fontWeight': 'bold',
    'color': 'white',
    'borderBottom': 'None',
    'borderLeft': 'None',
    'borderRight': 'None',

}


external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
        'crossorigin': 'anonymous'
    }
]
#
# global list_dict
list_dict = []

success = html.Div([
html.Div([
dcc.Tabs([
    dcc.Tab(label='Welcome', children=[
        html.Div([
            html.Br(),
            html.Br(),
            html.H3("Welcome to", style={
                "color": "white",
                "text-align": "center",

            }),

            html.H2("AZTECH DIGITAL SOLUTIONS", style={
                "color": "#92E0D3",
                "text-align": "center",


            }),

            html.H4("Aztech Digital is a business analytics tool that aims at providing non-data science savvies with the opportunity to turn data-driven."
                    "If you hold a business and do not have the technical knowledge or staff to handle your daily operations and transactions, this is the place for you."
                    "A business analytics platform that allows transaction registration companies monitor the performance of their business (Small and medium sized enterprises)."
                    ,
                style={
                "color": "white",
                "text-align": "Justify",
                "font-family":"Montserrat",
                "width": "60%",

                "font-size": "20px",
                "margin-left": "20%"

                   }
                    ),
            html.H4(
                "You will find below the steps to be able to use this application successfully."
                ,
                style={
                    "color": "white",
                    "text-align": "Justify",
                    "font-family": "Montserrat",
                    "width": "60%",

                    "font-size": "20px",
                    "margin-left": "20%"

                }
                ),



            html.Br(),
            html.Br(),
            html.Div([
                html.Div([
                    html.Img(src=app.get_asset_url("avail.png"),style={
                                       "display": "block",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "width": "50%"

                    }),
                    html.H5("Available Everywhere", style={"color":"#92E0D3",'text-align': 'center',
                                                           # "font-family":"Montserrat",
                                                           "font-size": "15px"
                                                           }),
                    html.H5("Have your application available to you everywhere on every device 24/7 ", style={
                         'text-align': 'center',
                        "color": "white"
                        , "font-family": "Montserrat"

                    })
                ], className="three columns"),


                html.Div([
                    html.Img(src=app.get_asset_url("click.png"),style={
                        "display": "block",
                        "margin-left": "auto",
                        "margin-right": "auto",
                        "width": "50%"
                    }),
                    html.H5("Easy to use", style={"color": "#92E0D3", 'text-align': 'center',
                                                  # "font-family": "Montserrat",
                                                  "font-size": "15px"
                                                  }),
                    html.H5("With our pre-made dashboard and predictive tools, only focus receiving insights", style={
                        'text-align': 'center',
                        "color": "white"
                        , "font-family": "Montserrat"

                    })
                ],className="three columns"),
                html.Div([
                    html.Img(src=app.get_asset_url("customerservice.png"),style={
                        "display": "block",
                        "margin-left": "auto",
                        "margin-right": "auto",
                        "width": "50%"
                    }),
                    html.H5("Expert Support", style={"color": "#92E0D3", 'text-align': 'center',
                                              # "font-family": "Montserrat",
                                              "font-size": "15px",

                                              }),
                    html.H5("Get support from our team for further and advanced analytics", style={
                        'text-align': 'center',
                        "color": "white"
                        , "font-family": "Montserrat"

                    })

                ],className="three columns"),
                html.Div([
                    html.Img(src=app.get_asset_url("interactive.png"),style={
                        "display": "block",
                        "margin-left": "auto",
                        "margin-right": "auto",
                        "width": "50%"
                    }),
                    html.H5("Interactive Usage", style={"color": "#92E0D3", 'text-align': 'center',
                                                  # "font-family": "Montserrat",
                                                  "font-size": "15px",

                                                  }),
                    html.H5("Interact on with analytics as if you made", style={
                        'text-align': 'center',
                        "color": "white"
                        ,"font-family": "Montserrat"

                    })


                ],className="three columns"),

            ],className="row",style={"width":"70%","margin-left": "16%"

                }),

            # Get started
            html.Br(),
            html.Br(),
            html.H3("HOW TO GET STARTED", style={"color":"#F4D44D", 'text-align': 'center',}),
            html.Div([

            html.H3('STEP 1', style={'text-align': 'Left', "color":"#F4D44D"}),
            html.H4(
                'Use our template sheet to record your transaction, note that for better and faster'
                'processing, this the names of the columns shouldnt be change . The sheet mainly consists of rows to'
                'records your sales/transactions, their dates, amount and some other categorizations.'
                , style={'text-align': 'Justify', "color":"white"
                         ,"font-family":"Montserrat"

                         }),
                html.A("Template Sheet",
                       href='https://docs.google.com/spreadsheets/d/1jHhDxHi_2IhJZFDEOrOS7xhm1OORrgPOAL1l2O-XTzs/edit?usp=sharing',
                       target="_blank",style={"color":"#85E0D3"
                        , "font-family": "Montserrat"

                                              }),
            html.Br(),
            html.H3('STEP 2', style={'text-align': 'Left', "color": "#F4D44D"}),
            html.H4(
                'When you reach a stage of your data and feel you need some insights, download the data '
                'as a xlsx, csv, txt and tsv file and'
                'uppload it below, this is the data that will be used to construct all the analytics. '
                'Note that the data you enter is local and we do not keep track of your data. '
                'The below columns should appear in your data. '
                'There will be more explanation about what you should do to the above sample when you open it. '
                , style={'text-align': 'Justify', "color": "white"

                         ,"font-family":"Montserrat"
                         }),


                html.H4(
                    "Source    |    Product    |    Amount    |    Date    |    Location    |    Payment    |    Mode"
                    , style={'text-align': 'Justify', "color": "white"

                        , "font-family": "Montserrat"
                             }),

            html.Br(),
            html.H3('STEP 3', style={'text-align': 'Left', "color": "#F4D44D"}),
            html.H4(
                "After upploading your data you can head to the other tabs tabs, where the"
                "information is now updated."
                , style={'text-align': 'Justify', "color": "white"
                    , "font-family": "Montserrat"

                         }),

            html.Br(),
            html.Br(),

                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ], style={"color":"white"}),
                    style={
                        'width': '80%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderColor': 'white',
                        "font-family":"Montserrat",
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        "margin-left":"10%",
                        # 'margin': '20px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=False
                ),
                html.Br(),

                html.Div(id='output_container3', children=[],style={"color":"green",'text-align': 'center', "font-size":"20px"
                    , "font-family": "Montserrat"

                                                                    }),

            ],style={

                "width":"80%",

                "margin-left": "11%", "background-color":"#1C202D", "padding":"7%"
 })

            ],
    style={
        "margin": "5%",
         "padding": "5%x",
        "padding-bottom":"5%",
         "background-color":"#0F1328",
        "width": "90%", "border": "3px",
        "margin-left": "5%",
           }
        ),


        ],style=tab_style1,selected_style=tab_selected_style1),


        dcc.Tab(id = "your_dashbord",label='Your Dashboard', children=[
            # Layer for 80% width
            html.H2("YOUR DASHBOARD", style={
                "color": "#92E0D3",
                "text-align": "center",
            }),
    html.Div([

        # Start of div slider
        html.Div([

            html.Br(),
            html.H4("Total Revenue", style={'text-align': 'left',"color":"white", "font-family":"monospace","margin": "5%",}),
            html.Div(id='output_container', children=[],
                     style={
                            "color":'#92E0D3',
                            "font-size": "150%",
                            # "border-color": "coral",
                            "border":"1px solid white",
                            "width": "80%",
                            "background-color":"#1B1E2B",
                         "font-family": "Roboto",

                         "padding":"5%",
                            "margin": "10%",
                            'text-align': 'center'

                     }),
            html.Br(),
                    html.H4("Rate of change", style={'text-align': 'left',"color":"white", "font-family":"monospace","margin": "5%",}),
                    html.Div(id='output_container1', children=[],
                     style={
                            "color":'#92E0D3',
                            "font-size": "150%",
                            "border":"1px solid white",
                            "width": "80%",
                            "font-family":"Roboto",
                            "background-color":"#1B1E2B",
                            "padding":"5%",
                            "margin": "10%",
                            'text-align': 'center'
                     }),
            html.Br(),
                    html.H4("No Products", style={'text-align': 'left',"color":"white", "font-family":"monospace","margin": "5%",}),
                                        html.Div(id='output_container10', children=[],
                                         style={
                                                "color":'#92E0D3',
                                                "font-size": "150%",
                                                "border":"1px solid white",
                                                "width": "80%",
                                                "font-family":"Roboto",
                                                "background-color":"#1B1E2B",
                                                "padding-top": "5%",
                                                 "padding-bottom": "5%",
                                                "margin": "10%",
                                                'text-align': 'center'
                                         }),
            html.Br(),
            html.H4("No Payment",
                    style={'text-align': 'left', "color": "white", "font-family": "monospace", "margin": "5%", }),
            html.Div(id='output_container11', children=[],
                     style={
                         "color": '#92E0D3',
                         "font-size": "150%",
                         "border": "1px solid white",
                         "width": "80%",
                         "font-family": "Roboto",
                         "background-color": "#1B1E2B",
                         "padding-top": "5%",
                         "padding-bottom": "5%",
                         "margin": "10%",
                         'text-align': 'center'
                     }),

            html.Div(id="data_picker", children =[
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=date(1995, 1, 1),
                max_date_allowed=date(2030, 1, 1),
                initial_visible_month=date(2021, 2, 10),
                end_date=date(2021, 4, 1),
                stay_open_on_select = True,
            ),
],                style={
                    "border": "4px solid Yellow",
                    "color":"#9A3E49",
                    "width":"85%",
                    "margin":"7%"
            },),

            html.Br(),

            html.Div(id = "output_container4",style={'background-color': '#0F1328',"color":"#9A3E49"},),


        ],className="two columns",style={"background-color":"#0F1328",
                                         # "height":"100%",
                                            "margin":'1%'
                                         }),
        # End of div slider

        # Layer for the graphs
        html.Div([
            # Layer for the first row
            html.Div([
                html.Div([ dcc.Graph(id='product', figure={}), ], className="six columns"),

                html.Div([dcc.Graph(id='location', figure={}),], className="six columns",style={"margin-left": "1%"}) ],
            className="row",style={"margin":'1%'}),

                      # Layer for the second row
            html.Div([
                html.Div([dcc.Graph(id='month_year', figure={}),], className="six columns"),
                html.Div([dcc.Graph(id='paiement', figure={}), ], className="six columns",style={"margin-left": "1%"}),
            ],className="row",style={"margin":'1%'}),


            # End of second row
             ],className="ten columns",style={
            "margin-left": "-1%"
        }),
             # End of div graph

# <-------------------->
],className="row",style={
                        "margin": "auto", "width": "95%", "border": "3px",
                         # "background-color":"#0F1328",
                         #    "display":'flex',
                            "margin-left": "5%",
                         # "padding": "5%",
                         })
        ],style=tab_style,selected_style=tab_selected_style),


        dcc.Tab(label='ForeCasting',children=[
            html.Div([
                html.H2("CASH FLOW FORECAST", style={
                    "color": "#92E0D3",
                    "text-align": "center",
                    "padding-bottom":"1%"
                }),
                html.Div([
            dcc.Graph(id='predict', figure={})], style={
                    # "padding": "5%",
                    # "padding-bottom": "1%"

                }),
            html.Div(id='output_container5', children=[]
                     ,style=
            {
                # "margin-left":"1%",
                # "padding":"1%"
            }
                     ),

            html.H3("Please Enter the number months you want to forcast for",style={"color":"white", "text-align":"center"}),
            daq.NumericInput(
                                labelPosition='bottom',
                                id='my-numeric-input',
                                size=120,
                                min=0,
                                max=10000,
                                value=100,
                                # style={bla}
                            ),
        ],style={
                # "padding":"5%",
                "padding-left":"5%",
                "padding-right": "5%",
                "padding-bottom": "5%",
                "padding-top":"0.5%"})

    ], style=tab_style,selected_style=tab_selected_style),

    dcc.Tab(label='Download and Contact', children=[

        html.Div([
        html.H2("Contact Information", style={
            "color": "#92E0D3",
            "text-align": "center",
        }),

        html.H4("If you have advanced needs or would like a customized dashboard, reach out to us using the below information", style={
            "color": "white",
            "text-align": "center",
        }),
        html.Br(),

        html.H4("Email : ksoro17@alustudent.com", style={
            "color": "white",
            "text-align": "center",
        }),
        html.H4("Phone Number : +250784649249", style={
            "color": "white",
            "text-align": "center",
        }),

        html.Br(),
        html.Br(),
        html.Br(),

        html.Button('Print Report', id='button', n_clicks=0,
                    style={
                        "border": "4px solid Yellow",
                        "color": "white",
                        "display": "block",
                        "margin-left": "auto",
                        "margin-right": "auto",
                    }
                    ),

        html.H2("The downloaded State", style={
            "color": "#92E0D3",
            "text-align": "center",
        }),

        html.Div([
        html.Div(id='graph_img', style={"width":"50%"}),
        html.Div(id='graph_img2', style={"width":"50%"}),
        html.Div(id='graph_img3', style={"width":"50%"}),
        html.Div(id='graph_img4', style={"width":"50%"}),
        html.Div(id='graph_img5', style={"width":"50%"}),

        ], style={"width":"80%",
                  "margin-left":"21%",
                'borderColor': 'white',}),

        ],style={ "padding":"5%", "padding-bottom":"10%",})


    ], style=tab_style, selected_style=tab_selected_style),












]),

    # <-------------------->
],style={
    "position": "relative",
    "background-color":"#1E2130"
})

])



def parse_data(contents, filename):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV or TXT file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        elif "txt" or "tsv" in filename:
            # Assume that the user upl, delimiter = r'\s+'oaded an excel file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter=r"\s+")
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df


def pdq_paramaters(y):
    p = d = q = range(0, 2)

    # Generate all different combinations of p, q and q triplets
    pdq = list(itertools.product(p, d, q))

    # Generate all different combinations of seasonal p, q and q triplets
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

    # specify to ignore warning messages
    param_list=[]
    warnings.filterwarnings("ignore")
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)

                results = mod.fit()

                # print('SARIMAX{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                param_list.append([param,param_seasonal,results.aic])
            except:
                continue
    return param_list

# Computing the best index
def area_constructer(param_list):
    area_under_list = []
    for i in range(len(param_list)):
        area_under_list.append(param_list[i][2])
    return area_under_list


def index_finder(area_under_list, param_list):
    temp_list = []
    for i in range(len(area_under_list)):
        if (area_under_list[i] == min(area_under_list)):
            temp_list.append([statistics.mean(param_list[i][0]), i])

    second_temp = []
    for i in range(len(temp_list)):
        second_temp.append(temp_list[i][0])

    for i in range(len(temp_list)):
        if temp_list[i][0] == max(second_temp):
            return temp_list[i][1]



@app.callback(
    dash.dependencies.Output('predict', 'figure'),
    [
    dash.dependencies.Input('my-numeric-input', 'value'),
    dash.dependencies.Input('dropdown-id1', 'value'),
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
     ])
def update_output_line1(days,value,content,filename):
    df = parse_data(content, filename)
    df = df[df["Product"].isin(value)]
    df['Date'] = pd.to_datetime(df['Date'])
    data = df[['Date', 'Amount']]
    forcast_data = data.groupby('Date')['Amount'].sum().reset_index()
    y = pd.read_csv(io.StringIO(u"" + forcast_data.to_csv(index=False)),
                    header=0,
                    index_col=0,
                    parse_dates=True,
                    squeeze=True,
                    )
    y.index = pd.to_datetime(y.index)

    param_list = pdq_paramaters(y)
    area_under_list = area_constructer(param_list)
    best_index = index_finder(area_under_list, param_list)

    p = param_list[best_index][0][0]
    d = param_list[best_index][0][1]
    q = param_list[best_index][0][2]
    r = param_list[best_index][1][0]
    s = param_list[best_index][1][1]
    t = param_list[best_index][1][2]
    u = param_list[best_index][1][3]

    # fiiting the arima model
    mod = sm.tsa.statespace.SARIMAX(y,
                                    order=(p, d, q),
                                    seasonal_order=(r, s, t, u),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)

    results = mod.fit()

    # Get forecast 500 steps ahead in future
    pred_uc = results.get_forecast(steps=days)

    # Get confidence intervals of forecasts
    pred_ci = pred_uc.conf_int()

    # Creating the datetime list
    datelist = pd.date_range(y.index[len(y) - 1], periods=days).tolist()

    # Setting l.index a date list
    l = pred_uc.predicted_mean
    l.index = datelist

    # converting l.index to datetime
    l.index = pd.to_datetime(l.index)
    # Converting pred_ci to
    pred_ci.index = datelist
    y_values = list(y.values)

    predictted_values = list(l.values)
    Total_values = y_values + predictted_values
    y_index = list(y.index)
    predictted_index = list(l.index)
    Total_indexes = y_index + predictted_index

    Total_labels = []
    for i in range(len(y_values)):
        Total_labels.append("Observed")

    for i in range(len(predictted_values)):
        Total_labels.append("Forcast")

    list_of_tuples = list(zip(Total_indexes, Total_values, Total_labels))
    prediction_plot = pd.DataFrame(list_of_tuples,
                                   columns=['Dates', 'Values', 'Labels'])

    fig = px.line(
        data_frame=prediction_plot,
        x='Dates',
        y='Values',
        color='Labels',
        template='plotly_dark'
    )
    fig.update_layout(
        plot_bgcolor="#0F1328",
        paper_bgcolor="#0F1328",
        font_color="#fff",
        xaxis_title = 'Date',
        yaxis_title = 'Time Period',
        title={
        'text': "Observed and Predicted Revenue",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        font=dict(
        family="sans serif",
        ),
        title_font_size=20,
    )
    return fig

@app.callback(
   [dash.dependencies.Output('product', 'figure'),
    Output(component_id='output_container', component_property='children'),
    Output(component_id='output_container1', component_property='children'),
    Output(component_id='output_container3', component_property='children'),
    Output(component_id='output_container4', component_property='children'),
    Output(component_id='output_container5', component_property='children'),

    ],
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename'),
     dash.dependencies.Input('prod_num', 'value'),

     ])

def update_output(start_date, end_date,content,filename,value):
    df = parse_data(content, filename)
    df['Date'] = pd.to_datetime(df['Date'])
    for i in df['Product'].unique():
        dicti = {}
        dicti['label'] = i
        dicti['value'] = i
        list_dict.append(dicti)


    print(list_dict)

    document = filename+" "+" was Loaded sucessfully"


    print(df)
    if(start_date==None):
        start_date = Timestamp('2021-02-01 00:00:00')

    mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
    product_df = df.loc[mask]
    final = product_df.groupby(['Product'])['Amount'].sum().reset_index()

    top_final = final.nlargest(value, 'Amount')

    Final = product_df['Amount'].sum()
    Value1 = df[df['Date']==start_date]["Amount"].sum()
    Value2 = df[df['Date']==end_date]["Amount"].sum()



    container1 = ""
    if Value1==0:
        container1 += "-"
    else:
        container_value = ((Value2/Value1)-1)*100
        container1 += str(round(container_value, 2))+""+"%"

    container = Final

    fig = px.pie(top_final, values=top_final['Amount'], names=top_final['Product'])
    fig.update_layout(
        plot_bgcolor="#0F1328",
        paper_bgcolor="#0F1328",
        font_color="#fff",
        xaxis_title = 'Products',
        yaxis_title = 'Aggregated Revenue',
        # margin=dict(t=50),
        title={
        'text': "Top Revenue Producers",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        font=dict(
        family="sans serif",
        ),
        title_font_size=20,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=10
        ),
    )

    return fig,container,container1,document,dcc.Dropdown(
        id='dropdown-id',
        options=list_dict,
        value=[list_dict[0]['label']],
        style={'background-color': '#0F1328', "color": "#9A3E49", "width": "90%", "margin": "5%"},
        multi=True
        , searchable=True
    ),dcc.Dropdown(
        id='dropdown-id1',
        options=list_dict,
        value=[list_dict[0]['label']],
        style={
            'background-color': '#1E2130',
             "color": "#9A3E49",
            "padding-bottom":"1%"
        },
        multi=True
        , searchable=True
    )


# Plot for the pie(product chart)
@app.callback(
    dash.dependencies.Output('paiement', 'figure'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename'),
     dash.dependencies.Input('paiement_num', 'value')

     ])
def update_output_bar(start_date, end_date,content,filename,value):
    df = parse_data(content, filename)
    df['Date'] = pd.to_datetime(df['Date'])
    if(start_date==None):
        start_date = Timestamp('2021-02-01 00:00:00')
    mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
    product_df = df.loc[mask]
    final = product_df.groupby(['Payment Mode'])['Amount'].sum().reset_index()

    top_final = final.nlargest(value, 'Amount')


    fig = px.bar(
        data_frame=top_final,
        y='Payment Mode',
        x='Amount',
        orientation='h',
        hover_data=['Payment Mode', 'Amount'],
        labels={'Payment Mode': 'turnover'},
        template='plotly_dark'
    )
    fig.update_layout(
        plot_bgcolor="#0F1328",
        paper_bgcolor="#0F1328",
        font_color="#fff",
        xaxis_title = 'Payment Mode',
        yaxis_title = 'Aggregated Revenue',
        title={
        'text': "Top Payment mode",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        font=dict(
        family="sans serif",
        ),
        title_font_size=20,
    )

    return fig


# Line chart
@app.callback(
    dash.dependencies.Output('month_year', 'figure'),

    [dash.dependencies.Input('dropdown-id', 'value'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename'),
     ])
def update_output_line(value,content,filename):
    df = parse_data(content, filename)


    df['Date'] = pd.to_datetime(df['Date'])
    month_year = df.groupby(['Date',"Location",'Product'])['Amount'].sum().reset_index()
    dff = month_year[month_year["Product"].isin(value)]

    fig = px.line(
        data_frame=dff,
        x='Date',
        y='Amount',
        template='plotly_dark',
        color = 'Product',

    )

    fig.update_layout(
        plot_bgcolor="#0F1328",
        paper_bgcolor="#0F1328",
        font_color="#fff",
        xaxis_title = 'Date',
        yaxis_title = 'Aggregated Revenue',
        title={
        'text': "Revenue Over the Year",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        font=dict(
        family="sans serif",
        ),
        title_font_size=20,
    )
    return fig


# Scatter plot
@app.callback(
    [dash.dependencies.Output('location', 'figure'),
     Output(component_id='output_container10', component_property='children'),
     Output(component_id='output_container11', component_property='children')],
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename')
     ])

def update_output_scatter(start_date, end_date,content,filename):
    df = parse_data(content, filename)
    number_value_prod = len(df['Product'].unique())
    number_value = len(df['Payment Mode'].unique())
    df['Date'] = pd.to_datetime(df['Date'])
    if(start_date==None):
        start_date = Timestamp('2021-02-01 00:00:00')
    mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
    location_df = df.loc[mask]

    final = location_df.groupby(['Location'])['Amount'].sum().reset_index()
    final1 = location_df.groupby(['Location'])['Amount'].count().reset_index()
    final1.columns = ["location", "count"]
    final['Count'] = final1['count']

    fig = px.scatter(final, x="Count", y="Amount",
                     size="Count", color="Location",
                     hover_name="Location", log_x=True, size_max=60)
    fig.update_layout(
        plot_bgcolor="#0F1328",
        paper_bgcolor="#0F1328",
        font_color="#fff",
        xaxis_title = 'Transaction Count',
        yaxis_title = 'Aggregated Revenue',
        title={
        'text': "Revenue Repartition per Location",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        font=dict(
        family="sans serif",
        ),
        title_font_size=20,
    )
    return fig,daq.NumericInput(
                labelPosition='bottom',
                id='prod_num',
                size=120,
                min=0,
                max=number_value_prod,
                value=number_value_prod,
                     ),daq.NumericInput(
                    labelPosition='bottom',
                    id='paiement_num',
                    size=120,
                    min=0,
                    max=number_value,
                    value=number_value,
                )



