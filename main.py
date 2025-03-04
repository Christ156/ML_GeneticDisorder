import streamlit as st
import pickle
import pandas as pd

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

def advancedPredict():
    st.title("Let's predict your disorder")

    # Biodata diri
    name = st.text_input('Nama')
    gender = st.pills("Gender", ["Men", "Women", "Ambiguous"], selection_mode="single", key="Gender")
    if gender == "Men":
        gender = 2
    elif gender == "Women":
        gender = 1
    else:
        gender = 0

    age = st.slider("Usia anda", 0, 120, 20)

    st.divider()

    col1, col2 = st.columns(2)

    # Skrining
    with col1:
        totalBloodCell = 0

        redBloodCellCount = st.number_input("Red Blood Cell Count (mcL)")
        whiteBloodCellCount = st.number_input("White Blood Cell Count (mcL)")
        totalBloodCell = redBloodCellCount + whiteBloodCellCount

        folicAcid = st.pills("Folic Acid details", ["Yes", "No"], selection_mode="single", key="folicAcid")
        if folicAcid == "Yes":
            folicAcid = 1
        else:
            folicAcid = 0

        totalSymtomps = 0

        symptom1 = st.checkbox("Symptom 1")
        if symptom1 == True:
            symptom1 = 1.0
            totalSymtomps += 1
        else:
            symptom1 = 0.0
        symptom2 = st.checkbox("Symptom 2")
        if symptom2 == True:
            symptom2 = 1.0
            totalSymtomps += 1
        else:
            symptom2 = 0.0
        symptom3 = st.checkbox("Symptom 3")
        if symptom3 == True:
            symptom3 = 1.0
            totalSymtomps += 1
        else:
            symptom3 = 0.0
        symptom4 = st.checkbox("Symptom 4")
        if symptom4 == True:
            symptom4 = 1.0
            totalSymtomps += 1
        else:
            symptom4 = 0.0
        symptom5 = st.checkbox("Symptom 5")
        if symptom5 == True:
            symptom5 = 1.0
            totalSymtomps += 1
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

    @st.dialog("Hasil Diagnosis")
    def prediction_full_modal():
        full_model = pickle.load(open('disorder_subclass_final.sav', 'rb'))
        full_proba = full_model.predict_proba([[genesMom, inheritDad, maternalGen, paternalGen, folicAcid, whiteBloodCellCount, symptom1, symptom2, symptom3, symptom4, symptom5, totalBloodCell, totalSymtomps, gender]])
        full_prediction = full_model.predict([[genesMom, inheritDad, maternalGen, paternalGen, folicAcid, whiteBloodCellCount, symptom1, symptom2, symptom3, symptom4, symptom5, totalBloodCell, totalSymtomps, gender]])
        full_diagnosis = ""

        if full_prediction[0] == 0:
            full_diagnosis = "Alzheimer's"
        elif full_prediction[0] == 1:
            full_diagnosis = "Cancer"
        elif full_prediction[0] == 2:
            full_diagnosis = "Cystic fibrosis"
        elif full_prediction[0] == 3:
            full_diagnosis = "Diabetes"
        elif full_prediction[0] == 4:
            full_diagnosis = "Hemochromatosis"
        elif full_prediction[0] == 5:
            full_diagnosis = "Leber's hereditary optic neuropathy"
        elif full_prediction[0] == 6:
            full_diagnosis = "Leigh syndrome"
        elif full_prediction[0] == 7:
            full_diagnosis = "Mitochondrial myopathy"
        else:
            full_diagnosis = "Tay-Sachs"

        percentDiag = "{:.2f}".format(full_proba[0][full_prediction[0]]*100)
        st.write(name, "dengan usia", age, "mengidap penyakit turunan", full_diagnosis, " dengan prosentase sebesar ", float(percentDiag), "%")

        st.title("Probabilitas terkena genetic disorder lain:")
        st.bar_chart(full_proba[0]*100, x_label="Disorder Class", y_label="Percentage")

        i = 0
        for x in full_proba[0]:
            if i != full_prediction[0]:
                if i == 0:
                    x = "{:.2f}".format(x*100)
                    st.write("0. Alzheimer's : ", float(x), "%")
                elif i == 1:
                    x = "{:.2f}".format(x*100)
                    st.write("1. Cancer : ", float(x), "%")
                elif i == 2:
                    x = "{:.2f}".format(x*100)
                    st.write("2. Cystic fibrosis : ", float(x), "%")
                elif i == 3:
                    x = "{:.2f}".format(x*100)
                    st.write("3. Diabetes : ", float(x), "%")
                elif i == 4:
                    x = "{:.2f}".format(x*100)
                    st.write("4. Hemochromatosis : ", float(x), "%")
                elif i == 5:
                    x = "{:.2f}".format(x*100)
                    st.write("5. Leber's hereditary optic neuropathy : ", float(x), "%")
                elif i == 6:
                    x = "{:.2f}".format(x*100)
                    st.write("6. Leigh syndrome : ", float(x), "%")
                elif i == 7:
                    x = "{:.2f}".format(x*100)
                    st.write("7. Mitochondrial myopathy : ", float(x), "%")
                else:
                    x = "{:.2f}".format(x*100)
                    st.write("8. Tay-Sachs : ", float(x), "%")
            i+=1

    if "full_predict" not in st.session_state:
        if st.button("Submit", key="fullPredict"):
            prediction_full_modal()

pg = st.navigation([st.Page(homePage, title="Home"), st.Page(advancedPredict, title="Prediction")])
pg.run()