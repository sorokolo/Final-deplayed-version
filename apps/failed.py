import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import dash_core_components as dcc
import dash_html_components as html
from apps import logout,login,tabsapps


failed = html.Div([dcc.Location(id='url_login_df', refresh=True)
                      , html.Div([html.H2('Log in Failed. Please try again. and refresh the page')
                                     , html.Br()
                                     , html.Div([login.login])
                                     , html.Br()
                                     , html.Button(id='back-button', children='Go back', n_clicks=0)
                                  ])  # end div
                   ])  # end div
