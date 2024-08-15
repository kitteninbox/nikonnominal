import pandas as pd
import numpy as np
import streamlit as st
import base64
import math

css = """
<style>
[data-testid="stToolbar"] {
    visibility: hidden;
}
</style>
"""

st.markdown(
    css,
    unsafe_allow_html=True
)

# Create a function that faciitate file download
def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'



# Create a function to process the data
def main():

    st.title('Nikon Nominal Values Calculation App')
    st.title('Created by Yue Hang')

    ## Input die-to-die Row (Y) and Col (X) pitches
    # For ZPS268
    col_x_pitch = st.number_input('Enter Column (X) Pitch', value=2660)
    row_y_pitch = st.number_input('Enter Row (Y) Pitch', value=2660)
    
    ## Measured X and Y distance from subpanel center in AutoCAD to the PACKAGE center (+ve and -ve signs are needed!)
    # For ZPS268
    package_col_x = st.number_input('Distance of Subpanel Center to First Package (X)', value=-140980)
    package_row_y = st.number_input('Distance of Subpanel Center to First Package (Y)', value=140980)
    
    ## Die offset in the center of the package (+ve and -ve signs are needed!)
    # For ZPS268
    die_col_x = st.number_input('Die Position Offset Within the Package (X)', value=-15.3)
    die_row_y = st.number_input('Die Position Offset Within the Package (Y)', value=-180.6)
    
    ## FINAL X and Y
    first_row_y = package_row_y + die_row_y
    first_col_x = package_col_x + die_col_x

    csv_file = st.file_uploader("Upload the Control Map (Bond Map) from Chen Kang, in CSV format", type=['csv'])

    if csv_file is not None:
        df = pd.read_csv(csv_file, header=None)


        # To check if the last columns contains NaN float value
        # If yes, drop it
        nan_count = 0

        for item in df.iloc[:, -1].to_list():
            if math.isnan(item):
                nan_count += 1

        if nan_count > 0:
            df.drop(df.columns[-1], axis=1, inplace=True)

        # # THIS LINE IS OPTIONAL. DEPENDS ON THE OUTPUT FROM read_csv()
        # df.drop(146, axis=1, inplace=True)


        # Remap the columns and index numbers
        df.columns = np.arange(1, len(df.columns)+1).tolist()
        df.index = np.arange(1, len(df.index)+1).tolist()


        # Define the rows and cols for each quadrant
        q0_rows = df.index[:int(len(df.index)/2)]
        q0_cols = df.columns[:int(len(df.columns)/2)]

        q1_rows = df.index[:int(len(df.index)/2)]
        q1_cols = df.columns[int(len(df.columns)/2):]


        q2_rows = df.index[int(len(df.index)/2):]
        q2_cols = df.columns[:int(len(df.columns)/2)]


        q3_rows = df.index[int(len(df.index)/2):]
        q3_cols = df.columns[int(len(df.columns)/2):]



        q0_row_with_die = []
        q0_col_with_die = []
        q0_die_type = []
        q0 = []

        q1_row_with_die = []
        q1_col_with_die = []
        q1_die_type = []
        q1 = []

        q2_row_with_die = []
        q2_col_with_die = []
        q2_die_type = []
        q2 = []

        q3_row_with_die = []
        q3_col_with_die = []
        q3_die_type = []
        q3 = []

        row_y_nominal = []
        col_x_nominal = []

        # Quadrant 0
        for item in q0_rows:
            for unit in q0_cols:
                q0_row_with_die.append(item)
                q0_col_with_die.append(unit)
                q0.append("Subpanel 1")
                if df.loc[item, unit] == 1:
                    q0_die_type.append(1)
                elif df.loc[item, unit] == 0:
                    q0_die_type.append(0)
                elif df.loc[item, unit] == 2:
                    q0_die_type.append(2)
                elif df.loc[item, unit] == 3:
                    q0_die_type.append(3)
                elif df.loc[item, unit] == 4:
                    q0_die_type.append(4)
                elif df.loc[item, unit] == 5:
                    q0_die_type.append(5)
                elif df.loc[item, unit] == 6:
                    q0_die_type.append(6)
                elif df.loc[item, unit] == 7:
                    q0_die_type.append(7)
                elif df.loc[item, unit] == 8:
                    q0_die_type.append(8)
                elif df.loc[item, unit] == 9:
                    q0_die_type.append(9)
                    

        # Quadrant 1
        for item in q1_rows:
            for unit in q1_cols:
                q1_row_with_die.append(item)
                q1_col_with_die.append(unit)
                q1.append("Subpanel 2")
                if df.loc[item, unit] == 1:
                    q1_die_type.append(1)
                elif df.loc[item, unit] == 0:
                    q1_die_type.append(0)
                elif df.loc[item, unit] == 2:
                    q1_die_type.append(2)
                elif df.loc[item, unit] == 3:
                    q1_die_type.append(3)
                elif df.loc[item, unit] == 4:
                    q1_die_type.append(4)
                elif df.loc[item, unit] == 5:
                    q1_die_type.append(5)
                elif df.loc[item, unit] == 6:
                    q1_die_type.append(6)
                elif df.loc[item, unit] == 7:
                    q1_die_type.append(7)
                elif df.loc[item, unit] == 8:
                    q1_die_type.append(8)
                elif df.loc[item, unit] == 9:
                    q1_die_type.append(9)

        # Quadrant 2
        for item in q2_rows:
            for unit in q2_cols:
                q2_row_with_die.append(item)
                q2_col_with_die.append(unit)
                q2.append("Subpanel 3")
                if df.loc[item, unit] == 1:
                    q2_die_type.append(1)
                elif df.loc[item, unit] == 0:
                    q2_die_type.append(0)
                elif df.loc[item, unit] == 2:
                    q2_die_type.append(2)
                elif df.loc[item, unit] == 3:
                    q2_die_type.append(3)
                elif df.loc[item, unit] == 4:
                    q2_die_type.append(4)
                elif df.loc[item, unit] == 5:
                    q2_die_type.append(5)
                elif df.loc[item, unit] == 6:
                    q2_die_type.append(6)
                elif df.loc[item, unit] == 7:
                    q2_die_type.append(7)
                elif df.loc[item, unit] == 8:
                    q2_die_type.append(8)
                elif df.loc[item, unit] == 9:
                    q2_die_type.append(9)

        # Quadrant 3
        for item in q3_rows:
            for unit in q3_cols:
                q3_row_with_die.append(item)
                q3_col_with_die.append(unit)
                q3.append("Subpanel 4")
                if df.loc[item, unit] == 1:
                    q3_die_type.append(1)
                elif df.loc[item, unit] == 0:
                    q3_die_type.append(0)
                elif df.loc[item, unit] == 2:
                    q3_die_type.append(2)
                elif df.loc[item, unit] == 3:
                    q3_die_type.append(3)
                elif df.loc[item, unit] == 4:
                    q3_die_type.append(4)
                elif df.loc[item, unit] == 5:
                    q3_die_type.append(5)
                elif df.loc[item, unit] == 6:
                    q3_die_type.append(6)
                elif df.loc[item, unit] == 7:
                    q3_die_type.append(7)
                elif df.loc[item, unit] == 8:
                    q3_die_type.append(8)
                elif df.loc[item, unit] == 9:
                    q3_die_type.append(9)

        # X and Y nominal values
        for item in q0_rows:
            for unit in q0_cols:
                row_y_nom = first_row_y - (item-1)*row_y_pitch
                col_x_nom = first_col_x + (unit-1)*col_x_pitch
                row_y_nominal.append(row_y_nom)
                col_x_nominal.append(col_x_nom)

        final_row_list = q0_row_with_die + q0_row_with_die + q0_row_with_die + q0_row_with_die
        final_col_list = q0_col_with_die + q0_col_with_die + q0_col_with_die + q0_col_with_die
        final_subpanel_list = q0 + q1 + q2 + q3
        final_die_type_list = q0_die_type + q1_die_type + q2_die_type + q3_die_type
        final_row_y_nominal = row_y_nominal + row_y_nominal + row_y_nominal + row_y_nominal
        final_col_x_nominal = col_x_nominal + col_x_nominal + col_x_nominal + col_x_nominal

        df_output = pd.DataFrame({
            "ZONE": final_subpanel_list,
            "ROW": final_row_list,
            "COLUM": final_col_list,
            "Col X Nominal": final_col_x_nominal,
            "Row Y Nominal": final_row_y_nominal,
            "Die Type": final_die_type_list
        })


        if st.button('Download Data as CSV'):
            tmp_download_link = download_link(df_output, 'Calculated_Nikon_Nominal.csv', 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
