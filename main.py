"""for any query contact surajnai567@gmail.com"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


#user define
from dataframehandler import get_all_zone, get_all_lang, \
    get_all_country, get_dict_for_drop_down, \
    get_all_student_name,get_teacher_by_student_name,\
    get_student_record,StudentDF, get_teacher_record,\
    get_student_record_for_chat,get_teacher_record_chart, get_data_by_zone

from component import get_tables_for_course_one, \
    get_tables_for_course_two, get_tables_for_course_three, \
    get_tables_for_course_practical, timeline, get_tables_global_score, controls

from style import *
from plotlygraph import graph_1_g, graph_2_g, graph_3_g

from utils import get_filter_data, get_score_for_third_course
from extra import get_global_score, calculate_score

zone = ''
language = None
country = None
timel = None

# side bar
sidebar = html.Div(
    [
        html.H5('Parameters', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)


couser_detail = dbc.Row(id='course_record_div', style=CONTEXT_GRAPH)
couser_detail_teacher = dbc.Row(id='course_record_teacher', style=CONTEXT_GRAPH)
content_graph = dbc.Row(id='timeline_g', style=CONTEXT_GRAPH)
content_zone = dbc.Row(id='timeline_zone', style=CONTEXT_GRAPH)
student_teacher_selector = dbc.Row([dcc.Dropdown
                                    (id='student',placeholder="select student", style=CONTENT_STUDENT_TEACHER),
                                    dcc.Dropdown(id='teacher', placeholder="select teacher", style=CONTENT_STUDENT_TEACHER)])
# main div for content
content = html.Div(
    [
        html.H4('....Dashboard....', style=TEXT_STYLE),
        html.Hr(),
        student_teacher_selector,
        couser_detail,
        couser_detail_teacher,
        content_graph,
        content_zone,
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, 'style.css'])
app.layout = html.Div([sidebar, content])

# callbacks


# zone wise data

@app.callback(
    Output(component_id='timeline_zone', component_property='children'),
    [Input(component_id='language', component_property='value'),
              Input(component_id='country', component_property='value'),
               Input(component_id='region', component_property='value'),
               #Input(component_id='radio_items', component_property='value'),
               ]
)
def update_zone(value, value2, v3):
    try:
        if  value is None and value2 is None:
            details = get_data_by_zone(v3)
            row1 = dbc.Row(dbc.Col([dcc.Graph(figure=graph_1_g(details, details.get_first_score().columns))
                                   , dcc.Graph(figure=graph_2_g(details, details.get_second_score().columns))]))
            row2 = dbc.Row(dbc.Col([dcc.Graph(figure=graph_3_g(details))]))
        # , dcc.Graph(figure=course_4_g)
            return [row1, row2]
        else:
            return []
    except Exception as e:
        return []

####################dropdown language update
@app.callback(
    Output(component_id='language', component_property='options'),
    [Input(component_id='region', component_property='value')]
)
def update_language(value):
    try:
        return get_dict_for_drop_down(get_all_lang(value))
    except Exception as e:
        return {}

@app.callback(
    Output(component_id='country', component_property='options'),
    [Input(component_id='region', component_property='value')]
)
def update_language(value):
    try:
        return get_dict_for_drop_down(get_all_country(value))
    except Exception as e:
        return {}
############################################
# radio items
@app.callback(
    [Output(component_id='country', component_property='disabled'),
    Output(component_id='language', component_property='value')],
    [Input(component_id='radio_items', component_property='value')]
)
def update_country(value):
    if value == "c":
        return [False,None]
    return [True, None]

@app.callback(
    [Output(component_id='language', component_property='disabled'),
    Output(component_id='country', component_property='value')],
    [Input(component_id='radio_items', component_property='value')]
)
def update_language(value):
    if value == "l":
        return [False, None]
    return [True, None]
###############################

##update teacher
@app.callback(Output(component_id='teacher', component_property='options'),
              [
               Input(component_id='region', component_property='value'),
               Input(component_id='country', component_property='value'),
               Input(component_id='language', component_property='value'),
               ])
def update_faculty(value2, value3, value4):
    try:
        return get_dict_for_drop_down\
            (get_teacher_by_student_name(value2, language = value4, country=value3))

    except Exception as e:
        return {}

## submit actions
@app.callback(Output(component_id='student', component_property='options'),
              Input(component_id='language', component_property='value'),
              Input(component_id='region', component_property='value' ),
              Input(component_id='country', component_property='value'),)

def update_student(value1, value2, value3):
    try:

        df = get_all_student_name(value2, language=value1, country = value3)
        # plot graph
        student_name_df = df[0].unique()
        return get_dict_for_drop_down(student_name_df)

    except Exception as e:
        print(e)
        return {}


## chart updations student
@app.callback([Output(component_id="course_record_div", component_property='children')],
              [Input(component_id='language', component_property='value'),
              Input(component_id='region', component_property='value'),
              Input(component_id='country', component_property='value'),
               Input(component_id='student', component_property='value'),
               #Input(component_id='teacher', component_property='value'),
               ])
def update(v1, v2, v3, v4):
    try:
        if v4:
            res = get_student_record_for_chat(name=v4, language=v1, country=v3, zone=v2)
            today = get_filter_data(res, 'd')
            week = get_filter_data(res, 'w')
            month = get_filter_data(res, 'm')
            df = StudentDF(res)
            #first
            t = StudentDF(today).get_first_score().mean().round(2).tolist()
            m = StudentDF(month).get_first_score().mean().round(2).tolist()
            w = StudentDF(week).get_first_score().mean().round(2).tolist()
            c1 = get_tables_for_course_one(["10","10","10","10","10"], m, w, t)
            # second
            t = StudentDF(today).get_second_score().mean().round(2).tolist()
            m = StudentDF(month).get_second_score().mean().round(2).tolist()
            w = StudentDF(week).get_second_score().mean().round(2).tolist()
            c2 = get_tables_for_course_two(["10","10","10","10", "10","10"], m, w, t)

            data = get_score_for_third_course(res)

            c3 = get_tables_for_course_three(["", "", "", ""], data[0], data[1] ,data[2])
            t = StudentDF(today).get_pratical_score().mean()
            m = StudentDF(month).get_pratical_score().mean()
            w = StudentDF(week).get_pratical_score().mean()
            c4 = get_tables_for_course_practical(10, m, w, t)
            data1 = dbc.Row([dbc.Col([c1]), dbc.Col([c2])])
            data2 = dbc.Row([dbc.Col([c3]), dbc.Col([c4])])
            ## put value for courses for global score
            score, feedback = get_global_score(1, 2, 3, 4, 5)
            data3 = dbc.Row([get_tables_global_score(score, feedback)])
            return [[data1, data2, data3]]
    except Exception as e:
        print(e)
        return [[]]
    return [[]]


## chart updations teacher
@app.callback([Output(component_id="course_record_teacher", component_property='children')],
              [Input(component_id='language', component_property='value'),
              Input(component_id='region', component_property='value'),
              Input(component_id='country', component_property='value'),
            #Input(component_id='student', component_property='value'),
               Input(component_id='teacher', component_property='value'),
               ])
def update(v1, v2, v3, v4):
    try:
        if v4:
            res = get_teacher_record_chart(t_name=v4, language=v1, country=v3, zone=v2)

            today = get_filter_data(res, 'd')
            week = get_filter_data(res, 'w')
            month = get_filter_data(res, 'm')
            df = StudentDF(res)
            #first
            t = StudentDF(today).get_first_score().mean().round(2).tolist()
            m = StudentDF(month).get_first_score().mean().round(2).tolist()
            w = StudentDF(week).get_first_score().mean().round(2).tolist()
            c1 = get_tables_for_course_one([" "," "," "," ",""], m, w, t)
            # second
            t = StudentDF(today).get_second_score().mean().round(2).tolist()
            m = StudentDF(month).get_second_score().mean().round(2).tolist()
            w = StudentDF(week).get_second_score().mean().round(2).tolist()
            c2 = get_tables_for_course_two([" "," "," "," ", " ",""], m, w, t)
            # third

            data = get_score_for_third_course(res)
            c3 = get_tables_for_course_three(["","","",""],data[0], data[1], data[2])

            # forth
            t = StudentDF(today).get_pratical_score().mean()
            m = StudentDF(month).get_pratical_score().mean()
            w = StudentDF(week).get_pratical_score().mean()
            c4 = get_tables_for_course_practical(1,m,w,t)

            data1 = dbc.Row([dbc.Col([c1]), dbc.Col([c2])])
            data2 = dbc.Row([dbc.Col([c3]), dbc.Col([c4])])
            data3 = dbc.Row([get_tables_global_score(20, "hi i am testing this one and i will let you")])
            return [[data1, data2, data3]]
    except Exception as e:
        print(e)
        return [[]]
    return [[]]



## student graph update
@app.callback(Output(component_id='timeline_g', component_property='children'),
              Input(component_id='language', component_property='value'),
              Input(component_id='region', component_property='value' ),
              Input(component_id='country', component_property='value'),
              Input(component_id='timeline', component_property='value'),

              Input(component_id='country', component_property='disabled'),
              Input(component_id='language', component_property='disabled')
              )
def update_graph(value1, value2, value3, v4, country, lang):
    global timel
    if v4 == 'x':
        return []

    try:
        if (v4 and value3 and value2) or (v4 and value2 and value1):
            if not country:
                all_df = get_all_student_name(value2, value3)[1]
                all_df = get_filter_data(all_df, v4)
                details = StudentDF(all_df)
            if not lang:
                all_df = get_all_student_name(value2, language=value1)[1]
                all_df = get_filter_data(all_df, v4)
                details = StudentDF(all_df)

        #plot graph and send it
            row1 = dbc.Row(dbc.Col([dcc.Graph(figure=graph_1_g(details, details.get_first_score().columns))
                                       , dcc.Graph(figure=graph_2_g(details, details.get_second_score().columns))]))
            row2 = dbc.Row(dbc.Col([dcc.Graph(figure=graph_3_g(details))]))
            # , dcc.Graph(figure=course_4_g)
            return [row1, row2]
    except Exception as e:
        print(e)
    return []


if __name__ == '__main__':
    app.run_server(port='8085')