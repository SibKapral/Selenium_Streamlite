import streamlit as st
import pandas as pd
from defs import hh_to_df, list_columns_dicts, spliting_columns, map_f, number_of_vacancies, average_value_salary_from_to
from selenium_func import selen_func
from change_for_resume import send_resume, view_resume
import plotly.express as px

# Инициализация session_state
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

citys_list = {
    "Москва": 1,
    "Санкт-Петербург": 2,
    "Екатеринбург": 3,
    "Новосибирск": 4,
    "Ростов-на-Дону": 76
}

with st.sidebar:
    st.markdown(
        '<h3><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/HeadHunter_logo.png/200px-HeadHunter_logo.png" height="40">&nbsp Interactive Dashboard</h3>',
        unsafe_allow_html=True)
    st.markdown(
        '<h6>by <a href="https://github.com/Balalaika1">Balalaika1</a></h6>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    title = st.text_input('Сhoose a profession 👷', 'Аналитик')
    st.markdown("---")
    radio_widget = st.radio(
        label="Select a city 🏙️",
        key="visibility",
        options=citys_list.keys(),
    )
    st.markdown("---")
    period = st.slider('The number of days within which the vacancy is published on the site 📆', 1, 100, 1)
    value_area = citys_list[radio_widget]

    if st.button('Refresh'):
        st.session_state.df = hh_to_df(title, value_area, period)
        st.session_state.df = spliting_columns(list_columns_dicts(st.session_state.df), st.session_state.df)
        st.session_state.df = spliting_columns(list_columns_dicts(st.session_state.df), st.session_state.df)
        st.session_state.df.to_excel('main3.xlsx')

if not st.session_state.df.empty:
    tab1, tab2 = st.tabs(["📊 Analysis and visualization", "🤖 Automation"])
    
    with tab1:
        a = number_of_vacancies(st.session_state.df)
        b = average_value_salary_from_to(st.session_state.df)
        c1, c2, c3 = st.columns(3)
        c1.metric("Vacancies found", a[0])
        c2.metric("Vacancies where salary specified", a[1])
        c3.metric("Average salary", b)
        fig = map_f(st.session_state.df)
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("Download table 📥"):
            st.dataframe(st.session_state.df)
            with open("main3.xlsx", "rb") as file:
                btn = st.download_button(
                    label="Download excel file",
                    data=file,
                    file_name="main.xlsx"
                )
    with tab2:

        #bytes_data = 1           
        with st.expander("Alternative 📥"):
            uploaded_files = st.file_uploader('Choose a XLSX file with "apply_alternate_url"', accept_multiple_files=True, type=['xlsx'])
            for uploaded_file in uploaded_files:
                bytes_data = pd.read_excel(uploaded_file)
                st.markdown("---")
                data_add = st.dataframe(bytes_data)
        
        salary_check = st.checkbox('With salary')
        if "age_slider_value" not in st.session_state:
            #st.session_state.age_slider_value = 25
            c1, c2 = st.columns(2)
            with c1:
                min_salary = st.number_input('Minimum salary', value = 100000)
            with c2:
                num_vacanc = st.number_input('Vacancies quantity', value = 200, max_value = 200)
            #st.session_state.age_slider_value = age
        c1, c2 = st.columns(2)
        with c1:
            login = st.text_input('Login', '')
        with c2:
            passwd = st.text_input('Password', '')
        st.markdown("---")



        c1, c2 = st.columns(2)
        with c1:
            if st.button('Generate list', key='button_feedbacks'):
                df1 = st.session_state.df
                if 'bytes_data' in globals():
                    data_urls = view_resume(salary_check, min_salary, df1, bytes_data, num_vacanc)
                else:
                    data_urls = view_resume(salary_check, min_salary, df1, None, num_vacanc)
                st.dataframe(data_urls)
        with c2:
            if st.button('SEND RESUME', key='button_feedbacks2'):
                df1 = st.session_state.df
                if 'bytes_data' in globals():
                    urls = send_resume(salary_check, min_salary, st.session_state.df, bytes_data, num_vacanc)
                else:
                    urls = send_resume(salary_check, min_salary, df1, None, num_vacanc)
                quantity_urls = len(urls)
                a = 1
                with st.status("Parsing..."):
                    st.write("Searching for data...")
                    driver = selen_func(login, passwd)
                    for url_one in urls:
                        driver.get(url_one)
                        st.write(f"{a} of {quantity_urls} processed")
                        a = a+1


else:
    st.markdown('<h3>Select the data and click the refresh button 😉</h3>', unsafe_allow_html=True)


        #if st.button('Send resume', key='button_feedbacks'):
        #    urls = send_resume(salary_check, min_salary, st.session_state.df, bytes_data, num_vacanc)
        #    quantity_urls = len(urls)
        #    a = 1
        #    with st.spinner("Parsing..."):
        #        st.write("Searching for data...")
        #        driver = selen_func(login, passwd)
        #        for url_one in urls:
        #            driver.get(url_one)
        #            st.write(f"{a}/{quantity_urls}")
        #            a = a+1



        #with c2:
        #    if st.button('SEND RESUME', key='button_feedbacks2'):
        #        df1 = st.session_state.df
        #        if 'bytes_data' in globals():
        #            urls = view_resume(salary_check, min_salary, df1, bytes_data, num_vacanc)
        #        else:
        #            urls = view_resume(salary_check, min_salary, df1, None, num_vacanc)
        #        st.dataframe(ur
