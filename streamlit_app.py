import streamlit as st

# Set the page title
st.set_page_config(page_title="Bandla Venu Madhav's ML Engineer Portfolio", page_icon=":star:", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select a Section", ("About", "Skills", "Projects", "Contact Information"))

# About Section
if menu == "About":
    st.title("About Me")
    st.write("Aspiring Machine Learning Engineer with experience in software development and data science. Proficient in Python, SQL, and tools for data analysis and visualization. Passionate about building ML models to derive insights and solve complex problems.")

# Skills Section
elif menu == "Skills":
    st.title("Skills")
    st.subheader("Programming Languages")
    st.write("Python, SQL, JavaScript, HTML/CSS, PHP")
    st.subheader("Data Science Libraries")
    st.write("Pandas, Numpy, Matplotlib, Scikit-Learn, TensorFlow, PyTorch")
    st.subheader("Machine Learning Techniques")
    st.write("Supervised Learning, Unsupervised Learning, Neural Networks, Model Evaluation")
    st.subheader("Tools and Technologies")
    st.write("Git/GitHub, Jupyter Notebooks, Postman, Power BI, MS Excel")
    st.subheader("Soft Skills")
    st.write("Problem-solving, Collaboration, Analytical Thinking")

# Projects Section
elif menu == "Projects":
    st.title("Projects")
    
    st.subheader("Redbus Streamlit Application (Sep 2024)")
    st.write("**Technologies:** Python, Selenium, Streamlit, SQLite")
    st.write("- Developed web scraping scripts, increasing data collection speed by 50%.")
    st.write("- Implemented dynamic filtering using Streamlit to enhance user experience.")
    st.write("- [GitHub Repository](https://github.com/venumadhav2407/redbus_streamlit_app)")

    st.subheader("YouTube Ad View Prediction (Jul 2024)")
    st.write("**Technologies:** Python, Pandas, Numpy, Matplotlib, Scikit-Learn")
    st.write("- Applied label encoding and used ML algorithms including Linear Regression and Random Forest.")
    st.write("- Conducted cross-validation to fine-tune models and improve accuracy.")

    st.subheader("Music Player Using Flask (Apr 2024 -- May 2024)")
    st.write("**Technologies:** Flask, Jinja Templates")
    st.write("- Developed a web-based music player with search and play functionality.")
    st.write("- Integrated a secure login system to protect user privacy and data.")

# Contact Information Section
elif menu == "Contact Information":
    st.title("Contact Information")
    st.write("📧 [venumadhav.07.24@gmail.com](mailto:venumadhav.07.24@gmail.com)")
    st.write("📞 +91 84381 06497")
    st.write("🔗 [GitHub](https://github.com/venumadhav2407) | [LinkedIn](https://linkedin.com/in/venumadhav07) | [Kaggle](https://www.kaggle.com/venumadhav06)")

# Footer
st.markdown("---")
st.write("Created with ❤️ by Bandla Venu Madhav")
