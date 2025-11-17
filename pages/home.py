import pandas as pd
import streamlit as st
from core.router import BasePage
from core.layout import centered_content


class HomePage(BasePage):
    @property
    def name(self) -> str:
        return "Home"

    def render(self) -> None:

        st.markdown("""
        <style>
        /* Set a minimum width for the entire page content area */
        [data-testid="stAppViewContainer"] {
            min-width: 1100px !important;   /* <<< adjust this number */
        }

        /* Optional: horizontally scroll if the window is smaller than min-width */
        body {
            overflow-x: auto !important;
        }
        </style>
        """, unsafe_allow_html=True)

        with centered_content():
            st.header("Willkommen beim Tischtennis Bad Aibling")
            st.write(
                "Hier findest du alle Informationen rund um unseren Verein, "
                "unsere Mannschaften und aktuelle Neuigkeiten."
            )
            st.image("assets/übersicht.jpg", "Verein", width="content", use_column_width=None,
                     clamp=False, channels="RGB", output_format="auto", use_container_width=None)


            _render_training_tables()

            st.markdown("---")

            _render_team_section()



def _get_team_members() -> list[dict]:
    """Return static data for team members."""
    return [
        {
            "role": "Spartenleiter",
            "name": "Alexander Zilken",
            "email": "spartenleiter@tus-bad-aibling.de",
        },
        {
            "role": "Vizespartenleiter & Jugendwart",
            "name": "Florian Ludwig",
            "email": "jugendwart@tus-bad-aibling.de",
        },
        {
            "role": "Jugendtrainer",
            "name": "Richard Remmelberger",
            "email": "jugendtrainer@tus-bad-aibling.de",
        },
    ]


def _render_team_section():
    st.header("Team")

    members = _get_team_members()

    columns = st.columns([1, 1, 1])


    for (i, m), col in zip(enumerate(members), columns):
        with col:
            st.markdown(f"""
                **{m['role']}**  
                {m['name']}  
                [{m['email']}](mailto:{m['email']})
            """)
            if i < len(members) - 1:
                st.markdown("---")


def _get_training_data() -> dict[str, pd.DataFrame]:
    """Return dataframes for each training group."""
    jugend = pd.DataFrame(
        {
            "Tag": ["Montag", "Mittwoch"],
            "Uhrzeit": ["17:00 – 19:00", "17:00 – 19:00"],
        }
    )

    erwachsene = pd.DataFrame(
        {
            "Tag": ["Montag", "Mittwoch", "Freitag"],
            "Uhrzeit": ["19:00 – 22:00", "19:00 – 22:00", "19:00 – 22:00"],
        }
    )

    hobby = pd.DataFrame(
        {
            "Tag": ["Dienstag", "Donnerstag"],
            "Uhrzeit": ["19:00 – 22:00", "19:00 – 22:00"],
        }
    )

    return {
        "Jugend": jugend,
        "Erwachsene": erwachsene,
        "Erwachsene (Hobby Spieler)": hobby,
    }


def _render_training_tables():
    st.header("Trainingszeiten")

    for title, df in _get_training_data().items():
        df.index = [''] * len(df)
        st.subheader(title)
        st.table(df.style.hide(axis="index"))
