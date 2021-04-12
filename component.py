import dash_bootstrap_components as dbc
import dash_core_components as dcc
from style import *
import dash_html_components as html
from style import TEXT_STYLE
from dataframehandler import get_dict_for_drop_down, get_all_zone

"""html component for the graph course one two three means table for course one..two.."""

def get_tables_for_course_one(student_df: list, last_month:list, last_week:list, today:list, sub_name=['qa', 'qb','qc','qd','qe']):
    ## table 1
    table_header = [
        html.Thead(html.Tr([html.Th("{}".format("course 1"), colSpan=2), html.Th("Score", colSpan=2)])),
        html.Thead(html.Tr(
            [html.Th("milestone"), html.Th("target"), html.Th("last month"), html.Th("last week"), html.Th("today")]))
    ]
    ### table data for 1 courses

    row1 = html.Tr([html.Td("{}".format(sub_name[0])), html.Td("{}".format(student_df[0])),html.Td("{}".format(last_month[0])),html.Td("{}".format(last_week[0])), html.Td("{}".format(today[0]))])
    row2 =  html.Tr([html.Td("{}".format(sub_name[1])), html.Td("{}".format(student_df[1])),html.Td("{}".format(last_month[1])),html.Td("{}".format(last_week[1])), html.Td("{}".format(today[1]))])
    row3 =  html.Tr([html.Td("{}".format(sub_name[2])), html.Td("{}".format(student_df[2])),html.Td("{}".format(last_month[2])),html.Td("{}".format(last_week[2])), html.Td("{}".format(today[2]))])
    row4 = html.Tr([html.Td("{}".format(sub_name[3])), html.Td("{}".format(student_df[3])), html.Td("{}".format(last_month[3])),html.Td("{}".format(last_week[3])), html.Td("{}".format(today[3]))])
    row5 = html.Tr([html.Td("{}".format(sub_name[4])), html.Td("{}".format(student_df[4])), html.Td("{}".format(last_month[4])),html.Td("{}".format(last_week[4])), html.Td("{}".format(today[4]))])
    table_body = [html.Tbody([row1, row2, row3, row4, row5])]
    table_course = dbc.Table(table_header + table_body, bordered=True, id="course1", style=TEXT_STYLE)

    return table_course


def get_tables_for_course_two(student_df: list, last_month: list, last_week: list, today:list, sub_name:list =['pa','pb','pc', 'pd','pe','pf']):
    ## table 1
    table_header = [
        html.Thead(html.Tr([html.Th("{}".format("course 2"), colSpan=2), html.Th("Score", colSpan=2)])),
        html.Thead(html.Tr(
            [html.Th("milestone"), html.Th("target"), html.Th("last month"), html.Th("last week"), html.Th("today")]))
    ]
    ### table data for 1 courses
    row1 = html.Tr([html.Td("{}".format(sub_name[0])),html.Td("{}".format(student_df[0])),html.Td("{}".format(last_month[0])), html.Td("{}".format(last_week[0])),html.Td("{}".format(today[0]))])
    row2 = html.Tr(
        [html.Td("{}".format(sub_name[1])), html.Td("{}".format(student_df[1])), html.Td("{}".format(last_month[1])),
         html.Td("{}".format(last_week[1])), html.Td("{}".format(today[1]))])
    row3 = html.Tr(
        [html.Td("{}".format(sub_name[2])), html.Td("{}".format(student_df[2])), html.Td("{}".format(last_month[2])),
         html.Td("{}".format(last_week[2])), html.Td("{}".format(today[2]))])
    row4 = html.Tr(
        [html.Td("{}".format(sub_name[3])), html.Td("{}".format(student_df[3])), html.Td("{}".format(last_month[3])),
         html.Td("{}".format(last_week[3])), html.Td("{}".format(today[3]))])
    row5 = html.Tr(
        [html.Td("{}".format(sub_name[4])), html.Td("{}".format(student_df[4])), html.Td("{}".format(last_month[4])),
         html.Td("{}".format(last_week[4])), html.Td("{}".format(today[4]))])
    row6 = html.Tr(
        [html.Td("{}".format(sub_name[5])), html.Td("{}".format(student_df[5])), html.Td("{}".format(last_month[5])),
         html.Td("{}".format(last_week[5])), html.Td("{}".format(today[5]))])


    table_body = [html.Tbody([row1, row2, row3, row4, row5, row6])]
    table_course = dbc.Table(table_header + table_body, bordered=True, id="course2", style=TEXT_STYLE)

    return table_course

