import streamlit as st

# Set the page title
st.set_page_config(page_title="Bandla Venu Madhav's ML Engineer Portfolio", page_icon=":star:", layout="wide")

# Title and Introduction
st.title("Bandla Venu Madhav")
st.write("Aspiring Machine Learning Engineer with experience in software development and data science. Proficient in Python, SQL, and tools for data analysis and visualization. Passionate about building ML models to derive insights and solve complex problems.")

# Contact Information
st.header("Contact Information")
st.write("📧 [venumadhav.07.24@gmail.com](mailto:venumadhav.07.24@gmail.com)")
st.write("📞 +91 84381 06497")
st.write("🔗 [GitHub](https://github.com/venumadhav2407) | [LinkedIn](https://linkedin.com/in/venumadhav07) | [Kaggle](https://www.kaggle.com/venumadhav06)")

# Skills Section
st.header("Skills")
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

# Work Experience Section
st.header("Work Experience")
st.write("**Innervex Technology, Madurai** (May 2023 -- May 2024)")
st.write("- Debugged and fixed application issues, reducing downtime by 30%.")
st.write("- Utilized SQL for data management, improving retrieval times by 20%.")
st.write("- Developed features and optimized code, enhancing scalability and performance.")
st.write("- Collaborated on API integration, gaining expertise in testing and documentation.")

# Projects Section
st.header("Projects")
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

# Education Section
st.header("Education")
st.write("**T.J.S Engineering College** (Jul 2019 -- Jun 2023)")
st.write("**BE in Computer Science** | **CGPA:** 8.6 / 10")

# Certifications Section
st.header("Certifications")
st.write("- Python Programming Course: [Kaggle Certification](https://www.kaggle.com/learn/certification/venumadhav06/python)")
st.write("- Introduction to Cloud Computing: [Udemy](https://www.udemy.com/certificate/UC-436c2f12-3de2-4239-a137-0054833d290c)")
st.write("- Time Complexity: [CodeChef](https://www.codechef.com/certificates/public/6f4af74)")
st.write("- Git and GitHub for Beginners: [Udemy](https://www.udemy.com/certificate/UC-20344013-512f-42df-8470-a084c26522d3)")

# Languages Section
st.header("Languages")
st.write("English, Telugu, Tamil")

# Hobbies Section
st.header("Hobbies")
st.write("- Learning new technologies")
st.write("- Content writing")
st.write("- Coding practice")

# Download Resume Section
st.header("Download My Resume")
with open("Bandla_Venumadhav_resume.pdf", "rb") as file:
    btn = st.download_button(
        label="Download Resume",
        data=file,
        file_name="Bandla_Venu_Madhav_Resume.pdf",
        mime="application/pdf"
    )

# Footer
st.markdown("---")
st.write("Created with ❤️ by Bandla Venu Madhav")
