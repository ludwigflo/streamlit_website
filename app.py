# app.py

import streamlit as st
from core.router import PageRouter
from pages.home import HomePage
from pages.mannschaften import MannschaftenPage
from pages.neuigkeiten import NeuigkeitenPage
from pages.geschichte import GeschichtePage


def main():
    st.set_page_config(
        page_title="TuS Bad Aibling Tischtennis",
        page_icon="🏓",
        layout="wide",
    )

    st.markdown("""
            <style>
                /* Hide Streamlit’s own sidebar */
                [data-testid="stSidebar"] {display:none !important;}
                [data-testid="stSidebarToggle"] {display:none !important;}
                [data-testid="collapsedControl"] {display:none !important;}

                /* 👇 Scrollable content area on the right side */
                .tt-content-scroll {
                    overflow-x: auto;   /* enable horizontal scroll when needed */
                    width: 100%;
                }

                /* 👇 Force inner content to be wider than small windows */
                .tt-content-scroll > div {
                    min-width: 1100px;       /* adjust to your preferred design width */
                    max-width: none !important;
                }
            </style>
        """, unsafe_allow_html=True)

    pages = [
        HomePage(),
        MannschaftenPage(),
        NeuigkeitenPage(),
        GeschichtePage(),
    ]

    router = PageRouter(
        club_name="  TuS Bad Aibling Tischtennis",
        logo_path="assets/logo.png",
        pages=pages,
    )
    router.run()


if __name__ == "__main__":
    main()
