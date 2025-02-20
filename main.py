import streamlit as st
import pickle

st.logo("logoLabrakadabra.png", size="large", icon_image="logoLabrakadabra.png")

def homePage():
    st.title("Ayo kenali penyakit turunan anda sejak dini")
    st.image(image="doctor.png", width=300)

    st.subheader("Apa itu Genetic Disorder?", divider=True)
    st.text("Genetic disorder adalah penyakit akibat perubahan (mutasi) pada gen tertentu. Kondisi ini bisa diturunkan dari orang tua kepada anak, atau terjadi secara acak akibat paparan faktor tertentu.")
    st.text("Gen adalah materi genetik yang terdiri dari DNA sebagai penentu karakteristik fisik yang dimiliki orang, seperti warna kulit, rambut, dan mata, serta kerentanan terhadap penyakit tertentu. Gen sendiri diwariskan dari kedua orang tua kepada anaknya. Pada kelainan genetik, anak bisa mewarisi gen yang rusak dari salah satu maupun kedua orang tua. Hal ini membuat anak lebih berisiko menderita kelainan genetik sejak lahir. Selain terjadi sejak lahir, kelainan genetik dapat berkembang selama masa hidup penderitanya akibat paparan faktor tertentu, seperti penggunaan obat-obatan atau paparan zat kimia.")

    st.subheader("Penyebab Kelainan Genetik", divider=True)
    st.subheader("Gangguan kromosom")
    st.text("Normalnya, anak mewarisi 23 kromosom dari ayah dan ibunya sehingga totalnya adalah 46 kromosom. Kelainan genetik berupa gangguan kromosom terjadi karena perubahan pada bentuk maupun jumlah kromosom. Beberapa penyakit yang disebabkan oleh kelainan kromosom adalah sindrom Down, sindrom Pitt-Hopkins, sindrom Patau atau trisomi 13, sindrom Treacher Collins, dan sindrom Klinefelter.")

    st.subheader("Multifaktorial atau kompleks")
    st.text("Jenis kelainan genetik ini terjadi akibat kombinasi perubahan pada beberapa gen tertentu dan faktor lain, seperti paparan zat kimia, penggunaan obat-obatan, atau kekurangan zat gizi tertentu. Contoh kelainan genetik kompleks adalah kanker, autisme, spina bifida, dan penyakit Alzheimer.")

    st.subheader("Monogenik atau cacat gen tunggal")
    st.text("Monogenik adalah kelainan genetik yang disebabkan oleh perubahan pada gen tertentu. Kondisi ini bisa diturunkan kepada anak apabila salah satu atau kedua orang tua memiliki kelainan genetik yang sama atau menjadi pembawa (carrier) kelainan gen tersebut. Beberapa kelainan monogenik adalah cystic fibrosis, hiperkolesterolemia familial, hemokromatosis, anemia sel sabit, Swyer syndrome, sindrom Isaac, sindrom Barber Say, dan abetalipoproteinemia, sindrom Usher, atau Zellweger spectrum disorders.")

    st.subheader("Faktor risiko kelainan genetik", divider=True)
    st.text("Beberapa faktor yang dapat meningkatkan risiko seseorang terkena kelainan genetik adalah paparan zat kimia, sinar radiasi, dan sinar ultraviolet (UV), serta kebiasaan merokok.")

    st.subheader("Kapan harus ke dokter?", divider=True)
    st.text("Lakukan skrining genetik ke dokter sebelum merencanakan kehamilan. Tujuannya adalah untuk mengetahui seberapa besar kelainan genetik menurun kepada anak. Skrining genetik juga bisa dilakukan pada bayi yang baru lahir untuk mendeteksi adanya kelainan genetik. Segera bawa anak ke dokter jika ia pertumbuhan dan perkembangannya terlambat walaupun telah mendapat nutrisi yang cukup, atau mengalami cacat pada anggota tubuh tertentu.")

