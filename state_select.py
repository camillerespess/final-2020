from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application = app

app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

db_name = 'artprograms.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

db = SQLAlchemy(app)

class Art(db.Model):
    __tablename__ = 'arts_data'
    StateNumber = db.Column(db.Integer, primary_key=True)
    StateName = db.Column(db.String)
    Source = db.Column(db.String)
    ArtsDefinedCore = db.Column(db.String)
    EarlyChildhoodStandards = db.Column(db.String)
    ElementaryandorSecondaryStandards = db.Column(db.String)
    ArtsRequiredElementary = db.Column(db.String)
    ArtsRequiredMiddle = db.Column(db.String)
    ArtsRequiredHigh = db.Column(db.String)
    OptionforGradRequirement = db.Column(db.String)
    RequireStateDistrictTest = db.Column(db.String)
    ArtsforSchoolAccred = db.Column(db.String)
    StateProvidesFunding = db.Column(db.String)
    LinkSource = db.Column(db.String)
    DataCollectionYear = db.Column(db.String)
    StudentPopulation = db.Column(db.Integer)
    RawSchoolNum = db.Column(db.Integer)
    SchoolsWithoutArts = db.Column(db.Integer)
    StudentsWithoutAccess = db.Column(db.Integer)
    PctWithStudentsWithAnyAccess = db.Column(db.Integer)
    PctHSStudentsWithAnyAccess = db.Column(db.Float)
    PctStudentsWithAccesstoAll = db.Column(db.Integer)
    PctSchoolsWithAccesstoAll = db.Column(db.Integer)
    PctStudentsWithoutAnyAccess = db.Column(db.Integer)
    PctSchoolsWithAccess = db.Column(db.Integer)
    HighPovertyAccess = db.Column(db.Integer)
    HighPovertyEnrollmentPct = db.Column(db.Integer)
    LocationsLeastAccess = db.Column(db.String)
    DemoLeastAcess = db.Column(db.String)
    PctAnyArtsEnrollment = db.Column(db.Float)
    PctHighAnyArtsEnrollment = db.Column(db.Float)
    PctElemAnyArtsEnrollment = db.Column(db.Float)
    PctVisArtEnrollment = db.Column(db.Float)
    PctMusicEnrollment = db.Column(db.Float)
    PctTheatreEnrollment = db.Column(db.Float)
    PctWithVisArts = db.Column(db.Float)
    PctWithMusic = db.Column(db.Float)
    PctWithTheatre = db.Column(db.Float)
    PctWithDance = db.Column(db.Float)
    PctWithElemArts = db.Column(db.Float)
    PctWithElemMusic = db.Column(db.Float)
    PctWithElemTheatre = db.Column(db.Float)
    PctWithHSArt = db.Column(db.Float)
    PctWithHSMusic = db.Column(db.Float)
    PctWithHSTheatre = db.Column(db.Float)

arts = Art.query.order_by(Art.StateName).all()
pairs_list = []
for art in arts:
    pairs_list.append( (art.StateNumber, art.StateName) )

# Flask-WTF form magic
# set up the quickform - select includes value, option text (value matches db)
# all that is in this form is one select menu and one submit button
class ArtSelect(FlaskForm):
    select = SelectField( 'View more on arts education for every state:',
      choices=pairs_list
      )
    submit = SubmitField('Submit')

# routes

# starting page for app
@app.route('/')
def index():
    # make an instance of the WTF form class we created, above
    form = ArtSelect()
    # pass it to the template
    return render_template('index.html', form=form)


# whichever id comes from the form, that one state will be displayed
@app.route('/art', methods=['POST'])
def art_detail():
    art_id = request.form['select']
    # get all columns for the one sock with the supplied id
    the_state = Art.query.filter_by(StateNumber=art_id).first()
    # pass them to the template
    return render_template('state.html', the_state=the_state)


if __name__ == '__main__':
    app.run(debug=True)
