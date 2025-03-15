import streamlit as st
from internshala_bot import apply_for_multiple_internships
from database import save_credentials, load_credentials

# Set up the app title
st.title("🚀 InstaFill - Auto Apply for Internships")

# Credential Management
st.header("🔑 Credentials")
email = st.text_input("Email", type="email")
password = st.text_input("Password", type="password")
if st.button("Save Credentials"):
    save_credentials(email, password)
    st.success("Credentials saved successfully!")

# Application Preferences
st.header("📁 Application Preferences")
max_apps = st.number_input("Maximum Applications", min_value=1, value=5)
work_from_home = st.checkbox("Apply for Work From Home Internships")
category = st.selectbox("Select Category", ["All", "Engineering", "Marketing", "Data Science", "Design"])
resume_path = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
cover_letter_path = st.file_uploader("Upload Cover Letter (PDF)", type=["pdf"])

# Progress Tracker
progress_bar = st.progress(0)

# Start Application Button
if st.button("Start Applying"):
    if email and password and resume_path and cover_letter_path:
        st.info("Application process started. Please wait...")
        try:
            apply_for_multiple_internships(
                max_apps=max_apps,
                work_from_home=work_from_home,
                category=category,
                resume_path=resume_path.name,
                cover_letter_path=cover_letter_path.name,
                progress_bar=progress_bar
            )
            st.success("All applications completed successfully!")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please fill all the details before starting.")

st.markdown("### 🌟 Show Some Love!")
st.write("If you like this project, give it a ⭐ on [GitHub](https://github.com/username/InstaFill)!")

