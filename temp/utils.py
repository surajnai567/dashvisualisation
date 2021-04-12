import dash_html_components as html
from datetime import datetime, timedelta
from dataframehandler import StudentDF

# get one day old data
def get_today(datetime1):
    if datetime.now() - datetime1 < timedelta(days=0):
        return True
    return False

# return df 7 day old data
def get_week(datetime1):
    if datetime.now() - datetime1 < timedelta(days=7):
        return True
    return False

# month old data
def get_month(datetime1):
    if datetime.now() - datetime1 < timedelta(days=30):
        return True
    return False

# function to filter data based on some filters
def get_data_from_df_filter(df, filter_fun):
    return df[df['date'].apply(lambda x: filter_fun(x.to_pydatetime()))]

# returns df based on option like day week month etc
def get_filter_data(df, option):
    data = []
    if option== "d":
        return df[df['date'].apply(lambda x: get_today(x.to_pydatetime()))]
    if option == "w":
        return df[df['date'].apply(lambda x: get_week(x.to_pydatetime()))]

    if option == 'm':
        return df[df['date'].apply(lambda x: get_month(x.to_pydatetime()))]

# function which calcute score for course 3 and return a pandas list
def get_score_for_third_course(df):
    data = get_filter_data(df, 'm')
    st = StudentDF(data)
    lis = []
    try:

        aa = st.get_third_score()['aa'].value_counts().get(key='Yes', default=0)
        ab = st.get_third_score()['ab'].value_counts().get(key='Yes', default=0)
        ac = st.get_third_score()['ac'].value_counts().get(key='Yes', default=0)
        ad = st.get_third_score()['ad'].value_counts().get(key='Yes', default=0)
        lis.append([aa,ab,ac,ad])
    except:
         lis.append([0, 0, 0, 0])

    data = get_filter_data(df, 'w')
    st = StudentDF(data).get_third_score()

    try:
        aa = st.get_third_score()['aa'].value_counts().get(key='Yes', default=0)
        ab = st.get_third_score()['ab'].value_counts().get(key='Yes', default=0)
        ac = st.get_third_score()['ac'].value_counts().get(key='Yes', default=0)
        ad = st.get_third_score()['ad'].value_counts().get(key='Yes', default=0)
        lis.append([aa, ab, ac, ad])
    except:
        lis.append([0, 0, 0, 0])

    data = get_filter_data(df, 'd')
    st = StudentDF(data).get_third_score()

    try:
        aa = st.get_third_score()['aa'].value_counts().get(key='Yes', default=0)
        ab = st.get_third_score()['ab'].value_counts().get(key='Yes', default=0)
        ac = st.get_third_score()['ac'].value_counts().get(key='Yes', default=0)
        ad = st.get_third_score()['ad'].value_counts().get(key='Yes', default=0)
        lis.append([aa, ab, ac, ad])
    except:
        lis.append([0, 0, 0, 0])

    return lis