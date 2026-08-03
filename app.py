import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Data Portfolio | Professional Showcase",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555555;
    }
    .metric-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/color/96/source-code.png", width=80)
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to:", ["Home & Overview", "Projects Explorer", "Skills & Analytics", "Contact"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Connect with Me")
st.sidebar.markdown("[GitHub Profile](https://github.com/olumobigjoe)")
st.sidebar.markdown("[LinkedIn Profile](https://linkedin.com)")

# --- DATA: PROJECTS ---
projects_data = [
    {
        "Title": "Autonomous AI Agent for Student Performance Diagnostics",
        "Category": "Machine Learning & EdTech",
        "Tech": "Python, Streamlit, Pandas, LLMs",
        "Description": "An automated framework designed for higher education diagnostics to evaluate and analyze student result processing efficiently.",
        "Link": "https://github.com/olumobigjoe"
    },
    {
        "Title": "Voice-Powered Gate Vehicle Logging System",
        "Category": "Data Automation & IoT",
        "Tech": "Python, Speech-to-Text, SQLite, Streamlit",
        "Description": "A localized web tool that transcribes voice inputs to log strict parameters (plate numbers, vehicle types, models, colors) into a secure database.",
        "Link": "https://github.com/olumobigjoe"
    },
    {
        "Title": "Global Gadgets 3NF Relational Database",
        "Category": "Data Engineering",
        "Tech": "MS SQL Server, T-SQL, Database Normalization",
        "Description": "Designed and implemented a fully normalized 3NF enterprise database architecture optimizing complex e-commerce queries and data integrity.",
        "Link": "https://github.com/olumobigjoe"
    }
]
df_projects = pd.DataFrame(projects_data)

# --- HOME & OVERVIEW SECTION ---
if selection == "Home & Overview":
    col1, col2 = st.run_col if hasattr(st, 'run_col') else st.columns([2, 1]) # standard column split
    
    with col1:
        st.markdown('<p class="main-header">Hello, I\'m a Data Analyst & Academic Technologist 👋</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="sub-header">Specializing in data science, educational learning analytics, machine learning structures, '
            'and building scalable, interactive dashboard applications.</p>', 
            unsafe_allow_html=True
        )
        
        st.write("")
        st.write(
            "Welcome to my dynamic portfolio! Here, I merge rigorous academic research with practical data engineering "
            "and application development. Use the sidebar to look through my repositories, technical competencies, and live toolsets."
        )

    with col2:
        st.info("💡 **Quick Fact:** I build robust data architectures, automation scripts, and interactive web tools using Python and SQL.")

    st.markdown("---")
    
    # Quick metrics layout
    st.subheader("Career Snapshot")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Core Stack", value="Python & SQL", delta="Advanced")
    m2.metric(label="Cloud Cert", value="AWS Practitioner", delta="Certified")
    m3.metric(label="Domain Focus", value="Learning Analytics", delta="Active Research")
    m4.metric(label="Repositories", value="Open Source", delta="GitHub Active")

# --- PROJECTS EXPLORER SECTION ---
elif selection == "Projects Explorer":
    st.markdown('<p class="main-header">🚀 Featured Projects</p>', unsafe_allow_html=True)
    st.write("Filter through my key engineering and data analytics projects below:")

    # Interactive Filter
    category_filter = st.selectbox("Filter by Category:", ["All"] + list(df_projects["Category"].unique()))
    
    if category_filter != "All":
        filtered_df = df_projects[df_projects["Category"] == category_filter]
    else:
        filtered_df = df_projects

    for index, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"### {row['Title']}")
            st.markdown(f"**Category:** `{row['Category']}` | **Tech Stack:** `{row['Tech']}`")
            st.write(row['Description'])
            st.markdown(f"[View Repository / Source]({row['Link']})")
            st.markdown("---")

# --- SKILLS & ANALYTICS SECTION ---
elif selection == "Skills & Analytics":
    st.markdown('<p class="main-header">📈 Technical Competencies & Visualizer</p>', unsafe_allow_html=True)
    st.write("An interactive breakdown of my technical proficiency across different data tooling domains.")

    # Sample dataset for dynamic chart visualization
    skills_data = {
        "Skill Category": ["Python & Libraries", "SQL & Databases", "Data Visualization", "Cloud & DevOps", "Web Frameworks"],
        "Proficiency Score": [95, 90, 85, 75, 90],
        "Projects Count": [5, 4, 4, 2, 3]
    }
    df_skills = pd.DataFrame(skills_data)

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Proficiency Level Distribution")
        fig_bar = px.bar(
            df_skills, 
            x="Skill Category", 
            y="Proficiency Score", 
            color="Proficiency Score",
            color_continuous_scale="Blues",
            text="Proficiency Score"
        )
        fig_bar.update_layout(xaxis_title="", yaxis_title="Score (%)", showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        st.subheader("Skill Share Breakdown")
        fig_pie = px.pie(
            df_skills, 
            names="Skill Category", 
            values="Projects Count", 
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown('<p class="main-header">📬 Get in Touch</p>', unsafe_allow_html=True)
    st.write("Have a project in mind, want to collaborate on research, or looking for a data analyst? Drop a message below!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and message:
                st.success(f"Thank you, {name}! Your message has been noted. (To wire this to a live inbox, you can link it with an SMTP backend or Streamlit secrets).")
            else:
                st.error("Please fill in all fields before submitting.")