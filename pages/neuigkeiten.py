import streamlit as st
from core.router import BasePage
from core.layout import centered_content


class NeuigkeitenPage(BasePage):
    @property
    def name(self) -> str:
        return "Neuigkeiten"

    def render(self) -> None:
            # In the future you might load news from a database or a CSV
        with centered_content():
            st.header("Neuigkeiten")
            st.write(
                "Hier kannst du Berichte über Spiele, Turniere, "
                "Vereinsfeste und andere News veröffentlichen."
            )

            # Beispiel für eine News-Karte
            st.subheader("Beispiel-News: Erfolgreicher Saisonstart")
            st.write(
                "Unsere 1. Herrenmannschaft ist mit einem 9:4-Sieg in die neue Saison gestartet. "
                "Herzlichen Glückwunsch an alle Spieler!"
            )

            st.caption("Später kannst du hier eine Liste von Newsartikeln dynamisch erzeugen.")
