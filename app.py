from venv import create
from shiny import App, ui, render

# UI

app_ui = ui.page_fluid(

    ui.input_slider("n", "N", 0,100,40),
    ui.output_text_verbatim("txt"),

)


# Server

def server(input, output, session):
    @output
    @render.text

    def txt():
        return f"n*2 is {input.n() * 2}"

app = App(app_ui, server)

