import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title('ITA Index Resolver')

# Upload CSV file
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Transpose the DataFrame's header into a new DataFrame
    transpose_df = pd.DataFrame(df.columns, columns=['column name'])
    
    # Available columns for selection
    available_columns = transpose_df['column name'].tolist()

    #Auto Select columns based on keywords
    percentage_keywords = ['%','+/-','change','percent','conv','leverage']
    currency_keywords = ['sale','ads','aur','revenue','s2d','bopis'] 
    decimal_keywords = ['upt']
    number_keywords = ['unit','trans']
    colvis_keywords = ['measurement','rank']
    hidden_keywords = ['time','rank','region','district','date']

# [element for element in my_array if any(keyword in element for keyword in currency_keywords)]
    
    # Create multiselect dropdowns for different column types
    percentage_columns = st.multiselect(
        'Select percentage columns',
        options=available_columns,
        default=[col for col in available_columns if any(keyword in col.lower() for keyword in percentage_keywords)]
    )
    
    available_columns = [col for col in available_columns if col not in percentage_columns]

    currency_columns = st.multiselect(
        'Select currency columns',
        options=available_columns,
        default=[col for col in available_columns if any(keyword in col.lower() for keyword in currency_keywords) and not any(keyword in col.lower() for keyword in percentage_keywords) ]
    )
    
    # Update available columns
    available_columns = [col for col in available_columns if col not in currency_columns]
    
    numerical_columns = st.multiselect(
        'Select numerical columns',
        options=available_columns,
        default=[col for col in available_columns if any(keyword in col.lower() for keyword in number_keywords)]
    )
    
    available_columns = [col for col in available_columns if col not in numerical_columns]
    
    decimal_columns = st.multiselect(
        'Select decimal columns',
        options=available_columns,
        default=[col for col in available_columns if any(keyword in col.lower() for keyword in decimal_keywords)]
    )
    
    available_columns = [col for col in available_columns if col not in decimal_columns]
    
    colvis_columns = st.multiselect(
        'Select colvis columns',
        options=available_columns,
        default=[col for col in available_columns if any(keyword in col.lower() for keyword in colvis_keywords)]
    )
    
    # available_columns = [col for col in available_columns if col not in colvis_columns]
    
    hidden_columns = st.multiselect(
        'Select hidden columns',
        options=available_columns,
        default=[col for col in available_columns if any(keyword in col.lower() for keyword in hidden_keywords)]
    )
    
    # Add selections to the DataFrame for visualization
    transpose_df['Currency'] = transpose_df['column name'].apply(lambda x: x in currency_columns)
    transpose_df['Percentage'] = transpose_df['column name'].apply(lambda x: x in percentage_columns)
    transpose_df['Numerical'] = transpose_df['column name'].apply(lambda x: x in numerical_columns)
    transpose_df['Decimal'] = transpose_df['column name'].apply(lambda x: x in decimal_columns)
    transpose_df['Colvis'] = transpose_df['column name'].apply(lambda x: x in colvis_columns)
    transpose_df['Hidden'] = transpose_df['column name'].apply(lambda x: x in hidden_columns)
    
    # Display the updated DataFrame with selections
    st.dataframe(transpose_df)
    
    # Display the lists of selected columns and their index numbers
    st.write("Selected Currency Columns:", currency_columns)
    st.write("Index Numbers:", [df.columns.get_loc(col) for col in currency_columns])
    
    st.write("Selected Percentage Columns:", percentage_columns)
    st.write("Index Numbers:", [df.columns.get_loc(col) for col in percentage_columns])
    
    st.write("Selected Numerical Columns:", numerical_columns)
    st.write("Index Numbers:", [df.columns.get_loc(col) for col in numerical_columns])
    
    st.write("Selected Decimal Columns:", decimal_columns)
    st.write("Index Numbers:", [df.columns.get_loc(col) for col in decimal_columns])
    
    st.write("Selected Colvis Columns:", colvis_columns)
    st.write("Index Numbers:", [df.columns.get_loc(col) for col in colvis_columns])
    
    st.write("Selected Hidden Columns:", hidden_columns)
    st.write("Index Numbers:", [df.columns.get_loc(col) for col in hidden_columns])
else:
    st.write("Please upload a CSV file to proceed.")
