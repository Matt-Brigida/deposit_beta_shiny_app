from shiny.express import input, render, ui
import pandas as pd

betas = pd.read_pickle("./TV_deposit_betas_levels.pkl")
inst = pd.read_csv("./act_inst.csv")

ui.input_selectize(
    "bank", "Select Bank",
     choices = list(inst["NAME"].values)
)

@render.plot
#@render.text
def hist():
    from matplotlib import pyplot as plt
    plt.style.use('dark_background')

#    choice_rssd = inst[inst["NAME"] == input.bank()]["FED_RSSD"]
    choice_rssd = inst[inst["NAME"].str.contains(str(input.bank()))]["FED_RSSD"]
#    return str(choice_rssd)
#    return input.bank()
    betas[choice_rssd.values[0]].plot()

#    betas[int(input.bank())].plot()

