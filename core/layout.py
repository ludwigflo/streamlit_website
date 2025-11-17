import base64
from pathlib import Path
import streamlit as st
from contextlib import contextmanager

def _image_to_base64(path: str) -> str | None:
    try:
        img_bytes = Path(path).read_bytes()
        return base64.b64encode(img_bytes).decode("utf-8")
    except Exception:
        return None


@contextmanager
def centered_content(width_ratio: float = 2.0):
    """
    Use as:
        with centered_content():
            st.header("...")
            st.write("...")

    This centers the content horizontally using three columns.
    """
    left, center, right = st.columns([1, width_ratio, 1])
    with center:
        yield


def render_header(club_name: str, logo_path: str) -> None:
    """Centered logo + title, logo size tied to title font size."""
    logo_b64 = _image_to_base64(logo_path)

    if logo_b64:
        logo_html = (
            f'<img src="data:image/png;base64,{logo_b64}" '
            'style="height:3em;width:auto;margin:0;" alt="Logo" />'
        )
    else:
        logo_html = '<span style="font-size:1.2em;margin:0;">🏓</span>'

    # The font-size on this container controls both logo and title size
    st.markdown(
        f"""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            margin-top:0.8rem;
        ">
            <div style="
                display:flex;
                align-items:center;
                gap:0.4rem;
                font-size:5rem;
            ">
                {logo_html}
                <span>{club_name}</span>
            </div>
        </div>
        <hr style="margin-top:0.6rem;margin-bottom:0.6rem;" />
        """,
        unsafe_allow_html=True,
    )
