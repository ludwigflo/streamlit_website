# pages/home.py
import streamlit as st
from core.router import BasePage
from core.layout import centered_content


class HomePage(BasePage):
    @property
    def name(self) -> str:
        return "Home"

    def render(self) -> None:
        with centered_content():
            st.header("Willkommen beim Tischtennis Bad Aibling")
            st.write(
                "Hier findest du alle Informationen rund um unseren Verein, "
                "unsere Mannschaften und aktuelle Neuigkeiten."
            )
            st.write(
                "Diese Startseite kannst du später mit Bildern, Terminen "
                "und weiteren Infos erweitern."
            )
