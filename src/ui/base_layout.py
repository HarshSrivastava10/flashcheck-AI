import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
                .stApp{
                    background:  #003366 !important
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #E0E3FF !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                }
        </styles>
        """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                    background: #a9d0d9 !important
                }
        </styles>
        """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
                
                @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

                @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Outfit:wght@100..900&display=swap');
                /* Hide Top Bar of streamlit */

                #MainMenu, footer, header {
                    visibility: hidden;
                }

                .block-container {
                    padding-top:2rem !important;
                }

                h1 {
                    font-family: "Black Ops One" !important; 
                    font-size: 3.5 rem !important;
                    line-height: 1.1 !importatnt;
                    margin-bottom: 0rem !important;
                }

                h2 {
                    font-family: "Black Ops One" !important; 
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                }

                h3, h4, p {
                    font-family: "Outfit", sans-serif !important;
                }


                /* Base button styles applied to ALL buttons */
                button {
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                
                /* Default background color (Primary) */
                background-color: #5865F2 !important;
                }

                /* Secondary variant overrides only the background neon -- #FF5E62  pink --#FF416C */
                button[kind="secondary"] {
                background-color: #FF416C !important;
                }

                /* Tertiary variant overrides only the background */
                button[kind="tertiary"] {
                background-color: black !important;
                }

                button:hover{
                    transform: scale(1.05)
                }
        </style>

        """,
        unsafe_allow_html=True)