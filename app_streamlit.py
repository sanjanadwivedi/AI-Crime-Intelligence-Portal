# app_streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
import json
import warnings

warnings.filterwarnings("ignore")

# ---------------------------------------------------
# SIMPLE LOGIN SYSTEM
# ---------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.set_page_config(
        page_title="CrimeVision AI",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
    <style>

    #MainMenu{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    .stDeployButton{
        display:none;
    }

    .stApp{
        background:#09090B;
    }

    .login-title{
        font-size:56px;
        font-weight:800;
        color:white;
        text-align:center;
        margin-bottom:10px;
    }

    .login-subtitle{
        color:#A1A1AA;
        text-align:center;
        font-size:18px;
        margin-bottom:35px;
    }

    .stTextInput input{

        background:#111827;

        border:1px solid #2D3748;

        border-radius:14px;

        color:white;

        padding:14px;

    }

    .stButton>button{

        width:100%;

        background:#7C3AED;

        color:white;

        border:none;

        border-radius:999px;

        padding:14px;

        font-size:16px;

        font-weight:600;

    }

    .stButton>button:hover{

        background:#8B5CF6;

    }

    </style>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.2, 1])

    with center:

        st.markdown(
            "<h1 class='login-title'>CrimeVision AI</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p class='login-subtitle'>Welcome back. Sign in to continue.</p>",
            unsafe_allow_html=True
        )

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        if st.button("Launch Platform"):

            if username == "admin" and password == "admin123":

                st.session_state.logged_in = True

                st.rerun()

            else:

                st.error("Invalid Username or Password")
            st.markdown("""
    <div style="
        margin-top:25px;
        padding:18px;
        border-radius:16px;
        background:rgba(124,58,237,0.08);
        border:1px solid rgba(124,58,237,0.25);
    ">
        <h4 style="
            margin:0 0 12px 0;
            color:#C084FC;
            font-size:18px;
        ">
            💡 Demo Access
        </h4>

        <p style="margin:4px 0;color:#E5E7EB;">
            <b>Username:</b> admin
        </p>

        <p style="margin:4px 0;color:#E5E7EB;">
            <b>Password:</b> admin123
        </p>

        <hr style="border-color:#27272A; margin:14px 0;">

        <p style="
            margin:0;
            color:#A1A1AA;
            font-size:14px;
            line-height:1.6;
        ">
            This is a demonstration version of <b>CrimeVision AI</b>. Use the above credentials to explore Dashboard, AI Prediction, Crime Analytics, Forecasting and Heatmap visualizations.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.stop()
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Crime Intelligence Portal",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
st.markdown("""
<style>
/* ------------------------------------------------ */
/* MAIN APP */
/* ------------------------------------------------ */

.stApp{

    background:#0B1120 !important;
    color:#FFFFFF !important;
}

/* ------------------------------------------------ */
/* MAIN CONTAINER */
/* ------------------------------------------------ */

.main .block-container{

    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* ------------------------------------------------ */
/* SIDEBAR */
/* ------------------------------------------------ */

section[data-testid="stSidebar"]{

    background:#111827 !important;
    border-right:1px solid #1F2937;
}

/* Remove default top padding */

section[data-testid="stSidebar"] > div{

    padding-top:15px;
}

/* ------------------------------------------------ */
/* SIDEBAR TOGGLE (>>) */
/* ------------------------------------------------ */

button[kind="header"]{

    color:white !important;
    background:transparent !important;
    border:none !important;
}

button[kind="header"]:hover{

    background:#7C3AED !important;
    border-radius:10px;
}

button[kind="header"] svg{

    fill:white !important;
    color:white !important;
    width:22px;
    height:22px;
}

/* ------------------------------------------------ */
/* GLOBAL TEXT */
/* ------------------------------------------------ */

html,
body,
p,
span,
label,
div{

    color:#F8FAFC !important;
}

/* ------------------------------------------------ */
/* HEADINGS */
/* ------------------------------------------------ */

h1{

    color:white !important;
    font-size:3rem !important;
    font-weight:800 !important;
}

h2{

    color:white !important;
    font-size:2rem !important;
    font-weight:700 !important;
}

h3,h4,h5,h6{

    color:white !important;
}

/* ------------------------------------------------ */
/* KPI CARDS */
/* ------------------------------------------------ */

.kpi-card{

    background:linear-gradient(
        135deg,
        #1E293B,
        #111827
    );

    border-left:5px solid #8B5CF6;

    border-radius:18px;

    padding:24px;

    text-align:center;

    box-shadow:0 10px 30px rgba(0,0,0,.35);

    transition:.25s;
}

.kpi-card:hover{

    transform:translateY(-4px);

    box-shadow:0 15px 40px rgba(139,92,246,.25);
}

.kpi-title{

    color:#D8B4FE !important;

    font-size:17px;

    margin-bottom:10px;
}

.kpi-value{

    color:white !important;

    font-size:36px;

    font-weight:800;
}

/* ------------------------------------------------ */
/* BUTTONS */
/* ------------------------------------------------ */

.stButton>button{

    background:linear-gradient(
        135deg,
        #7C3AED,
        #A855F7
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:12px !important;

    padding:.75rem 1.7rem !important;

    font-weight:700 !important;

    transition:.25s;

    box-shadow:0 8px 18px rgba(124,58,237,.35);
}

.stButton>button:hover{

    transform:translateY(-2px);

    background:linear-gradient(
        135deg,
        #8B5CF6,
        #C084FC
    ) !important;

    box-shadow:0 12px 28px rgba(124,58,237,.45);
}

/* ------------------------------------------------ */
/* DOWNLOAD BUTTON */
/* ------------------------------------------------ */

.stDownloadButton>button{

    background:linear-gradient(
        135deg,
        #7C3AED,
        #A855F7
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:12px !important;

    padding:.75rem 1.7rem !important;

    font-weight:700 !important;

    box-shadow:0 8px 18px rgba(124,58,237,.35);
}

.stDownloadButton>button:hover{

    transform:translateY(-2px);

    background:linear-gradient(
        135deg,
        #8B5CF6,
        #C084FC
    ) !important;
}
/* ------------------------------------------------ */
/* SIDEBAR NAVIGATION */
/* ------------------------------------------------ */

div[role="radiogroup"] > label{

    background:#1F2937 !important;

    border:1px solid #374151 !important;

    border-radius:14px !important;

    padding:14px 18px !important;

    margin-bottom:12px !important;

    color:#F8FAFC !important;

    font-size:17px !important;

    font-weight:600 !important;

    transition:all .25s ease;
}

/* Hover */

div[role="radiogroup"] > label:hover{

    background:#2D3748 !important;

    border-color:#8B5CF6 !important;

    transform:translateX(6px);
}

/* Selected */

div[role="radiogroup"] > label[data-checked="true"]{

    background:linear-gradient(
        135deg,
        #7C3AED,
        #A855F7
    ) !important;

    color:white !important;

    border-color:#A855F7 !important;

    box-shadow:0 10px 25px rgba(124,58,237,.35);
}

/* Radio circle */

div[role="radiogroup"] svg{

    fill:white !important;
}

/* ------------------------------------------------ */
/* SELECTBOX */
/* ------------------------------------------------ */

div[data-baseweb="select"]{

    background:#1F2937 !important;

    border:2px solid #8B5CF6 !important;

    border-radius:12px !important;
}

div[data-baseweb="select"]>div{

    background:#1F2937 !important;

    color:white !important;
}

div[data-baseweb="select"] span{

    color:white !important;

    font-size:17px !important;
}

/* Dropdown */

div[role="listbox"]{

    background:#111827 !important;

    border-radius:12px !important;
}

div[role="option"]{

    background:#111827 !important;

    color:white !important;

    padding:12px !important;
}

div[role="option"]:hover{

    background:#374151 !important;
}

/* ------------------------------------------------ */
/* SLIDER */
/* ------------------------------------------------ */

.stSlider label{

    color:white !important;

    font-weight:600;
}

.stSlider span{

    color:white !important;
}

.stSlider [data-baseweb="slider"]{

    padding-top:10px;
}

.stSlider [role="slider"]{

    background:white !important;

    border:4px solid #8B5CF6 !important;

    width:18px !important;

    height:18px !important;
}

/* ------------------------------------------------ */
/* METRIC */
/* ------------------------------------------------ */

[data-testid="metric-container"]{

    background:#1F2937 !important;

    border-radius:18px !important;

    border-left:5px solid #8B5CF6;

    padding:20px !important;

    box-shadow:0 8px 20px rgba(0,0,0,.35);
}

/* ------------------------------------------------ */
/* ALERTS */
/* ------------------------------------------------ */

.stAlert{

    border-radius:14px !important;
}

/* ------------------------------------------------ */
/* FILE UPLOADER */
/* ------------------------------------------------ */

[data-testid="stFileUploader"]{

    background:#1F2937 !important;

    border:2px dashed #8B5CF6 !important;

    border-radius:16px !important;

    padding:18px !important;
}

[data-testid="stFileUploader"] *{

    color:white !important;
}

[data-testid="stFileUploader"] button{

    background:linear-gradient(
        135deg,
        #7C3AED,
        #A855F7
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:10px !important;
}

section[data-testid="stFileUploaderDropzone"]{

    background:#1F2937 !important;

    border:2px dashed #8B5CF6 !important;
}

/* ------------------------------------------------ */
/* LINKS */
/* ------------------------------------------------ */

a{

    color:#C084FC !important;
}

/* ------------------------------------------------ */
/* SCROLLBAR */
/* ------------------------------------------------ */

::-webkit-scrollbar{

    width:10px;
}

::-webkit-scrollbar-track{

    background:#111827;
}

::-webkit-scrollbar-thumb{

    background:#8B5CF6;

    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)
# ---------------------------------------------------
# LOGIN
if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df_nat = pd.read_excel("data/2000-22.xlsx")

df_nat.columns = (
    df_nat.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

state_df = pd.read_excel(
    "data/Total IPC Crimes by State_UT(2011-2022).xlsx"
)

state_df.columns = (
    state_df.columns
    .astype(str)
    .str.strip()
)

# ---------------------------------------------------
# LOAD GEOJSON
# ---------------------------------------------------

with open("india_states.geojson", "r") as f:
    india_geo = json.load(f)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = joblib.load("models/crime_model.pkl")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
#  AI Crime Intelligence Portal
""")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("## 🛡️ AI Crime Portal")
    st.caption("Crime Intelligence System")

    st.divider()

    module = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🤖 AI Prediction",
            "📊 Crime Analytics",
            "📈 Forecasting",
            "🗺️ Heatmap",
            "⚙️ Admin Panel"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.rerun()

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

if module == "🏠 Dashboard":

    latest_year = df_nat["year"].max()

    latest = df_nat[
        df_nat["year"] == latest_year
    ]

    total_crimes = int(
        latest[
            "total_cognizable_crimes_under_ipc"
        ].iloc[0]
    )

    population = int(
        latest["population"].iloc[0]
    )

    crime_rate = float(
        latest["total_crimes_per_million"].iloc[0]
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">
                Total Crimes
            </div>
            <div class="kpi-value">
                {total_crimes:,}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">
                Population
            </div>
            <div class="kpi-value">
                {population:,}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">
                Crime Rate
            </div>
            <div class="kpi-value">
                {crime_rate:.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    fig = px.line(
        df_nat,
        x="year",
        y="total_cognizable_crimes_under_ipc",
        markers=True,
        title="National Crime Trend"
    )

    fig.update_layout(
        height=500,
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.markdown("---")

    top_crimes = {
        "Murder": int(df_nat["murder"].sum()),
        "Rape": int(df_nat["rape"].sum()),
        "Robbery": int(df_nat["robbery"].sum()),
        "Theft": int(df_nat["theft"].sum()),
        "Riots": int(df_nat["riots"].sum())
    }

    pie_df = pd.DataFrame({
        "Crime": list(top_crimes.keys()),
        "Count": list(top_crimes.values())
    })

    pie = px.pie(
        pie_df,
        names="Crime",
        values="Count",
        title="Crime Distribution"
    )

    pie.update_layout(
        paper_bgcolor="#0B1120",
        font_color="white",
        height=500
    )

    st.plotly_chart(
        pie,
        width="stretch"
    )

# ---------------------------------------------------
# AI PREDICTION
# ---------------------------------------------------

elif module == "🤖 AI Prediction":

    st.markdown("""
         <h2 style='
         color:white;
         font-size:30px;
         font-weight:700;
         margin-bottom:20px;'>
         State Crime Prediction</h2>""", unsafe_allow_html=True)

    states = sorted(
        state_df["States_UT"].dropna().unique()
    )

    state = st.selectbox(
        "Select State",
        states
    )

    year = st.slider(
        "Select Future Year",
        2023,
        2035,
        2026
    )

    # GET VALID YEAR COLUMNS
    year_cols = [
        c for c in state_df.columns
        if str(c).isdigit()
    ]

    latest_year = year_cols[-1]

    if st.button("Predict Crimes"):

        row = state_df[
            state_df["States_UT"] == state
        ]

        base_crime = int(
            row[latest_year].values[0]
        )

        growth_rate = 0.03

        years_diff = year - int(latest_year)

        predicted = int(
            base_crime *
            ((1 + growth_rate) ** years_diff)
        )

        if predicted < 100000:
            risk = "Low"
            color = "green"

        elif predicted < 500000:
            risk = "Medium"
            color = "orange"

        else:
            risk = "High"
            color = "red"

        st.success(
            f"""
            Predicted Crimes in {state}
            ({year}) : {predicted:,}
            """
        )

        st.markdown(
            f"""
            <h2 style='color:{color};'>
            Risk Level : {risk}
            </h2>
            """,
            unsafe_allow_html=True
        )

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=predicted,
                title={
                    'text': f"{state} Crime Forecast"
                },
                gauge={
                    'axis': {
                        'range': [0, predicted * 1.5]
                    },
                    'bar': {
                        'color': color
                    },
                }
            )
        )

        gauge.update_layout(
            height=500,
            paper_bgcolor="#0B1120",
            font_color="white"
        )

        st.plotly_chart(
            gauge,
            width="stretch"
        )

        st.warning(
            f"""
            {state} is predicted to have
            {risk.lower()} crime risk in {year}.
            """
        )

# ---------------------------------------------------
# CRIME ANALYTICS
# ---------------------------------------------------

elif module == "📊 Crime Analytics":

    st.markdown("""
<h2 style='
color:white;
font-size:30px;
font-weight:700;
margin-bottom:20px;
'>
Crime Analytics
</h2>
""", unsafe_allow_html=True)

    crimes = [
        "murder",
        "rape",
        "robbery",
        "theft",
        "riots",
        "hurt",
        "cheating"
    ]

    selected = st.selectbox(
        "Select Crime Type",
        crimes
    )

    fig = px.bar(
        df_nat,
        x="year",
        y=selected,
        color=selected,
        title=f"{selected.title()} Trend"
    )

    fig.update_layout(
        height=600,
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ---------------------------------------------------
# FORECASTING
# ---------------------------------------------------

elif module == "📈 Forecasting":

    st.markdown("""
<h2 style='
color:white;
font-size:30px;
font-weight:700;
margin-bottom:20px;
'>
Crime Forecasting
</h2>
""", unsafe_allow_html=True)

    crime = st.selectbox(
        "Select Crime Type",
        [
            "murder",
            "rape",
            "robbery",
            "theft"
        ]
    )

    years_future = st.slider(
        "Forecast Years",
        1,
        10,
        5
    )

    historical = df_nat[
        ["year", crime]
    ]

    last_year = historical["year"].max()

    growth_rate = 0.03

    future_years = []
    future_values = []

    last_value = historical[crime].iloc[-1]

    for i in range(1, years_future + 1):

        fy = last_year + i

        fv = last_value * (
            (1 + growth_rate) ** i
        )

        future_years.append(fy)

        future_values.append(fv)

    forecast_df = pd.DataFrame({
        "year": future_years,
        crime: future_values
    })

    historical["Type"] = "Historical"

    forecast_df["Type"] = "Forecast"

    combined = pd.concat([
        historical,
        forecast_df
    ])

    fig = px.line(
        combined,
        x="year",
        y=crime,
        color="Type",
        markers=True,
        title=f"{crime.title()} Forecast"
    )

    fig.update_layout(
        height=600,
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ---------------------------------------------------
# ---------------------------------------------------
# HEATMAP
# ---------------------------------------------------

elif module == "🗺️ Heatmap":
    
    st.markdown("""
<h2 style='
color:white;
font-size:30px;
font-weight:700;
margin-bottom:20px;
'>
India Crime Hotspot Map
</h2>
""", unsafe_allow_html=True)

    year_cols = [
        c for c in state_df.columns
        if str(c).isdigit()
    ]

    selected_year = st.selectbox(
        "Select Year",
        year_cols
    )

    map_df = state_df[
        ["States_UT", selected_year]
    ].copy()

    map_df.columns = [
        "State",
        "Crime"
    ]

    map_df.dropna(inplace=True)

    # MATCH GEOJSON NAMES
    state_mapping = {

        "A & N Islands":
            "Andaman and Nicobar",

        "Andhra Pradesh":
            "Andhra Pradesh",

        "Arunachal Pradesh":
            "Arunachal Pradesh",

        "Assam":
            "Assam",

        "Bihar":
            "Bihar",

        "Chhattisgarh":
            "Chhattisgarh",

        "Delhi UT":
            "Delhi",

        "Goa":
            "Goa",

        "Gujarat":
            "Gujarat",

        "Haryana":
            "Haryana",

        "Himachal Pradesh":
            "Himachal Pradesh",

        "Jammu & Kashmir":
            "Jammu and Kashmir",

        "Jharkhand":
            "Jharkhand",

        "Karnataka":
            "Karnataka",

        "Kerala":
            "Kerala",

        "Madhya Pradesh":
            "Madhya Pradesh",

        "Maharashtra":
            "Maharashtra",

        "Manipur":
            "Manipur",

        "Meghalaya":
            "Meghalaya",

        "Mizoram":
            "Mizoram",

        "Nagaland":
            "Nagaland",

        "Odisha":
            "Odisha",

        "Punjab":
            "Punjab",

        "Rajasthan":
            "Rajasthan",

        "Sikkim":
            "Sikkim",

        "Tamil Nadu":
            "Tamil Nadu",

        "Telangana":
            "Telangana",

        "Tripura":
            "Tripura",

        "Uttar Pradesh":
            "Uttar Pradesh",

        "Uttarakhand":
            "Uttarakhand",

        "West Bengal":
            "West Bengal"
    }

    map_df["State"] = map_df["State"].replace(
        state_mapping
    )

    fig = px.choropleth(
        map_df,
        geojson=india_geo,
        featureidkey="properties.NAME_1",
        locations="State",
        color="Crime",
        color_continuous_scale="Reds",
        title=f"India Crime Heatmap ({selected_year})"
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        height=700,
        margin={
            "r":0,
            "t":50,
            "l":0,
            "b":0
        },
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ---------------------------------------------------
# ADMIN PANEL
# ---------------------------------------------------

elif module == "⚙️ Admin Panel":

     st.markdown("""
     <h2 style='
     color:white;
     font-size:30px;
     font-weight:700;
     margin-bottom:20px;'>AI Data Ingestion System</h2>""", unsafe_allow_html=True)


     st.markdown("""
    Upload new NCRB crime datasets for:
    - dashboard updates
    - analytics refresh
    - AI model retraining
    """)

     st.markdown("---")

     uploaded_file = st.file_uploader(
        "Upload Crime Dataset",
        type=["csv", "xlsx"]
    )

     if uploaded_file is not None:

        # ---------------------------------------------------
        # FILE INFO
        # ---------------------------------------------------

        st.markdown("## 📄 File Information")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.info(f"Filename: {uploaded_file.name}")

        with c2:
            st.info(f"Type: {uploaded_file.type}")

        with c3:
            st.info(
                f"Size: {round(uploaded_file.size/1024,2)} KB"
            )

        # ---------------------------------------------------
        # SAVE FILE
        # ---------------------------------------------------

        save_path = f"uploads/{uploaded_file.name}"

        with open(save_path, "wb") as f:

            f.write(uploaded_file.getbuffer())

        st.success(
            "Dataset Uploaded Successfully"
        )

        # ---------------------------------------------------
        # READ DATASET
        # ---------------------------------------------------

        if uploaded_file.name.endswith(".csv"):

            new_df = pd.read_csv(save_path)

        else:

            new_df = pd.read_excel(save_path)

        # ---------------------------------------------------
        # CLEAN COLUMNS
        # ---------------------------------------------------

        new_df.columns = (
            new_df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        # ---------------------------------------------------
        # REMOVE DUPLICATES
        # ---------------------------------------------------

        before_rows = len(new_df)

        new_df.drop_duplicates(inplace=True)

        after_rows = len(new_df)

        removed = before_rows - after_rows

        # ---------------------------------------------------
        # TABS
        # ---------------------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs([
            "Dataset Preview",
            "Statistics",
            "Missing Values",
            "Visualization"
        ])

        # ---------------------------------------------------
        # PREVIEW
        # ---------------------------------------------------

        with tab1:

            st.markdown("## Dataset Preview")

            st.dataframe(
                new_df.head(20),
                width="stretch"
            )

            st.success(
                f"Removed {removed} duplicate rows"
            )

        # ---------------------------------------------------
        # STATISTICS
        # ---------------------------------------------------

        with tab2:

            st.markdown("## Dataset Statistics")

            st.write(new_df.describe())

            st.markdown("## Dataset Shape")

            st.write(
                f"Rows: {new_df.shape[0]}"
            )

            st.write(
                f"Columns: {new_df.shape[1]}"
            )

        # ---------------------------------------------------
        # MISSING VALUES
        # ---------------------------------------------------

        with tab3:

            st.markdown("## Missing Values")

            missing = new_df.isnull().sum()

            st.dataframe(
                missing.reset_index(),
                width="stretch"
            )

        # ---------------------------------------------------
        # VISUALIZATION
        # ---------------------------------------------------

        with tab4:

            numeric_cols = new_df.select_dtypes(
                include=np.number
            ).columns

            if len(numeric_cols) > 0:

                selected_col = st.selectbox(
                    "Select Numeric Column",
                    numeric_cols
                )

                fig = px.histogram(
                    new_df,
                    x=selected_col,
                    title=f"{selected_col} Distribution"
                )

                fig.update_layout(
                    paper_bgcolor="#0B1120",
                    plot_bgcolor="#0B1120",
                    font_color="white"
                )

                st.plotly_chart(
                    fig,
                    width="stretch"
                )

        # ---------------------------------------------------
        # MERGE DATASET
        # ---------------------------------------------------

        st.markdown("---")

        if st.button("Merge With Existing Dataset"):

            old_df = pd.read_excel(
                "data/2000-22.xlsx"
            )

            old_df.columns = (
                old_df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
            )

            combined = pd.concat(
                [old_df, new_df],
                ignore_index=True
            )

            combined.drop_duplicates(
                inplace=True
            )

            combined.to_excel(
                "data/updated_crime_data.xlsx",
                index=False
            )

            st.success(
                "Dataset Merged Successfully"
            )

            st.write(combined.tail())

        # ---------------------------------------------------
        # RETRAIN MODEL
        # ---------------------------------------------------

        st.markdown("---")

        if st.button("Retrain AI Model"):

            import os

            os.system(
                "python retrain_model.py"
            )

            st.success(
                "AI Model Retrained Successfully"
            )

        # ---------------------------------------------------
        # DOWNLOAD
        # ---------------------------------------------------

        st.markdown("---")

        csv = new_df.to_csv(index=False)

        st.download_button(
            "⬇ Download Uploaded Dataset",
            csv,
            "uploaded_dataset.csv",
            "text/csv"
        )
# ---------------------------------------------------
# DOWNLOAD DATASET
# ---------------------------------------------------

st.markdown("---")

csv = df_nat.to_csv(index=False)

st.download_button(
    "⬇ Download Dataset",
    csv,
    "crime_data.csv",
    "text/csv"
)
