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

            st.markdown("""
            <style>
            .fit-header-to-width {
                font-size: clamp(32px, 2vw, 48px);
                font-weight: bold;
                text-align: center;
                width: 100%;
                margin: 0 auto;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown("""
            <style>
            .fit-text-to-width {
                font-size: clamp(18px, 1.0vw, 42px);   /* size based on viewport width */
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown('<div class="fit-header-to-width">Willkommen beim Tischtennis Bad Aibling</div>',
                        unsafe_allow_html=True)

            text = "Hier findest du alle Informationen rund um unseren Verein, "
            text += "unsere Mannschaften und aktuelle Neuigkeiten."

            st.markdown('<div class="fit-text-to-width">{}</div>'.format(text),
                        unsafe_allow_html=True)
            st.image("assets/übersicht.jpg", "Verein", clamp=False,
                     channels="RGB", output_format="auto", width="stretch")


            _render_training_tables()
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            # _render_team_section()
            render_team_table()


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



def render_team_table():

    st.header("Team")

    st.markdown("""
    <style>
    /* If you only want to affect this specific table, use the class .team-table */
    table.team-table {
        border-collapse: collapse;
        width: 100%;
        border: none !important;
    }

    /* Remove any row borders Streamlit adds */
    table.team-table tr {
        border: none !important;
    }

    /* Remove cell borders and any outlines/shadows */
    table.team-table th,
    table.team-table td {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        padding: 0.3rem 2rem 0.3rem 0;
        vertical-align: top;
    }

    .team-title {
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    # 2) The table: note the class="team-table"
    st.markdown("""
    <table class="team-table">
      <!-- Row 1: Titles -->
      <tr>
        <td class="team-title">Spartenleiter</td>
        <td class="team-title">Vizespartenleiter &amp; Jugendwart</td>
        <td class="team-title">Jugendtrainer</td>
      </tr>

      <!-- Row 2: Names -->
      <tr>
        <td>Alexander Zilken</td>
        <td>Florian Ludwig</td>
        <td>Richard Remmelberger</td>
      </tr>

      <!-- Row 3: Emails -->
      <tr>
        <td><a href="mailto:spartenleiter@tus-bad-aibling.de">spartenleiter@tus-bad-aibling.de</a></td>
        <td><a href="mailto:jugendwart@tus-bad-aibling.de">jugendwart@tus-bad-aibling.de</a></td>
        <td><a href="mailto:jugendtrainer@tus-bad-aibling.de">jugendtrainer@tus-bad-aibling.de</a></td>
      </tr>
    </table>
    """, unsafe_allow_html=True)