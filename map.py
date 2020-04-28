import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
df = pd.read_csv('https://raw.githubusercontent.com/camillerespess/final-2020/master/art_data.csv')

username = 'camillerose' # your username
api_key = 'OrUvGgri7q7HsWaGbwa5' # your api key - go to profile > settings > regenerate key

for col in df.columns:
    df[col] = df[col].astype(str)


df['text'] = df['StateName'] + '<br>' + 'Number of public schools:' + ' ' + df['RawSchoolNum'] + '<br>' + \
    'The state ' + df['ArtsDefinedCore'] + ' define arts as a core academic subject.' + '<br>' + \
    'The state ' + df['ArtsforSchoolAccred'] + ' require arts programs for school accreditation.' + '<br>' + \
    'Percent of schools with music classes:' + ' ' + df['PctWithMusic'] + '<br>' + \
    'Percent of schools with visual arts classes:' + ' ' + df['PctWithVisArts']

fig = go.Figure(data=go.Choropleth(
    locations=df['id'],
    z=df['StudentPopulation'],
    locationmode='USA-states',
    colorscale='Picnic',
    autocolorscale=False,
    text=df['text'], # hover text
    marker_line_color='white', # line markers between states
    colorbar_title="Student Population"
))

fig.update_layout(
    title_text='Where Are the Arts?<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
)

fig.show()
pio.write_html(fig, file='map.html', auto_open=True)
