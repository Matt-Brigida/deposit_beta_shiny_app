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
#@render.text
def hist():
    #    from matplotlib import pyplot as plt
#     plt.style.use('dark_background')

#    choice_rssd = inst[inst["NAME"] == input.bank()]["FED_RSSD"]
    choice_rssd = inst[inst["NAME"].str.contains(str(input.bank()))]["FED_RSSD"]
    
    df = pd.DataFrame(betas[choice_rssd.values[0]])
    df.columns = ["Beta"]

    # betas[choice_rssd.values[0]].plot()
    fig = px.line(df, y="Beta", title='Time-Varying Deposit Beta Estimate', template='plotly_dark')
    return fig

