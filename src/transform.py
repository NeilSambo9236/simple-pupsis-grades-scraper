import pandas as pd

def to_table(headers, grades_in_list) :
    df = pd.DataFrame(grades_in_list, columns=headers)

    return df