import streamlit as st
from streamlit_option_menu import option_menu

# Set the page title
st.set_page_config(page_title="Bandla Venu Madhav's ML Engineer Portfolio", page_icon=":star:", layout="wide")

# Title
st.title("Bandla Venu Madhav")

# Create a sidebar menu
with st.sidebar:
    selected = option_menu("Menu", ["About", "Skills", "Projects", "Contact Information"],
                           icons=["person", "list-check", "file-earmark-text", "envelope"],
                           menu_icon="cast", default_index=0)

# About Section
if selected == "About":
    st.info("Experienced Software Developer transitioning into Data Science. Skilled in Python, SQL, PowerBI, and Excel for data visualization. Proficient in web app development, database management, and data manipulation. Leveraging analytical skills for Data Science role.")
# Skills Section
elif selected == "Skills":
    st.title("Skills")
    st.write("**Languages:** `Python`, `JavaScript`, `HTML/CSS`, `PHP`, `SQL`")
    st.write("**Data Science:** Pandas, Numpy, Matplotlib, Power BI, Machine Learning, Data Visualization, Data Wrangling")
    st.write("**Tools:** Git/GitHub, Jupyter Notebooks, MS Excel")
    st.write("**Soft Skills:** Problem-solving, Collaboration, Analytical Thinking")


# Projects Section
elif selected == "Projects":
    st.header("Projects")
    
    st.subheader("Redbus Streamlit Application (Sep 2024)")
    st.write("**Technologies:** Python, Selenium, Streamlit, SQLite")
    st.write("- Developed web scraping scripts, increasing data collection speed by 50%.")
    st.write("- Implemented dynamic filtering using Streamlit to enhance user experience.")
    st.write("- [GitHub Repository](https://github.com/venumadhav2407/redbus_streamlit_app)")
    st.write("- [Demo link](https://redbus-app.streamlit.app/)")

    st.subheader("YouTube Ad View Prediction (Jul 2024)")
    st.write("**Technologies:** Python, Pandas, Numpy, Matplotlib, Scikit-Learn")
    st.write("- Applied label encoding and used ML algorithms including Linear Regression and Random Forest.")
    st.write("- Conducted cross-validation to fine-tune models and improve accuracy.")
    st.write("- [GitHub Repository](https://github.com/venumadhav2407/youtube_adview_prediction_ml)")

    st.subheader("Music Player Using Flask (Apr 2024 -- May 2024)")
    st.write("**Technologies:** Flask, Jinja Templates")
    st.write("- Developed a web-based music player with search and play functionality.")
    st.write("- Integrated a secure login system to protect user privacy and data.")
    st.write("- [GitHub Repository](https://github.com/venumadhav2407/music-player)")

# Contact Information Section
elif selected == "Contact Information":
    st.header("Contact Information")
    st.write("📧 [venumadhav.07.24@gmail.com](mailto:venumadhav.07.24@gmail.com)")
    st.write("📞 +91 84381 06497")
    st.write("🔗 [GitHub](https://github.com/venumadhav2407) | [LinkedIn](https://linkedin.com/in/venumadhav07) | [Kaggle](https://www.kaggle.com/venumadhav06)")

# Footer
st.markdown("---")
st.write("Created with ❤️ by Bandla Venu Madhav")
