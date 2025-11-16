# core/layout.py
import base64
from pathlib import Path
from contextlib import contextmanager
import streamlit as st


@contextmanager
def centered_content(width_ratio: float = 2.0):
    """Shared centering for header, navbar and page content."""
    left, center, right = st.columns([1, width_ratio, 1])
    with center:
        yield


def _image_to_base64(path: str) -> str | None:
    try:
        img_bytes = Path(path).read_bytes()
        return base64.b64encode(img_bytes).decode("utf-8")
    except Exception:
        return None


def render_header(club_name: str, logo_path: str) -> None:
    """Logo + title as one centered block."""
    logo_b64 = _image_to_base64(logo_path)
    if logo_b64:
        logo_html = (
            f'<img src="data:image/png;base64,{logo_b64}" '
            'style="height:250px;margin:0;" />'
        )
    else:
        logo_html = '<span style="font-size:3rem;margin:0;">🏓</span>'

    with centered_content():
        st.markdown(
            f"""
            <div style="
                display:flex;
                justify-content:center;
                align-items:center;
                gap:0.5rem;
                margin-top:0.8rem;
            ">
                {logo_html}
                <h1 style="margin:0;font-size:4rem;">
                    {club_name}
                </h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)


def render_navbar(page_names: list[str], current_page: str) -> str:
    """Centered navbar row using buttons in columns."""

    # Inject CSS for button styling
    st.markdown("""
    <style>
    .nav-btn > button {
        background-color: #f5f5f5;
        border-radius: 8px;
        border: 1px solid #ddd;
        font-size: 1.1rem;
        padding: 0.4rem 0.6rem;
    }
    .nav-btn-active > button {
        background-color: #333 !important;
        color: white !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Render centered navbar
    from core.layout import centered_content
    with centered_content():
        cols = st.columns(len(page_names))
        new_page = current_page

        for i, name in enumerate(page_names):
            is_active = name == current_page
            css_class = "nav-btn-active" if is_active else "nav-btn"

            with cols[i]:
                # Wrap each button in a div so we can style it
                st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
                if st.button(name, width="content", use_container_width=True):
                    new_page = name
                st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

    return new_page

