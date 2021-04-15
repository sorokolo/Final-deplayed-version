import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import dash_core_components as dcc
import dash_html_components as html
from apps import logout, failed,login,tabsapps

logout = html.Div([dcc.Location(id='logout', refresh=True)
                      , html.Br()
                      , html.Div(html.H2('You have been logged out - Please login'))
                      , html.Br()
                      , html.Div([login.login])
                      , html.Button(id='back-button', children='Go back', n_clicks=0)
                   ])  # end div
