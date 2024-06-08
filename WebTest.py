import streamlit as st
import pandas as pd

data = pd.read_excel('D:/Unsri/Semester 4/Kecerdasan Buatan/Projek/Data Karir.xlsx')

st.write("""# Rekomendasi Pemilihan Karir""")
st.write("""Job Recommendation""")

# Linear search function
def linear_search(data, key_skills, industries):
    rekomendasi = {}

    for index, row in data.iterrows():
        if isinstance(row["Key Skills"], str) and isinstance(row["Industry"], str):
            row_skills = row["Key Skills"].lower()
            row_industries = row["Industry"].lower()

            for skill in key_skills:
                for industry in industries:
                    if skill.strip().lower() in row_skills and industry.strip().lower() in row_industries:
                        job_title = row["Job Title"]
                        if job_title not in rekomendasi:
                            rekomendasi[job_title] = 1
                        else:
                            rekomendasi[job_title] += 1

    # Sort recommendations by highest score and filter out zero scores
    sorted_rekomendasi = [(job_title, skor) for job_title, skor in sorted(rekomendasi.items(), key=lambda x: x[1], reverse=True) if skor > 0]
    return sorted_rekomendasi

# User input
key_skills_input = st.text_input("Masukkan Kemampuan (jika lebih dari 1, pisahkan dengan koma): ")
industries_input = st.text_input("Masukkan Minat (jika lebih dari 1, pisahkan dengan koma): ")

# Split input into lists
key_skills = key_skills_input.split(',') if key_skills_input else []
industries = industries_input.split(',') if industries_input else []

if st.button("Cari"):
    hasil_rekomendasi = linear_search(data, key_skills, industries)

    if hasil_rekomendasi:
        st.write("Pekerjaan yang paling sesuai dengan preferensi Anda:")
        for job_title, skor in hasil_rekomendasi[:10]:
            st.write("-", job_title)
    else:
        st.write("Tidak ada rekomendasi pekerjaan yang sesuai dengan preferensi Anda.")
