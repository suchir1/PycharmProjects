import pandas as pd
import ast

def clean(str_list):
    cleaned_str = []
    for str in str_list:
        str = str.replace('\n','')
        if str[len(str)-2:] == "’s" or str[len(str)-2:] == "'s":
            str = str[0:len(str)-2]
        if(len(str)>0 and (str[-1]=="'" or str[-1]=="’")):
            str = str[0:len(str)-1]
        if(str.find(' ')!=-1):
            str = str.title()
        cleaned_str.append(str)
    return cleaned_str

def read_locations(filename):
    results = pd.read_csv(filename)
    hopeful = pd.DataFrame.as_matrix(results)
    locations = hopeful[:, 5]
    all = []
    for ls in locations:
        if ls != '[]':
            ls1 = ast.literal_eval(ls)
            for loc in ls1:
                all.append(loc)
    return all

def delete_already_coded(excel_filename, locations):
    locations = clean(locations)
    existing = pd.read_excel(excel_filename)
    existing = pd.DataFrame.as_matrix(existing)
    existing = existing[1:,1]
    unencoded = []
    for loc in locations:
        if loc not in existing:
            unencoded.append(loc)
    print(unencoded)


best = read_locations("/home/cheesecake/PycharmProjects/LUCAS/Smart_Search_Ruobing/test2.csv")
delete_already_coded("/home/cheesecake/Desktop/CAMOE_region.xlsx", best)

ls = ['North Korea', 'US', 'South Korea', 'U.S.', 'South Korea', 'North Korea', 'NOrTh KoREA']