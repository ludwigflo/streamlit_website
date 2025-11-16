# core/router.py
from abc import ABC, abstractmethod
import streamlit as st

from core.layout import render_header, render_navbar


class BasePage(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def render(self) -> None:
        ...


class PageRouter:
    def __init__(self, club_name: str, logo_path: str, pages: list[BasePage]):
        self.club_name = club_name
        self.logo_path = logo_path
        self.pages = {p.name: p for p in pages}

        if "current_page" not in st.session_state:
            st.session_state["current_page"] = pages[0].name

    def run(self) -> None:
        page_names = list(self.pages.keys())
        current_page = st.session_state["current_page"]

        # header (logo + title)
        render_header(self.club_name, self.logo_path)

        # navbar (buttons) – updates session state
        selected = render_navbar(page_names, current_page)
        st.session_state["current_page"] = selected

        # render selected page
        self.pages[selected].render()
