import streamlit as st

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
   

