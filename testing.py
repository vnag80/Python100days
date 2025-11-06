import sys
import pandas as pd
import numpy as np
def main():
    # Check if exactly one argument is provided (excluding script name)
    if len(sys.argv) != 2:
        print("Usage: python script.py <your_string>")
        sys.exit(1)

    input_str = sys.argv[1]

    # Optional: Check type
    if not isinstance(input_str, str):
        raise TypeError("Argument must be a string")

    print(f"You entered: {input_str}")
    URL=URL = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    tables = pd.read_html(URL,header=0)          # returns a list of DataFrames
    df = tables[0].copy()               # first table has the data
    df.sort_values(by=['x-coordinate', 'y-coordinate'], ascending=[True, True], inplace=True)
    print(df)
    x_max = df['x-coordinate'].max()
    y_max = df['y-coordinate'].max()
    print()
    print(x_max,y_max)
   # for index, row in df.iterrows():
   #     print(row['Character'])
    matrix = np.full((x_max+1,y_max+1)," ",dtype=str)
    for index, row in df.iterrows():
        matrix[row['x-coordinate']] [row['y-coordinate']] = row['Character']
    for row in matrix:
        print("".join(row))    
    
if __name__ == "__main__":
    main()