def simplePredict():
    st.title("Simple prediction")

    # Biodata diri
    name = st.text_input('Nama')
    age = st.slider("Usia anda", 0, 120, 20)

    st.divider()

    col1, col2 = st.columns(2)

    # Skrining

    with col1:
        hOsubstanceAbuse = st.pills("H/O Substance abuse", ["Yes", "No"], selection_mode="single", key="hOsubstanceAbuse")
        if hOsubstanceAbuse == "Yes":
            hOsubstanceAbuse = 1
        else:
            hOsubstanceAbuse = 0

        autopsyBirthDefect = st.pills("Autopsy shows birth defect", ["Yes", "No"], selection_mode="single", key="autopsyBirthDefect")
        if autopsyBirthDefect == "Yes":
            autopsyBirthDefect = 1
        else:
            autopsyBirthDefect = 0

        symptom1 = st.checkbox("Symptom 1")
        if symptom1 == True:
            symptom1 = 1.0
        else:
            symptom1 = 0.0
        symptom2 = st.checkbox("Symptom 2")
        if symptom2 == True:
            symptom2 = 1.0
        else:
            symptom2 = 0.0
        symptom3 = st.checkbox("Symptom 3")
        if symptom3 == True:
            symptom3 = 1.0
        else:
            symptom3 = 0.0
        symptom4 = st.checkbox("Symptom 4")
        if symptom4 == True:
            symptom4 = 1.0
        else:
            symptom4 = 0.0
        symptom5 = st.checkbox("Symptom 5")
        if symptom5 == True:
            symptom5 = 1.0
        else:
            symptom5 = 0.0
    with col2:
        genesMom = st.checkbox("Genes in mother's side")
        if genesMom == True:
            genesMom = 1
        else:
            genesMom = 0
        inheritDad = st.checkbox("Inherited from father")
        if inheritDad == True:
            inheritDad = 1
        else:
            inheritDad = 0
        maternalGen = st.checkbox("Maternal gene")
        if maternalGen == True:
            maternalGen = 1
        else:
            maternalGen = 0
        paternalGen = st.checkbox("Paternal gene")
        if paternalGen == True:
            paternalGen = 1
        else:
            paternalGen = 0
    st.divider()

    @st.dialog("Simple Diagnosis Result")
    def prediction_simple_modal():
        simple_model = pickle.load(open('disorder_subclass_simple.sav', 'rb'))
        simple_prediction = simple_model.predict([[genesMom, inheritDad, maternalGen, paternalGen, autopsyBirthDefect, hOsubstanceAbuse, symptom1, symptom2, symptom3, symptom4, symptom5]])
        
        # st.write(name, "dengan usia", age, "mengidap penyakit turunan ")
        if simple_prediction[0] == 0:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Alzheimer's")
        elif simple_prediction[0] == 1:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Cancer")
        elif simple_prediction[0] == 2:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Cystic fibrosis")
        elif simple_prediction[0] == 3:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Diabetes")
        elif simple_prediction[0] == 4:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Hemochromatosis")
        elif simple_prediction[0] == 5:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Leber's hereditary optic neuropathy")
        elif simple_prediction[0] == 6:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Leigh syndrome")
        elif simple_prediction[0] == 7:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Mitochondrial myopathy")
        else:
            st.write("Tay-Sachs")

    if "simple_predict" not in st.session_state:
        if st.button("Submit", key="simplePredict"):
            prediction_simple_modal()

