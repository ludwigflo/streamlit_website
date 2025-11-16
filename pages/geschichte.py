import streamlit as st
from core.router import BasePage
from core.layout import centered_content


class GeschichtePage(BasePage):
    @property
    def name(self) -> str:
        return "Geschichte"

    def render(self) -> None:
        with centered_content():
            st.header("Vereinsgeschichte")
            st.write(
                "Auf dieser Seite kannst du die Geschichte des Vereins "
                "Tischtennis Bad Aibling erzählen – Gründung, wichtige Erfolge, "
                "besondere Persönlichkeiten und Meilensteine."
            )

            st.write(
                "Zum Beispiel:\n\n"
                "- Gründungsjahr\n"
                "- Aufstiege in höhere Ligen\n"
                "- Ausrichtung von Turnieren\n"
                "- Besondere Vereinsaktionen"
            )
