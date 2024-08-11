from flask_wtf import FlaskForm
from wtforms import  StringField ,SubmitField ,IntegerField ,PasswordField ,TextAreaField,SelectField,DateTimeField,DateField,FormField ,SelectMultipleField,BooleanField,FieldList
from wtforms.validators import DataRequired ,Email ,Length



#create  a form Class
class AdminSignupForm(FlaskForm):
    name = StringField(validators=[DataRequired()],render_kw={"placeholder":"Name"})
    username = StringField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Password"})
    email = StringField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    phone = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Phone number"})
    country = StringField(validators=[DataRequired()],render_kw={"placeholder":"Country"})
    state  = StringField(validators=[DataRequired()],render_kw={"placeholder":"State"})
    city = StringField(validators=[DataRequired()],render_kw={"placeholder":"City"})
    pin_code = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Pin code"})
    address_description =TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"Address description"})
    submit = SubmitField('Submit')
class InfluencerSignUpForm(FlaskForm):
    name = StringField(validators=[DataRequired()],render_kw={"placeholder":"Name"})
    username = StringField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Password"})
    email = StringField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    phone = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Phone number"})
    country = StringField(validators=[DataRequired()],render_kw={"placeholder":"Country"})
    state  = StringField(validators=[DataRequired()],render_kw={"placeholder":"State"})
    city = StringField(validators=[DataRequired()],render_kw={"placeholder":"City"})
    pin_code = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Pin code"})
    address_description =TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"Address description"})
    category= SelectField(u'Access Type', choices=[('entertainment', 'Entertainment'),('academic', 'Academic'), ('finance', 'Finance'),('acting', 'Acting'),('art', 'Art'),('tech', 'Tech'),('beauty', 'Beauty'),('commercial', 'Commercial')],render_kw={"placeholder":"Industry"})
    niche= StringField(validators=[DataRequired()],render_kw={"placeholder":"Niche"})

    follower_count = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Total follower count"})
    following_count = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Total following count"})


    submit = SubmitField('Submit')
class SponsorSignUpForm(FlaskForm):
    name = StringField(validators=[DataRequired()],render_kw={"placeholder":"Name"})
    username = StringField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Password"})
    email = StringField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    phone = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Phone number"})
    country = StringField(validators=[DataRequired()],render_kw={"placeholder":"Country"})
    state  = StringField(validators=[DataRequired()],render_kw={"placeholder":"State"})
    city = StringField(validators=[DataRequired()],render_kw={"placeholder":"City"})
    pin_code = IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Pin code"})
    address_description =TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"Address description"})
    industry= SelectField(u'Access Type', choices=[('entertainment', 'Entertainment'),('academic', 'Academic'), ('finance', 'Finance'),('acting', 'Acting'),('art', 'Art'),('tech', 'Tech'),('beauty', 'Beauty'),('commercial', 'Commercial')],render_kw={"placeholder":"Industry"})
    budget= IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Budget"})
    submit = SubmitField('Submit')
class SignInForm(FlaskForm):
    username = StringField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder":"Password"})
    usertype = SelectField(u'Access Type', choices=[('influencer', 'Influencer'),('sponsor', 'Sponsor'), ('admin', 'Admin')],render_kw={"placeholder":"UserType"})
   
    submit = SubmitField('Submit')
class CreateCanpaign(FlaskForm):
    campaignName = StringField(validators=[DataRequired(),Length(min=1,max=20)],render_kw={"placeholder":"Campaign name"})
    description = TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"Description"})
    goal = StringField(validators=[DataRequired(),Length(min=8,max=50)],render_kw={"placeholder":"Goal"})
    budget= IntegerField(validators=[DataRequired()],render_kw={"placeholder":"Budget"})
    startDate = DateField('Start Date', validators=[DataRequired()],format='%Y/%m/%d', render_kw={'placeholder': 'YYYY/MM/DD'})
    endDate = DateField('End Date', validators=[DataRequired()],format='%Y/%m/%d', render_kw={'placeholder': 'YYYY/MM/DD'})
    visibilty =  SelectField(u'Access Type' ,choices=[('default','Select the visibility of your campaign'),('public', 'Public'),('private', 'Private')])

    submit = SubmitField('Submit')

class SearchBox(FlaskForm):
    searchBox = StringField(validators=[DataRequired(),Length(min=1,max=20)],render_kw={"placeholder":"Search"})
    filter_by = SelectField(u'Filter by:', choices=[
        ('username', 'username'),
        ('category', 'category'),
        ('niche', 'niche'),
        ('follower_count', 'follower_count')
    ])
    search = SubmitField('Search')