def advancedPredict():
    st.title('Advanced predict')

    # Biodata diri
    name = st.text_input('Nama')
    age = st.slider("Usia anda", 0, 120, 20)

    st.divider()

    col1, col2 = st.columns(2)

    # Skrining

    with col1:
        bloodCellCount = st.number_input("Blood Cell Count (mcL)")
        followUp = st.pills("Follow-up", ["High", "Low"], selection_mode="single")
        if followUp == "Low":
            followUp = 1
        else:
            followUp = 0

        hOradiationExposure = st.pills("H/O Radiation exposure (X-Ray)", ["Yes", "No"], selection_mode="single", key="hOradiationExposure")
        if hOradiationExposure == "Yes":
            hOradiationExposure = 1
        else:
            hOradiationExposure = 0

        hOsubstanceAbuse = st.pills("H/O Substance abuse", ["Yes", "No"], selection_mode="single", key="hOsubstanceAbuse")
        if hOsubstanceAbuse == "Yes":
            hOsubstanceAbuse = 1
        else:
            hOsubstanceAbuse = 0  

        birthDefect = st.pills("Birth defects", ["Singular", "Multiple"], selection_mode="single", key="birthDefect")
        if birthDefect == "Singular":
            birthDefect = 1
        else:
            birthDefect = 0 

        birthAsphyxia = st.pills("Birth asphyxia", ["Yes", "No"], selection_mode="single", key="birthAsphyxia")
        if birthAsphyxia == "Yes":
            birthAsphyxia = 1
        else:
            birthAsphyxia = 0

        whiteBloodCellCount = st.number_input("White blood cell count (thousand per microliter)")
        bloodTestResult = st.pills("Blood test result", ["Normal", "Abnormal", "Slightly abnormal", "Inconclusive"], selection_mode="single", key="bloodTestResult")
        if bloodTestResult == "Normal":
            bloodTestResult = 2
        elif bloodTestResult == "Abnormal":
            bloodTestResult = 0
        elif bloodTestResult == "Slightly abnormal":
            bloodTestResult = 3            
        elif bloodTestResult == "Inconclusive":
            bloodTestResult = 1

        symptom1 = st.checkbox("Symptom 1")
        if symptom1 == True:
            symptom1 = 1.0
        else:
            symptom1 = 0.0
        symptom2 = st.checkbox("Symptom 2")
        if symptom2 == True:
            symptom2 = 1.0
        else:
            symptom2 = 0.0
        symptom3 = st.checkbox("Symptom 3")
        if symptom3 == True:
            symptom3 = 1.0
        else:
            symptom3 = 0.0
        symptom4 = st.checkbox("Symptom 4")
        if symptom4 == True:
            symptom4 = 1.0
        else:
            symptom4 = 0.0
        symptom5 = st.checkbox("Symptom 5")
        if symptom5 == True:
            symptom5 = 1.0
        else:
            symptom5 = 0.0

    with col2:
        momAge = st.slider("Mother's age", 0, 120, 20)
        DadAge = st.slider("Father's age", 0, 120, 20)
        genesMom = st.checkbox("Genes in mother's side")
        if genesMom == True:
            genesMom = 1
        else:
            genesMom = 0

        inheritDad = st.checkbox("Inherited from father")
        if inheritDad == True:
            inheritDad = 1
        else:
            inheritDad = 0

        maternalGen = st.checkbox("Maternal gene")
        if maternalGen == True:
            maternalGen = 1
        else:
            maternalGen = 0

        status = st.pills("Status", ["Alive", "Deceased"], selection_mode="single", key="status")
        if status == "Alive":
            status = 0
        else:
            status = 1

    st.divider()

    @st.dialog("Full Diagnosis Result")
    def prediction_full_modal():
        full_model = pickle.load(open('disorder_subclass_full.sav', 'rb'))
        full_prediction = full_model.predict([[genesMom, inheritDad, maternalGen, momAge, DadAge, status, followUp, birthAsphyxia, birthDefect, hOradiationExposure, hOsubstanceAbuse, whiteBloodCellCount, bloodTestResult, symptom1, symptom2, symptom3, symptom4, symptom5, bloodCellCount]])

        if full_prediction[0] == 0:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Alzheimer's")
        elif full_prediction[0] == 1:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Cancer")
        elif full_prediction[0] == 2:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Cystic fibrosis")
        elif full_prediction[0] == 3:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Diabetes")
        elif full_prediction[0] == 4:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Hemochromatosis")
        elif full_prediction[0] == 5:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Leber's hereditary optic neuropathy")
        elif full_prediction[0] == 6:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Leigh syndrome")
        elif full_prediction[0] == 7:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Mitochondrial myopathy")
        else:
            st.write(name, "dengan usia", age, "mengidap penyakit turunan Tay-Sachs")

    if "full_predict" not in st.session_state:
        if st.button("Submit", key="fullPredict"):
            prediction_full_modal()

pg = st.navigation([st.Page(homePage, title="Home"), st.Page(simplePredict, title="Simple prediction"), st.Page(advancedPredict, title="Advanced prediction")])
pg.run()