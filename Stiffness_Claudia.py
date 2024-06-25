import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def process_file(file):
    lines = file.readlines()
    lines = [line.decode("utf-8") for line in lines]  # Decode lines to string

    # Find the index of the line containing "N O D E   O U T P U T"
    node_output_index = next(i for i, line in enumerate(lines) if "N O D E   O U T P U T" in line)

    # Extract lines starting with "        87      " and "        89      " after the "N O D E   O U T P U T" line
    extracted_lines_87 = []
    extracted_lines_89 = []
    for line in lines[node_output_index+1:]:
        if line.startswith("        87      "):
            extracted_lines_87.append(line.strip())
        elif line.startswith("        89      "):
            extracted_lines_89.append(line.strip())

    # Process the extracted lines to get the 6 groups of real numbers
    data_87 = []
    for line in extracted_lines_87:
        parts = line.split()
        if len(parts) == 7:  # We expect 7 parts, the first being the identifier and the rest being the values
            data_87.append(parts[1:])

    data_89 = []
    for line in extracted_lines_89:
        parts = line.split()
        if len(parts) == 7:  # We expect 7 parts, the first being the identifier and the rest being the values
            data_89.append(parts[1:])

    # Create DataFrames with the extracted data
    df_87 = pd.DataFrame(data_87, columns=['COOR1', 'COOR2', 'COOR3', 'U1', 'U2', 'U3'])
    df_89 = pd.DataFrame(data_89, columns=['COOR1', 'COOR2', 'COOR3', 'U1', 'U2', 'U3'])

    # Convert columns to float
    df_87 = df_87.astype(float)
    df_89 = df_89.astype(float)

    return df_87, df_89

def main():
    st.title("DAT File Processor")
    
    uploaded_file = st.file_uploader("Choose a .dat file", type="dat")
    
    if uploaded_file is not None:
        df_87, df_89 = process_file(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Read Info Node 87")
            st.dataframe(df_87)
        
        with col2:
            st.subheader("Read Info Node 89")
            st.dataframe(df_89)
        
        # Extract required values from dataframes
        N87_X0 = df_87['COOR1'].iloc[0]
        N87_Y0 = df_87['COOR2'].iloc[0]
        N87_Z0 = df_87['COOR3'].iloc[0]
        N89_X0 = df_89['COOR1'].iloc[0]
        N89_Y0 = df_89['COOR2'].iloc[0]
        N89_Z0 = df_89['COOR3'].iloc[0]
        
        # displacement 87 and 89 von Seitenkraft    
        a = df_87['U1'].iloc[0]
        b = df_87['U2'].iloc[0]
        c = df_87['U3'].iloc[0]
        d = df_89['U1'].iloc[0]
        e = df_89['U2'].iloc[0]
        f = df_89['U3'].iloc[0]
        
        # displacement 87 and 89 von Laengskraft    
        g = df_87['U1'].iloc[1]
        h = df_87['U2'].iloc[1]
        i = df_87['U3'].iloc[1]
        j = df_89['U1'].iloc[1]
        k = df_89['U2'].iloc[1]
        l = df_89['U3'].iloc[1]
        
        # displacement 87 and 89 von AlignT    
        m = df_87['U1'].iloc[2]
        n = df_87['U2'].iloc[2]
        o = df_87['U3'].iloc[2]
        p = df_89['U1'].iloc[2]
        q = df_89['U2'].iloc[2]
        r = df_89['U3'].iloc[2]

        # Calculate additional variables
        Seitenkraft_Vorspur = np.arcsin(((N87_X0 + a) - (N89_X0 + d)) / 
                                        np.sqrt(((N87_X0 + a) - (N89_X0 + d))**2 + ((N87_Y0 + b) - (N89_Y0 + e))**2)) * 180 / np.pi
        
        Seitenkraft_Sturz = np.arcsin(((N87_Z0 + c) - (N89_Z0 + f)) / 
                                      np.sqrt(((N87_X0 + a) - (N89_X0 + d))**2 + ((N87_Y0 + b) - (N89_Y0 + e))**2)) * 180 / np.pi
        
        Brake_Vorspur = np.arcsin(((N87_X0 + g) - (N89_X0 + j)) / 
                                  np.sqrt(((N87_X0 + g) - (N89_X0 + j))**2 + ((N87_Y0 + h) - (N89_Y0 + k))**2)) * 180 / np.pi
        
        Brake_Sturz = np.arcsin(((N87_Z0 + i) - (N89_Z0 + l)) / 
                                np.sqrt(((N87_X0 + g) - (N89_X0 + j))**2 + ((N87_Y0 + h) - (N89_Y0 + k))**2)) * 180 / np.pi
        
        AT_Vorspur = np.arcsin(((N87_X0 + m) - (N89_X0 + p)) / 
                               np.sqrt(((N87_X0 + m) - (N89_X0 + p))**2 + ((N87_Y0 + n) - (N89_Y0 + q))**2)) * 180 / np.pi
        
        AT_Sturz = np.arcsin(((N87_Z0 + o) - (N89_Z0 + r)) / 
                             np.sqrt(((N87_X0 + m) - (N89_X0 + p))**2 + ((N87_Y0 + n) - (N89_Y0 + q))**2)) * 180 / np.pi
        
        Orig_Vorspur = np.arcsin((N87_X0 - N89_X0) / 
                                 np.sqrt((N87_X0 - N89_X0)**2 + (N87_Y0 - N89_Y0)**2)) * 180 / np.pi
        
        Orig_Sturz = np.arcsin((N87_Z0 - N89_Z0) / 
                               np.sqrt((N87_X0 - N89_X0)**2 + (N87_Y0 - N89_Y0)**2)) * 180 / np.pi
        
        kraft = st.number_input('Enter the force (N)', min_value=0.0, value=1000.0, step=1.0)
        moment = st.number_input('Enter the Moment for AT (Nm)', min_value=0.0, value=100.0, step=1.0)

        results = {
            'Variable': ['Seitenkkraft_ToeChange', 'Seitenkkraft_CamberChange', 'Seitenkkraft_@WC@Compliance',
                         'Braking_ToeChange', 'Braking_CamberChange', 'Brake_@WC@Compliance',
                         'AT_ToeChange', 'AT_CamberChange'],
            'Value': [
                (Seitenkraft_Vorspur - Orig_Vorspur) / kraft,
                (Seitenkraft_Sturz - Orig_Sturz) / kraft,
                b / kraft,
                (Brake_Vorspur - Orig_Vorspur) / kraft,
                (Brake_Sturz - Orig_Sturz) / kraft,
                g / kraft,
                (AT_Vorspur - Orig_Vorspur) / moment,
                (AT_Sturz - Orig_Sturz) / moment
            ]
        }

        results_df = pd.DataFrame(results)
        
        st.subheader("Results")
        st.dataframe(results_df.style.format({"Value": "{:.2e}"}))

if __name__ == '__main__':
    main()
