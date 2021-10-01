import json
import requests
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask.app import Flask
import plotly.express as px

def retUser(torreUN):
    """Return User data from the api given an Torre.co Username
    
    all in JSON format
    """
    API_ENDPOINT = "https://torre.bio/api/bios/"+str(torreUN)

    r1 = requests.get(url = API_ENDPOINT)
    user_data = json.loads(r1.text)  
    return user_data

#######################################################################################

#CREATE DASH APP

stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = Flask(__name__)
app = dash.Dash('Torre_Test', external_stylesheets=stylesheets)
app.title='Torre_Test'
server = app.server

app.layout=html.Div( children=[
    html.Div(style={'display':'inline-block', 'width':'100%'}, children=[
        html.H1(children='Torre User Personality Comparator', style={'textAlign': 'center'}),
        html.Div(style={'display':'inline'}, children=[
            html.Div(style={'float':'left', 'width':'48%', 'border-width':'1%'},children=[
                html.H2(children='User #1', style={'textAlign': 'center'}),
                dcc.Input(id='user1-input', placeholder='Username...', debounce=True, style={'display':'block', 'margin':'auto', 'align': 'center'}),
                html.Div(id='userpic1', style={'margin-top':'15px'}, children=[]),
                html.H4(id='userfullname1', children=[], style={'textAlign': 'center'}),
                html.H6(id='usertitle1', children=[], style={'textAlign': 'center'}),
                dcc.Markdown(id='markdown1', style={'margin':'2%', 'overflow-x':'hidden'}),
                html.Div(id='bio1', style={'margin':'4%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='markdown1_2', style={'margin':'2%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='interest1', style={'margin':'4%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='markdown1_3', style={'margin':'2%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='strengths1', style={'margin':'4%', 'overflow-x':'hidden'}),
            ]),
            html.Div(style={'float':'right', 'width':'48%', 'border-width':'1%'},children=[
                html.H2(children='User #2', style={'textAlign': 'center'}),
                dcc.Input(id='user2-input', placeholder='Username...', debounce=True, style={'display':'block', 'margin':'auto', 'align': 'center'}),
                html.Div(id='userpic2', style={'margin-top':'15px'}, children=[]),
                html.H4(id='userfullname2', children=[], style={'textAlign': 'center'}),
                html.H6(id='usertitle2', children=[], style={'textAlign': 'center'}),
                dcc.Markdown(id='markdown2', style={'margin':'2%', 'overflow-x':'hidden'}),
                html.Div(id='bio2', style={'margin':'4%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='markdown2_2', style={'margin':'2%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='interest2', style={'margin':'4%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='markdown2_3', style={'margin':'2%', 'overflow-x':'hidden'}),
                dcc.Markdown(id='strengths2', style={'margin':'4%', 'overflow-x':'hidden'}),
            ])
        ]),
    ]),
    html.Div(style={'display':'block'}, children=[
        html.H2(children='Personality', style={'textAlign': 'center'}),
        html.Button('Compare', id='runComparison', style={'verticalAlign': 'middle', 'display':'block'}),
        dcc.Graph(id='contrastFig')
    ])
])



#CALLBACKS

#USER #1
@app.callback(
    [dash.dependencies.Output('userpic1','children'),
    dash.dependencies.Output('userfullname1','children'),
    dash.dependencies.Output('usertitle1','children'),
    dash.dependencies.Output('bio1','children'),
    dash.dependencies.Output('markdown1','children'),
    dash.dependencies.Output('interest1','children'),
    dash.dependencies.Output('markdown1_2','children'),
    dash.dependencies.Output('strengths1','children'),
    dash.dependencies.Output('markdown1_3','children')],
    [dash.dependencies.Input('user1-input','value')],
    prevent_initial_call=True
)
def depUser1(username1):
    """Return basic information for the user #1 to compare
    
    display name, title, bio, interests and strenghts
    """
    userdata1=retUser(username1)
    profPic1=html.Img(src=userdata1['person']['picture'], style={'display':'block', 'margin':'auto', 'border-radius': '50%', 'height':'45%', 'width':'45%'})
    marktitle1='''__About:__
    '''
    userBio1=str(f"{userdata1['person']['summaryOfBio']}")
    marktitle1_2='''__Interests:__
    '''
    interestList1=[]
    for interest in userdata1['interests']:
        interestList1.append(interest['name'])
    interestStr=""""""
    for intName in interestList1:
        interestStr=interestStr+"""

        -"""+intName
    userInterest1=interestStr
    marktitle1_3='''__Strengths:__
    '''
    strengthsList1=[]
    for strength in userdata1['strengths']:
        strengthsList1.append(strength['name'])
    strengthsStr=""""""
    for strngName in strengthsList1:
        strengthsStr=strengthsStr+"""

        -"""+strngName
    userStrengths1=strengthsStr
    
    return profPic1, userdata1['person']['name'], userdata1['person']['professionalHeadline'], userBio1, marktitle1, userInterest1, marktitle1_2, userStrengths1, marktitle1_3

#USER #2
@app.callback(
    [dash.dependencies.Output('userpic2','children'),
    dash.dependencies.Output('userfullname2','children'),
    dash.dependencies.Output('usertitle2','children'),
    dash.dependencies.Output('bio2','children'),
    dash.dependencies.Output('markdown2','children'),
    dash.dependencies.Output('interest2','children'),
    dash.dependencies.Output('markdown2_2','children'),
    dash.dependencies.Output('strengths2','children'),
    dash.dependencies.Output('markdown2_3','children')],
    [dash.dependencies.Input('user2-input','value')],
    prevent_initial_call=True
)
def depUser2(username2):
    """Return basic information for the user #2 to compare
    
    display name, title, bio, interests and strenghts
    """
    userdata2=retUser(username2)
    profPic2=html.Img(src=userdata2['person']['picture'], style={'display':'block', 'margin':'auto', 'border-radius': '50%', 'height':'45%', 'width':'45%'})
    marktitle2='''__About:__
    '''
    userBio2=str(f"{userdata2['person']['summaryOfBio']}")
    marktitle2_2='''__Interests:__
    '''
    interestList2=[]
    for interest in userdata2['interests']:
        interestList2.append(interest['name'])
    interestStr=""""""
    for intName in interestList2:
        interestStr=interestStr+"""

        -"""+intName
    userInterest2=interestStr
    marktitle2_3='''__Strengths:__
    '''
    strengthsList2=[]
    for strength in userdata2['strengths']:
        strengthsList2.append(strength['name'])
    strengthsStr=""""""
    for strngName in strengthsList2:
        strengthsStr=strengthsStr+"""

        -"""+strngName
    userStrengths2=strengthsStr
    
    return profPic2, userdata2['person']['name'], userdata2['person']['professionalHeadline'], userBio2, marktitle2, userInterest2, marktitle2_2, userStrengths2, marktitle2_3

#Comparison Graph
@app.callback(
    dash.dependencies.Output('contrastFig','figure'),
    dash.dependencies.Input('runComparison','n_clicks'),
    [dash.dependencies.State('user1-input','value'),
    dash.dependencies.State('user2-input','value')],
    prevent_initial_call=True
)
def runComparison(dummyc, userval1, userval2):
    """Return Plotly Plot with Personality comparison between 2 users
    
    line plot
    """
    userdata1=retUser(userval1)
    userdata2=retUser(userval2)
    userdict1={
        'User':userval1,
        userdata1['personalityTraitsResults']['analyses'][0]['groupId']:userdata1['personalityTraitsResults']['analyses'][0]['analysis'], 
        userdata1['personalityTraitsResults']['analyses'][1]['groupId']:userdata1['personalityTraitsResults']['analyses'][1]['analysis'], 
        userdata1['personalityTraitsResults']['analyses'][2]['groupId']:userdata1['personalityTraitsResults']['analyses'][2]['analysis'], 
        userdata1['personalityTraitsResults']['analyses'][3]['groupId']:userdata1['personalityTraitsResults']['analyses'][3]['analysis'], 
        userdata1['personalityTraitsResults']['analyses'][4]['groupId']:userdata1['personalityTraitsResults']['analyses'][4]['analysis'], 
        userdata1['personalityTraitsResults']['analyses'][5]['groupId']:userdata1['personalityTraitsResults']['analyses'][5]['analysis'], 
        userdata1['personalityTraitsResults']['analyses'][6]['groupId']:userdata1['personalityTraitsResults']['analyses'][6]['analysis']
    }
    userdict2={
        'User':userval2,
        userdata2['personalityTraitsResults']['analyses'][0]['groupId']:userdata2['personalityTraitsResults']['analyses'][0]['analysis'], 
        userdata2['personalityTraitsResults']['analyses'][1]['groupId']:userdata2['personalityTraitsResults']['analyses'][1]['analysis'], 
        userdata2['personalityTraitsResults']['analyses'][2]['groupId']:userdata2['personalityTraitsResults']['analyses'][2]['analysis'], 
        userdata2['personalityTraitsResults']['analyses'][3]['groupId']:userdata2['personalityTraitsResults']['analyses'][3]['analysis'], 
        userdata2['personalityTraitsResults']['analyses'][4]['groupId']:userdata2['personalityTraitsResults']['analyses'][4]['analysis'], 
        userdata2['personalityTraitsResults']['analyses'][5]['groupId']:userdata2['personalityTraitsResults']['analyses'][5]['analysis'], 
        userdata2['personalityTraitsResults']['analyses'][6]['groupId']:userdata2['personalityTraitsResults']['analyses'][6]['analysis']
    }

    analysesDF=pd.DataFrame(columns=[
        'User',
        'openness-to-experience', 
        'honesty-humility', 
        'agreeableness', 
        'altruism', 
        'conscientiousness', 
        'emotionality', 
        'extraversion'
        ]
    )
    analysesDF=analysesDF.append(userdict1, ignore_index=True)
    analysesDF=analysesDF.append(userdict2, ignore_index=True)
    analysesDFmelt = pd.melt(analysesDF, id_vars=['User'], var_name='analysis')
    comparisonFig=px.line(analysesDFmelt, x='analysis', y='value', color='User')
    return comparisonFig

if __name__ == '__main__':
    app.run_server(debug=True, port=8001)
