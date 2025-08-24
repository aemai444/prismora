import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer

# Dialog function using the decorator
@st.dialog("Message Window", dismissible=True, width="small")
def show_message_dialog(message: str):
    st.write(message)
    if st.button("Close"):
        ss.show_dialog = False
        st.rerun()

def main_page():
    st.title("prismora")
    st.subheader("Channeling Data, Creating Value")
    st.markdown("At Prismora, every interaction counts—turning the information users share into actionable insights that drive innovation and growth. By transforming user activity into marketable value, we empower businesses while creating a platform where engagement is truly rewarded.")
    # Initialize session state variables
    if "pdf_ref" not in ss:
        ss.pdf_ref = None
    if "show_dialog" not in ss:
        ss.show_dialog = False
    if "popup_message" not in ss:
        ss.popup_message = "Error 404: Data could not be found"

    # File uploader
    st.file_uploader("Upload PDF file", type="pdf", key="pdf")
    if ss.pdf:
        ss.pdf_ref = ss.pdf


    # Button to show the popup
    if st.button("database"):
        ss.show_dialog = True

    # Display dialog if triggered
    if ss.show_dialog:
        show_message_dialog(ss.popup_message)

    # Display PDF if uploaded
    if ss.pdf_ref:
        binary_data = ss.pdf_ref.getvalue()
        pdf_viewer(input=binary_data, width=700)
