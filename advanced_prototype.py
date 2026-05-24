import streamlit as st

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Philips Healthcare",
    layout="wide"
)

# ------------------------------------------------
# LOGIN SESSION
# ------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ------------------------------------------------
# LOGIN PAGE
# ------------------------------------------------

if not st.session_state.logged_in:

    st.markdown(
        """
        <h1 style='text-align:center;color:#005EB8;'>
        PHILIPS HEALTHCARE
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Patient Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "Patient A" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Wrong username or password")

# ------------------------------------------------
# MAIN DASHBOARD
# ------------------------------------------------

else:

    # ---------------- TOP BAR ---------------- #

    col1, col2 = st.columns([8,2])

    with col1:
        st.markdown(
            "<h1 style='color:#005EB8;'>PHILIPS</h1>",
            unsafe_allow_html=True
        )

    with col2:
        st.write("👤 Patient A")

    st.divider()

    # ---------------- BUTTON SECTION ---------------- #

    left, center, right = st.columns([2,5,2])

    # LEFT SIDE
    with left:

        st.markdown("## Menu")

        if st.button("🧠 AI Monitoring"):
            st.session_state.page = "AI"

        if st.button("🛡️ Quality Guardian"):
            st.session_state.page = "Quality"

    # CENTER
    with center:

        st.markdown("## Patient Records")

        st.container(border=True)

        st.subheader("Patient A")

        st.write("Patient ID: PH-2026-1001")
        st.write("Age: 35")
        st.write("Blood Group: O+")
        st.write("Condition: Stable")

        st.divider()

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Heart Rate", "78 BPM")

        with c2:
            st.metric("Blood Pressure", "120/80")

        with c3:
            st.metric("Oxygen", "98%")

        with c4:
            st.metric("Temperature", "36.6°C")

        st.divider()

        st.subheader("Recent Notes")

        st.info(
            "Regular checkup completed successfully."
        )

    # RIGHT SIDE
    with right:

        st.markdown("## System")

        if st.button("🔗 Interoperability"):
            st.session_state.page = "Interop"

    st.divider()

    # ------------------------------------------------
    # DYNAMIC PAGE CONTENT
    # ------------------------------------------------

    if st.session_state.page == "AI":

        st.header("🧠 AI Monitoring")

        st.warning(
            "AI detected slight blood pressure increase."
        )

        st.info(
            "Monitoring recommended for 24 hours."
        )

        st.success(
            "No critical emergency detected."
        )

    elif st.session_state.page == "Quality":

        st.header("🛡️ Quality Guardian")

        st.write("Device Safety Status: SAFE")
        st.write("Complaint Risk Score: LOW")
        st.write("Maintenance Status: COMPLETED")

        st.success(
            "All medical devices functioning normally."
        )

    elif st.session_state.page == "Interop":

        st.header("🔗 Interoperability System")

        st.write("Connected Systems:")

        st.write("✅ Electronic Health Records")
        st.write("✅ MRI Scanner")
        st.write("✅ Laboratory System")
        st.write("✅ Insurance Database")

        st.success(
            "All hospital systems connected successfully."
        )

    else:

        st.header("📊 Dashboard")

        a1, a2 = st.columns(2)

        with a1:
            st.error(
                "AI Alert: Slight increase in blood pressure."
            )

        with a2:
            st.success(
                "Latest lab results uploaded successfully."
            )

    st.divider()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()