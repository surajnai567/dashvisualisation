import pandas as pd

"""module for interecting with data with pandas"""


file_location = "descriptionDATA.xlsx"
f = pd.ExcelFile(file_location)

mdf = pd.read_excel(f, sheet_name=1, index_col=0,header=1)
df1 = pd.read_excel(f, sheet_name='std. trn 27',index_col=0 ,header=1)
df2 = pd.read_excel(f, sheet_name='std. trn 28',index_col=0, header=1)
fields_of_interest = ["date", "name", "Region", "lang", "Country"]

# return df with full data
def get_df(all=False):
    if all:
        return pd.concat([mdf, df1, df2], ignore_index=True)
    return pd.concat([mdf, df1, df2])

# returns avalibale zones in data
def get_all_zone(df = get_df()):
    return df['Region'].dropna().unique()


#  return all language
def get_all_lang(zone, df=get_df()):
    filters = df['Region'] == zone
    return df['lang'].where(filters).dropna().unique()

# retun all country
def get_all_country(zone, df=get_df()):
    filters = df['Region'] == zone
    return df['Country'].where(filters).dropna().unique()

# utils func to retun dictionary for drop down
def get_dict_for_drop_down(list):
    values = []
    for val in list:
        a = {"value": val, "label": val}
        values.append(a)
    return values

# return all the student based on zone country and language
def get_all_student_name(zone, country=None, language= None):
    df = get_df()
    df = df.loc[df['Region'] == zone]
    if country is not None:
        df = df.loc[(df['Country'] == country) & (df['Region'] == zone)]
    if language is not None:
        df = df.loc[(df['lang'] == language) & (df['Region'] == zone)]
    return df['name'], df

# return student by name
def get_student_by_name(name):
    df = get_df()
    return mdf.loc[(df['name'] == name)]

# class with functions to get required data from df
class StudentDF:
    def __init__(self, mdf):
        self.df = mdf

    def __str__(self):
        return "student obj"

    def get_third_score(self):
        filters = ["aa", "ab", "ac", "ad"]
        return self.df[filters]

    def get_calculation_of_score_df(self):
        filters = ["metric4", "metric5", "metric3", "metric1", "metric2"]
        return self.df[filters]

    def get_first_score(self):
        filters = ["qa", "qb", "qc", "qd", "qe"]
        return self.df[filters]

    def get_second_score(self):
        filters = ["pa", "pb", "pc", "pd", "pf", "pg"]
        return self.df[filters]

    def get_global(self):
        return self.df['Global']

    def get_pratical_score(self):
        return self.df['top score']

    def get_names(self):
        return self.df['name']

    def get_dates(self):
        return self.df['date']

    def get_family(self):
        return self.df['family']

    def get_lang(self):
        return self.df['lang']

    def get_region(self):
        return self.df['Region']

    def get_country(self):
        return self.df['Country']

    def get_teacher(self):
        return self.df['teacher']


def get_teacher_by_student_name(zone, country=None, language=None):
    df = get_df()
    if country:
        df = df.loc[(df['Country'] == country) & (df['Region'] == zone)]
        print(df)
        return df['teacher'].unique()
    if language:
        df = df.loc[(df['Region'] == zone) & (df['lang'] == language)]
        return df['teacher'].unique()
    return {}

# return student records based on name zone country and language
def get_student_record(name, zone=None, country=None, language=None, teacher=None):
    df = get_df()
    print(name, zone, country, language, teacher)
    if (zone and language) or (zone and country):
        if language:
            res =  df.loc[(df['Region'] == zone)
                  & (df['name'] == name)  & (df['lang'] == language)]
            stu = StudentDF(res)
            return stu
        if country:
            res = df.loc[(df['Region'] == zone)
                         & (df['name'] == name) & (df['Country'] == country)]
            stu = StudentDF(res)
            return stu
    return []

# return teacher records based on name zone country
def get_teacher_record(t_name, zone=None, country=None, language=None):
    df = get_df()
    if (zone and language) or (zone and country):
        if language:
            res =  df.loc[(df['Region'] == zone)
                  & (df['teacher'] == t_name)  & (df['lang'] == language)]
            stu = StudentDF(res)
            return stu
        if country:
            res = df.loc[(df['Region'] == zone)
                         & (df['teacher'] == t_name) & (df['Country'] == country)]
            stu = StudentDF(res)
            return stu
    return []

# return student record for chart
def get_student_record_for_chat(name, zone=None, country=None, language=None, teacher=None):
    df = get_df()

    if (zone and language) or (zone and country):
        if language:
            res = df.loc[(df['Region'] == zone)
                  & (df['name'] == name)  & (df['lang'] == language)]
            return res
        if country:
            res = df.loc[(df['Region'] == zone)
                         & (df['name'] == name) & (df['Country'] == country)]
            return res
    return []


def get_teacher_record_chart(t_name, zone=None, country=None, language=None):
    df = get_df()
    if (zone and language) or (zone and country):
        if language:
            res =  df.loc[(df['Region'] == zone)
                  & (df['teacher'] == t_name)  & (df['lang'] == language)]

            return res
        if country:
            res = df.loc[(df['Region'] == zone)
                         & (df['teacher'] == t_name) & (df['Country'] == country)]

            return res
    return []

# function to get data based on zone


def get_data_by_zone(zone, df=get_df()):
    return StudentDF(df[df['Region'] == zone])