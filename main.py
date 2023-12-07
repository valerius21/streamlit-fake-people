import numpy as np
import streamlit as st
import pandas as pd


def process_csv(file) -> pd.DataFrame:
    df = pd.read_csv(file)

    # randomize age for every person
    df['Age'] = np.random.randint(5, 100, df.shape[0])

    return df


def main():
    st.title('Fake People')
    st.write("You can upload a csv or xlsx file with fake people.")
    uploaded_file = st.file_uploader('Upload a file', type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.subheader('Raw data')
        df = process_csv(uploaded_file)
        st.dataframe(df)
        st.write(f'Total: `{len(df)}` Entries')
        st.header('Filter data')
        age_range = st.slider('Age', 1, 100, (18, 25))
        st.subheader(f'Filtered Data for `age` from {age_range[0]} to {age_range[1]}')
        filtered_by_age = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
        st.dataframe(filtered_by_age)
        st.write(f'Total: `{len(filtered_by_age)}` Entries')
        st.download_button('Download Filtered Data', data=filtered_by_age.to_csv(), file_name='filtered_by_age_data.csv')
        st.header(f'Number of people by age from {age_range[0]} to {age_range[1]}')
        st.line_chart(filtered_by_age['Age'].value_counts())
    else:
        st.write('No file uploaded. Please upload some fake people.')


main()
