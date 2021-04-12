import plotly.graph_objs as go
import plotly.express as px

"""
module for plotly graph
graph objects 1 g means for course one 2 means 2nd and so on...
"""
def graph_1_g(df, y: list):
    mean = df.get_first_score().mean().tolist()
    max = df.get_first_score().max().tolist()
    min = df.get_first_score().min().tolist()
    fig = go.Figure(data=[go.Bar(x=y, y=min, name='min'), go.Bar(x=y, y=mean, name='avg'), go.Bar(x=y, y=max, name='max')]
                    ,layout={"title":"Record of Course 1"})
    return fig


def graph_2_g(df, y: list):
    mean = df.get_second_score().mean().tolist()
    max = df.get_second_score().max().tolist()
    min = df.get_second_score().min().tolist()
    print(min, max, mean)
    fig = go.Figure(data=[go.Bar(x=y, y=min, name='min'), go.Bar(x=y, y=mean, name='avg'), go.Bar(x=y, y=max, name='max')]
                    ,layout={"title":"Record of Course 2"})
    return fig

def graph_3_g(df):
    score = df.get_third_score()
    columns = df.get_third_score().columns.tolist()
    c1 = score[columns[0]].value_counts().tolist()
    c2 = score[columns[1]].value_counts().tolist()
    c3 = score[columns[2]].value_counts().tolist()
    c4 = score[columns[3]].value_counts().tolist()
    labels = [['no', 'yes'],
              ['no', 'yes'],
              ['no', 'yes'],
              ['no', 'yes']]

    values = [c1, c2, c3, c4]

    data = []
    x1 = 0
    x2 = 0.20
    for label, value in zip(labels, values):
        data.append(go.Pie(labels=label,
                           values=value,
                           hoverinfo='label+value+percent', textinfo='value',
                           domain={'x': [x1, x2]}
                           )
                    )
        x1 = x1 + 0.25
        x2 = x1 + 0.20
    return go.Figure(data=data,layout={"title":"Record of Course 3"})

