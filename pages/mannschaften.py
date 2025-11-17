# pages/mannschaften.py
import streamlit as st
from core.router import BasePage
from core.layout import centered_content


class MannschaftenPage(BasePage):
    @property
    def name(self) -> str:
        return "Teams"

    def render(self) -> None:
        with centered_content():
            st.header("Mannschaften")
            st.write(
                "Hier kannst du später die einzelnen Mannschaften vorstellen "
                "(z. B. Herren, Damen, Jugend, Schüler, etc.)."
            )

            # Beispiel-Struktur, die du später dynamisch machen kannst
            st.subheader("Herren I")
            st.write("• Liga: Bezirksliga\n• Mannschaftsführer: Max Mustermann")

            st.subheader("Jugend")
            st.write("• Trainingszeiten: Dienstag & Donnerstag\n• Trainer: N. N.")
