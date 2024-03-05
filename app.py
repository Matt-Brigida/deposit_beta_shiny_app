from shiny.express import input, render, ui
import pandas as pd
import plotly.express as px
from shiny.express import input, render, ui
from shinywidgets import render_plotly

betas = pd.read_pickle("./TV_deposit_betas_levels.pkl")
inst = pd.read_csv("./act_inst.csv")

ui.input_selectize(
    "bank", "Select Bank",
     choices = list(inst["NAME"].values)
)

# @render.plot
@render_plotly
def hist():

#    choice_rssd = inst[inst["NAME"] == input.bank()]["FED_RSSD"]
    choice_rssd = inst[inst["NAME"].str.contains(str(input.bank()))]["FED_RSSD"]
    
    df = pd.DataFrame(betas[choice_rssd.values[0]])
    df.columns = ["Beta"]

    fig = px.line(df, y="Beta", title='Time-Varying Deposit Beta Estimate', template='plotly_dark')
    return fig

@render.table
def table():
    only_inst = pd.DataFrame(inst[inst["NAME"].str.contains(str(input.bank()))][["FDICREGN", "CBSA_METRO_NAME",  "CITY", "STALP", "ASSET", "EQ", "DEP", "DEPDOM", "ROA", "ROE"]])
    only_inst.columns = ["FDIC Region", "Metro", "City", "State", "Assets", "Equity", "Deposits", "Domestic Deposits", "ROA", "ROE"]
    return only_inst

