from venv import create
from shiny import App, ui,  render

# UI

app_ui = ui.page_fluid(
    ui.navset_pill(
        ui.nav("About me",
        ui.page_fluid(
            ui.panel_title(
                "Who am I?"
            ),
            ui.layout_sidebar(
                ui.panel_sidebar(
                    ui.output_ui("name"),
                    ui.output_text("me")
                ),
                ui.panel_main(
                    ui.output_ui("photo")
                )
            )
        )
        ),

        ui.nav_control(
            ui.a("GitHub", href = "https://github.com/antonioespinoza98", target = "_blank")
            ),

        ui.nav_control(
            ui.a("Instagram", href = "https://www.instagram.com/marco_espinoza/", target = "_blank")
            ),
        ui.nav_control(
            ui.a("LinkedIn", href = "https://www.linkedin.com/in/marco-antonio-espinoza-marin-5365a1176/", target="_blank")
        )
    )

)


# Server

def server(input, output, session):
    @output
    @render.ui

    def name():
        return ui.HTML("<marquee>My name is Marco Espinoza!</marquee>")

    @output
    @render.text
    def me():
        return "I am currently working as a Data Analyst/Engineer. I am also a student finishing my bachelor's degree in statistics at the University of Costa Rica. My professional interests are data engineering and data analysis using complex statistical models. In addition, I have a great passion for music, so I like to play the guitar and go to local music venues. I also like art and I am in the process of learning how to paint on canvas because in the future I want to develop a project called Timeline that consists of a series of paintings that relate important memories in my life. I also have a great passion for analog photography."

    @output
    @render.ui

    def photo():
        return ui.HTML("<a href='https://pbs.twimg.com/media/FSg-V9UUUAAU6MO?format=jpg&name=small'><img src='https://pbs.twimg.com/media/FSg-V9UUUAAU6MO?format=jpg&name=small' alt='MDN' width='500' height='600'></a>")
app = App(app_ui, server)

