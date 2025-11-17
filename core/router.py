# core/router.py
from abc import ABC, abstractmethod
import streamlit as st

from core.layout import render_header


class BasePage(ABC):
    """Abstract base class for all pages."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable page name."""
        ...

    @abstractmethod
    def render(self) -> None:
        """Render the page content."""
        ...


def render_left_nav(page_names: list[str], current_page: str) -> str:
    """
    Left-side hamburger + vertical navbar.
    Returns the selected page name.
    """

    # Session state for open/closed menu
    if "menu_open" not in st.session_state:
        st.session_state["menu_open"] = True

    # Hamburger toggle (font-size now controlled globally in app.py)
    if st.button("☰", use_container_width=True):
        st.session_state["menu_open"] = not st.session_state["menu_open"]

    selected = current_page

    # Menu entries (font-size now controlled globally in app.py)
    if st.session_state["menu_open"]:

        selected = st.radio("Navigation", index=page_names.index(current_page),
                            label_visibility="collapsed", options=page_names)
    return selected


class PageRouter:
    """
    Handles header, left-side navigation and dispatches
    to the correct page based on the current selection.
    """

    def __init__(self, club_name: str, logo_path: str, pages: list[BasePage]):
        self.club_name = club_name
        self.logo_path = logo_path
        self.pages = {p.name: p for p in pages}

        if "current_page" not in st.session_state and pages:
            st.session_state["current_page"] = pages[0].name

    def run(self) -> None:

        # Header at the top (logo + title)
        render_header(self.club_name, self.logo_path)

        page_names = list(self.pages.keys())
        current_page = st.session_state.get("current_page", page_names[0])

        # Three columns: left = menu, middle = divider, right = content
        col_menu, col_content = st.columns([1, 7])

        with col_menu:

            st.markdown('<div class="tt-left-menu">', unsafe_allow_html=True)
            selected = render_left_nav(page_names, current_page)
            st.markdown('</div>', unsafe_allow_html=True)

        # Update current page
        st.session_state["current_page"] = selected

        # RIGHT: page content
        with col_content:
            st.markdown('<div class="tt-content-scroll">', unsafe_allow_html=True)
            self.pages[selected].render()
            st.markdown('</div>', unsafe_allow_html=True)