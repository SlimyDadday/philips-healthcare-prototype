import streamlit as st

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Philips MedSentinel AI",
    layout="wide"
)

# ------------------------------------------------
# BACKGROUNDS
# ------------------------------------------------
login_bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}
[data-testid="stHeader"]{background: rgba(0,0,0,0);}
[data-testid="stSidebar"]{background: rgba(0,0,0,0);}
</style>
"""

dashboard_bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image:
linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
url("https://images.unsplash.com/photo-1579684385127-1ef15d508118");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}

h1,h2,h3,h4,h5,h6,p,div,label{
color:white !important;
}

.stButton>button{
background-color:#00b4d8;
color:white;
border-radius:10px;
border:none;
padding:10px 20px;
font-weight:bold;
}
</style>
"""

# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ------------------------------------------------
# LOGIN SCREEN
# ------------------------------------------------
if not st.session_state.logged_in:

    st.markdown(login_bg, unsafe_allow_html=True)

    # 🏥 BRANDING ON LOGIN PAGE
    st.markdown(
        """
        <div style='text-align:center;'>
            <h1 style='color:white;'>🏥 Philips MedSentinel AI</h1>
            <p style='color:white;'>Smart Healthcare Monitoring System</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "Patient A" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong username or password")

# ------------------------------------------------
# MAIN APP
# ------------------------------------------------
else:

    st.markdown(dashboard_bg, unsafe_allow_html=True)

    # 🏥 LOGO + HEADER (MAIN IMPROVEMENT)
    col1, col2 = st.columns([1, 5])

    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/5/5f/Philips_logo_new.svg",
            width=90
        )

    with col2:
        st.title("Philips MedSentinel AI")
        st.subheader("Smart Medical Monitoring & Interoperability System")

    st.markdown("---")

    # ---------------- SIDEBAR ----------------
    st.sidebar.image(
        "https://upload.wikimedia.org/wikipedia/commons/5/5f/Philips_logo_new.svg",
        width=120
    )

    st.sidebar.title("MedSentinel AI Menu")

    if st.sidebar.button("📊 Dashboard"):
        st.session_state.page = "Dashboard"

    if st.sidebar.button("🧠 AI Monitoring"):
        st.session_state.page = "AI"

    if st.sidebar.button("🛡️ Quality Guardian"):
        st.session_state.page = "Quality"

    if st.sidebar.button("🔗 Interoperability"):
        st.session_state.page = "Interop"

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # ------------------------------------------------
    # PAGES
    # ------------------------------------------------
    if st.session_state.page == "Dashboard":

        st.header("Patient Dashboard")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Patients Connected", "1,245")
        with col2:
            st.metric("Active Alerts", "12")
        with col3:
            st.metric("System Accuracy", "98%")

        st.markdown("---")

        st.subheader("Patient Records")

        st.info("""
        Patient Name: Patient A  
        Patient ID: PH-2026-1001  
        Age: 35  
        Blood Group: O+  
        Condition: Stable  
        """)

        st.success("Latest lab results uploaded successfully.")
        st.warning("AI Alert: Slight increase in blood pressure.")

    elif st.session_state.page == "AI":

        st.header("AI Monitoring System")

        st.warning("AI detected slight blood pressure increase.")
        st.info("Recommended monitoring: 24 hours.")
        st.success("No emergency condition detected.")

    elif st.session_state.page == "Quality":

        st.header("AI Quality Guardian")

        st.success("All medical devices functioning normally.")
        st.info("No product recall risk detected.")

    elif st.session_state.page == "Interop":

        st.header("Interoperability System")

        st.success("Electronic Health Records")
        st.success("MRI Scanner")
        st.success("Laboratory System")
        st.success("Insurance Database")
        st.success("Patient Monitoring Devices")