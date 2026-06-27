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
        </style>
        """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                    background: #a9d0d9 !important
                }
        </style>
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

                div[data-testid="stTextInput"] label,
                div[data-testid="stSelectbox"] label,
                div[data-testid="stTextArea"] label{
                    color:#111111 !important;
                }

                
                /* Cloud uses white text because it is using dark inputs. Override them. */
                div[data-testid="stTextInput"] input{
                    background:#ffffff !important;
                    color:#111111 !important;
                }
                
                div[data-testid="stTextInput"] input[type="password"]{
                    background:#ffffff !important;
                    color:#111111 !important;
                }

                div[data-testid="stSelectbox"] div[data-baseweb="select"]{
                    background:white !important;
                    color:#111111 !important;
                }

                div[data-testid="stSelectbox"] span{
                    color:#111111 !important;
                }

                /* Your dataframe is rendered using Streamlit's theme. */
                .stDataFrame{
                    color:#111111 !important;
                }

                .stDataFrame table{
                    background:white !important;
                }

                .stDataFrame th{
                    background:white !important;
                    color:#111111 !important;
                }

                .stDataFrame td{
                    color:#111111 !important;
                }


                h1,
                h2,
                h3,
                h4,
                h5,
                h6{
                    color:#111111 !important;
                }

                h1 {
                    font-family: "Black Ops One" !important; 
                    font-size: 3.5rem !important;
                    line-height: 1.1 !important;
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