def get_tables_for_course_three(student_df: list, last_month:list, last_week: list, today:list, sub_name=['aa','ab','ac','ad']):
    table_header = [
        html.Thead(html.Tr([html.Th("{}".format("course 3"), colSpan=2), html.Th("Score", colSpan=2)])),
        html.Thead(html.Tr(
            [html.Th("milestone"), html.Th("target"), html.Th("last month"), html.Th("last week"), html.Th("today")]))
    ]
    ### table data for 3 courses
    row1 = html.Tr([html.Td(str(sub_name[0])), html.Td("{}".format(student_df[0])), html.Td("{}".format(last_month[0])),html.Td("{}".format(last_week[0])),html.Td("{}".format(today[0]))])
    row2 = html.Tr([html.Td(str(sub_name[1])), html.Td("{}".format(student_df[1])), html.Td("{}".format(last_month[1])),html.Td("{}".format(last_week[1])),html.Td("{}".format(today[0]))])
    row3 = html.Tr([html.Td(str(sub_name[2])), html.Td("{}".format(student_df[2])), html.Td("{}".format(last_month[2])),html.Td("{}".format(last_week[2])),html.Td("{}".format(today[0]))])
    row4 = html.Tr([html.Td(str(sub_name[3])), html.Td("{}".format(student_df[3])), html.Td("{}".format(last_month[3])),html.Td("{}".format(last_week[3])),html.Td("{}".format(today[0]))])
    table_body = [html.Tbody([row1, row2, row3, row4])]
    table_course = dbc.Table(table_header + table_body, bordered=True, id="course3", style=TEXT_STYLE)

    return table_course

# table for pratical course
def get_tables_for_course_practical(student_score:int, last_month:int, last_week:int, today:int, sub_name=['pra']):
    table_header = [
        html.Thead(html.Tr([html.Th("{}".format("course 1"), colSpan=2), html.Th("Score", colSpan=2)])),
        html.Thead(html.Tr(
            [html.Th("milestone"), html.Th("target"), html.Th("last month"), html.Th("last week"), html.Th("today")]))
    ]
    ### table data for 3 courses
    print(student_score, last_week,last_month, today)
    row1 = html.Tr([html.Td("{}".format(sub_name[0])), html.Td("{}".format(student_score)),html.Td("{}".format(last_month)),html.Td("{}".format(last_week)), html.Td("{}".format(today))])
    table_body = [html.Tbody([row1])]
    table_course = dbc.Table(table_header + table_body, bordered=True, id="course4", style=TEXT_STYLE)

    return table_course

## global score table
def get_tables_global_score(global_score:int, feedback:str = ""):
    table_header = [
        html.Thead(html.Tr([html.Th("{}".format("global score"), colSpan=2), html.Th("feedback", colSpan=3)]))
    ]
    ### table data for 3 courses
    row1 = html.Tr([ html.Td(global_score, colSpan=2), html.Td("{}".format(feedback), colSpan=6)])
    table_body = [html.Tbody([row1])]
    table_course = dbc.Table(table_header + table_body, bordered=True, id="course4")
    return table_course

content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=3
    )
])

timeline = dbc.Row([
    dbc.Col([dbc.Card([dbc.RadioItems(
            id='timeline',
            options=[{
                'label': 'today',
                'value': 'd'
            },
                {
                    'label': 'week',
                    'value': 'w'
                },
                {
                    'label': 'month',
                    'value': 'm'
                },
                {
                    'label': 'clear',
                    'value': 'x'
                }
            ],
            style={
                'margin': 'auto'
            },
            labelStyle={'display': 'inline-block'}
        )])],md=3, align=""),
])

controls = dbc.FormGroup(
    [
        dcc.Dropdown(
            id='region',
            options=get_dict_for_drop_down(get_all_zone()),
            placeholder="select Region",
            value='EMEA'
        ),
        html.Br(),
        dbc.Card([dcc.RadioItems(
            id='radio_items',
            options=[{
                'label': 'Country',
                'value': 'c'
            },
                {
                    'label': 'Language',
                    'value': 'l'
                },
            ],
            labelStyle={'display': 'inline-block', 'margin':'10px 10px 10px 10px'},
        )]),
        html.Br(),
        dcc.Dropdown(
            id='language',
            placeholder=" select language"
        ),
        html.Br(),
        dcc.Dropdown(
            id='country',
            placeholder="select country"
        ),
        html.Br(),
        timeline,
        html.Br()
    ]
)
