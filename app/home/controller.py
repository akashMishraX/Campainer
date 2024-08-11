from flask import current_app as app
from flask import render_template ,url_for ,redirect ,request ,session
from flask_login import UserMixin ,LoginManager ,login_required,login_user,logout_user,current_user
from flask_bcrypt import Bcrypt
from datetime import date
from app.authentication.models import *
from app.home.router import *
from app.authentication.forms import *


bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



@app.route('/',methods=['GET'])
def default():
    return redirect(home_url) 

#SIGNIN ADN SIGNUP
@app.route(home_url,methods =['GET'])
def home():
    return render_template('home.html')
@app.route(register_home_url,methods =['GET'])
def register():
    return render_template('register_home.html')

#LOGIN AND SIGNUP MANGEMENT 
@app.route(admin_signUp_url,methods = ['GET','POST'])
def adminSignUp():  
    name=None
    username=None
    password=None
    email=None
    phone=None
    country=None
    state=None 
    city=None 
    pin_code=None 
    address_description=None
    form = AdminSignupForm()
    #Validate form
    if form.validate_on_submit():
        name = form.name.data
        username=form.username.data
        password=form.password.data
        email=form.email.data
        phone=form.phone.data
        country=form.country.data
        state=form.state.data 
        city=form.city.data 
        pin_code=form.pin_code.data 
        address_description=form.address_description.data
          #adding admin
        user = User.query.filter_by(username=username).first()
        if not user:
            createAdmin(name,username,bcrypt.generate_password_hash(password),email,phone,country,state,city,pin_code,address_description)
        else:
            raise KeyError('Username already exist')  
        
        form.name.data =''
        form.username.data=''
        form.password.data=''
        form.email.data=''
        form.phone.data=''
        form.country.data=''
        form.state.data =''
        form.city.data =''
        form.pin_code.data =''
        form.address_description.data=''
        
    return render_template('auth/adminSignUp.html',
                        name = name,
                        username=username,
                        password=password,
                        email=email,
                        phone=phone,
                        country=country,
                        state=state, 
                        city=city ,
                        pin_code=pin_code ,
                        address_description=address_description,
                        form=form
                        )

@app.route(influencer_signUp_url,methods = ['GET','POST'])
def influencerAboutSignUp():    
    name=None
    username=None
    password=None
    email=None
    phone=None
    country=None
    state=None 
    city=None 
    pin_code=None 
    address_description=None
    category=None
    niche=None
    follower_count=None
    following_count=None

    form = InfluencerSignUpForm()
    #Validate form
    if form.validate_on_submit():
        name = form.name.data
        username=form.username.data
        password=form.password.data
        email=form.email.data
        phone=form.phone.data
        country=form.country.data
        state=form.state.data 
        city=form.city.data 
        pin_code=form.pin_code.data 
        address_description=form.address_description.data
        category=form.category.data
        follower_count=form.follower_count.data
        following_count=form.following_count.data
        niche=form.niche.data          
        

        user = User.query.filter_by(username=username).first()
        if not user:
            createInfluencer(name,username,bcrypt.generate_password_hash(password,10),email,phone,country,state,city,pin_code,address_description,category,niche,follower_count,following_count)
            print('HERE')
        else:
            raise KeyError('Username already exist')  

        form.name.data =''
        form.username.data=''
        form.password.data=''
        form.email.data=''
        form.phone.data=''
        form.country.data=''
        form.state.data =''
        form.city.data =''
        form.pin_code.data =''
        form.address_description.data=''
        form.category.data=''
        form.niche.data=''
        form.follower_count.data=''
        form.following_count.data=''

        return redirect(url_for('SignIn'))
    return render_template('auth/influencerSignUp.html',
                        name = name,
                        username=username,
                        password=password,
                        email=email,
                        phone=phone,
                        country=country,
                        state=state, 
                        city=city ,
                        pin_code=pin_code ,
                        address_description=address_description,
                        category=category,
                        niche=niche,
                        follower_count=follower_count,
                        following_count=following_count,
                        form=form
                        )



@app.route(sponsor_signUp_url,methods = ['GET','POST'])
def sponorSignUp():
    name=None
    username=None
    password=None
    email=None
    phone=None
    country=None
    state=None 
    city=None 
    pin_code=None 
    address_description=None
    industry=None
    budget=None
    form = SponsorSignUpForm()
    #Validate form
    if form.validate_on_submit():
        name = form.name.data
        username=form.username.data
        password=form.password.data
        email=form.email.data
        phone=form.phone.data
        country=form.country.data
        state=form.state.data 
        city=form.city.data 
        pin_code=form.pin_code.data 
        address_description=form.address_description.data
        industry=form.industry.data
        budget=form.budget.data
         #adding sponsor
        user = User.query.filter_by(username=username).first()
        if not user:
            id =createSponsor(name,username,bcrypt.generate_password_hash(password),email,phone,country,state,city,pin_code,address_description,industry,budget)
            print(id)
        else:
            raise KeyError('Username already exist')   
        form.name.data =''
        form.username.data=''
        form.password.data=''
        form.email.data=''
        form.phone.data=''
        form.country.data=''
        form.state.data =''
        form.city.data =''
        form.pin_code.data =''
        form.address_description.data=''
        form.industry.data=''
        form.budget.data=''
        return redirect(url_for('SignIn'))
    return render_template('auth/sponsorSignUp.html',
                        name = name,
                        username=username,
                        password=password,
                        email=email,
                        phone=phone,
                        country=country,
                        state=state, 
                        city=city ,
                        pin_code=pin_code ,
                        address_description=address_description,
                        industry=industry,
                        budget=budget,
                        form=form
                        )

@app.route(sign_in_url,methods = ['GET','POST'])
def SignIn():  
    username=None
    password=None
    usertype = None
    form = SignInForm()
    #Validate form@app.route('/create_route',methods = ['GET','POST'])
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        usertype = form.usertype.data

        user =User.query.filter_by(username=username).first()
        role_id = user.role_id
        role = Roles.query.filter_by(role_id=role_id).first()
        
        if user:
            if bcrypt.check_password_hash(user.password,password):
                login_user(user)
              
                if  role.role_name == 'admin' and usertype == 'admin':
                    return redirect(url_for('admin_dashboard'))                   
                elif role.role_name == 'influencer' and usertype == 'influencer':
                    return redirect(url_for('influencer_dashboard'))
                elif  role.role_name == 'sponsor' and usertype == 'sponsor':
                    return redirect(url_for('sponsor_dashboard'))
        else:
            print('USER ALREADY EXIST!!')
        form.username.data=''
        form.password.data=''
        form.usertype.data=''
    return render_template('auth/signInPage.html',
                        username=username,
                        password=password,
                        usertype=usertype,
                        form=form
                        )

@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('SignIn'))




#ADMIN MANGEMENT
@app.route(admin_base_url,methods =['GET','POST'])
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')





#INFLUENCER MANGEMENT
@app.route(influencer_base_url,methods =['GET','POST'])
@login_required
def influencer_dashboard():
    return render_template('influencer/dashboard.html')





#SPONSOR MANGEMENT 
@app.route(sponsor_base_url,methods =['GET','POST'])
@login_required
def sponsor_dashboard():
    #nummber of  active and complted camapign 
    # number of ad request
    campaigns = db.session.query(Campaign,Sponsors,User).select_from(Campaign).join(Sponsors).join(User).filter(Sponsors.sponsors_id==current_user.id).all()
    numberOfActiveCampaign = 0
    numberOfCompletedCampaign = 0
    for campaign in campaigns:
        if campaign[0].active == 1:
            numberOfActiveCampaign += 1
        elif campaign[0].active == 0:
            numberOfCompletedCampaign += 1
        else:
            pass
    adRequst = db.session.query(Ad_request,Campaign,Influencer).select_from(Ad_request).join(Campaign).join(Influencer).filter(Sponsors.sponsors_id==current_user.id).all()
    print(adRequst)
    incomingAdRequest = []
    outGoingAdRequest = []
    totalNumberOfAdRequest = 0
    for ad in adRequst:
        totalNumberOfAdRequest += 1
        obj ={
            'influencer_username':ad[2].username,
            'campaign_name':ad[1].campaign_name,
            'message':ad[0].message,
            'requirement':ad[0].requirement,
            'pay':ad[0].pay,
            'status':ad[0].status
        }
        if ad[0].requested_by == 'sponsor':
            outGoingAdRequest.append(obj)
        elif ad[0].requested_by == 'influencer':
            incomingAdRequest.append(obj)
    print(incomingAdRequest)

    return render_template('sponsor/dashboard.html',
                    numberOfActiveCampaign=numberOfActiveCampaign,
                    numberOfCompletedCampaign=numberOfCompletedCampaign,
                    totalNumberOfAdRequest=totalNumberOfAdRequest,
                    incomingAdRequest=incomingAdRequest,
                    outGoingAdRequest=outGoingAdRequest
                    )

@app.route(sponsor_profile,methods =['GET','POST'])
@login_required
def sponsor_profile():
    return render_template('sponsor/profile.html')

@app.route(sponsor_campiagn,methods =['GET','POST','PUT'])
@login_required
def sponsor_campiagn(): 

    #CHANGE ACTIVE STATUS
    camapign_name=  request.args.get('submit')
    if camapign_name:
        campaign = Campaign.query.filter_by(campaign_name=camapign_name).first()
        if campaign.active == 1: 
            campaign.active = 0
        else:
            campaign.active = 1
        db.session.commit()

    #MAIN 
    campaigns = db.session.query(Campaign,Sponsors,User).select_from(Campaign).join(Sponsors).join(User).filter(Sponsors.sponsors_id==current_user.id).all()
    activeData=[]
    pastData=[]
    for campaign in campaigns:
        # print(campaign)
        obj={
            'campaign_name':campaign[0].campaign_name,
            'sponsor_name':campaign[2].name,
            'description':campaign[0].description,
            'goal':campaign[0].goal,
            'start_date':campaign[0].start_date,
            'end_date':campaign[0].end_date,
            'budget':campaign[0].budget,
            "number_of_active_ads":campaign[0].numberOfActiveAds,
            'visibilty':campaign[0].visibilty
        }
        if campaign[0].active == 1:
            activeData.append(obj)
        elif campaign[0].active == 0:
            pastData.append(obj)
        else:
            pass
    
    # if request.method == 'delete':

    return render_template('sponsor/campaign/campaign.html',activeData=activeData,pastData=pastData)
    
@app.route(sponsor_create_campaign,methods =['GET','POST','DELETE'])
@login_required
def create_campaign():
    if request.method == 'POST':
        campaignName=request.form.get('campaignName')
        description=request.form.get('description')
        goal=request.form.get('goal')
        budget=request.form.get('budget')
        startDate=request.form.get('startDate')
        endDate=request.form.get('endDate')
        visibilty=request.form.get('visibilty')   
        # date_str = startDate.strftime('%Y-%m-%d')
       
        startDate = date(int(startDate.split('-')[0]),int(startDate.split('-')[1]),int(startDate.split('-')[2]))
        endDate = date(int(endDate.split('-')[0]),int(endDate.split('-')[1]),int(endDate.split('-')[2]))
        createCampaign(campaignName,description,goal,budget,startDate,endDate,visibilty,current_user.id)
        return redirect(url_for('sponsor_campiagn'))


    campaignName=None
    description=None
    goal=None
    budget=None
    startDate=None
    endDate=None
    visibilty=None   
    form = CreateCanpaign()
    #Validate form
    if form.validate_on_submit():
        campaignName=form.campaignName.data
        description=form.description.data
        goal=form.goal.data
        budget=form.budget.data
        startDate=form.startDate.data
        endDate=form.endDate.data
        visibilty=form.visibilty.data  
 
        
        form.campaignName.data =''
        form.description.data=''
        form.goal.data=''
        form.budget.data=''
        form.startDate.data=''
        form.endDate.data=''
        form.visibilty.data=''
    
        
    return render_template('sponsor/campaign/campaignForm.html',
                        heading='Create a new campaign',
                        campaignName =campaignName,
                        description=description,
                        goal=goal,
                        budegt=budget,
                        startDate=startDate,
                        endDate=endDate,
                        visibilty=visibilty,
                        root=sponsor_create_campaign,
                        form=form
                        )

@app.route(sponsor_upadte_campaign,methods =['GET','POST'])
@login_required
def update_campaign():
    if request.method == 'POST':
        camapign_name=request.form.get('campaignName')
        description=request.form.get('description')
        goal=request.form.get('goal')
        budget=request.form.get('budget')
        startDate=request.form.get('startDate')
        endDate=request.form.get('endDate')
        visibilty=request.form.get('visibilty')   
        # date_str = startDate.strftime('%Y-%m-%d')
       
        startDate = date(int(startDate.split('-')[0]),int(startDate.split('-')[1]),int(startDate.split('-')[2]))
        endDate = date(int(endDate.split('-')[0]),int(endDate.split('-')[1]),int(endDate.split('-')[2]))
        
      
        campaign = Campaign.query.filter_by(campaign_name=camapign_name).first()
        campaign.description = description
        campaign.goal = goal
        campaign.budget = budget
        campaign.start_date = startDate
        campaign.end_date = endDate
        campaign.visibilty = visibilty
        db.session.commit()


        return redirect(url_for('sponsor_campiagn'))

    campaignName=None
    description=None
    goal=None
    budget=None
    startDate=None
    endDate=None
    visibilty=None   
    form = CreateCanpaign()

    camapign_name = request.args.get('campaign_name')
    campaign = Campaign.query.filter_by(campaign_name=camapign_name).first()
    # print(campaign)  
    campaign_description = campaign.description
    campaign_goal = campaign.goal
    campaign_budget = campaign.budget
    campaign_start_date = campaign.start_date
    campaign_end_date = campaign.end_date
    campaign_visibilty = campaign.visibilty

    
    form.campaignName.data = camapign_name
    form.campaignName.render_kw = {"hidden": True}
    form.description.data= campaign_description
    form.goal.data= campaign_goal
    form.budget.data= campaign_budget
    form.startDate.data= campaign_start_date
    form.endDate.data= campaign_end_date
    form.visibilty.data= campaign_visibilty

    #Validate form
    if form.validate_on_submit():
        description=form.description.data
        goal=form.goal.data
        budget=form.budget.data
        startDate=form.startDate.data
        endDate=form.endDate.data
        visibilty=form.visibilty.data  
 
        
        form.campaignName.data =''
        form.description.data=''
        form.goal.data=''
        form.budget.data=''
        form.startDate.data=''
        form.endDate.data=''
        form.visibilty.data=''

        
    return render_template('sponsor/campaign/campaignForm.html',
                        heading='update campaign',
                        campaignName =campaignName,
                        description=description,
                        goal=goal,
                        budegt=budget,
                        startDate=startDate,
                        endDate=endDate,
                        visibilty=visibilty,
                        root=sponsor_upadte_campaign,
                        form=form
                        )
        
@app.route(sponsor_delete_campaign,methods =['GET','POST'])
@login_required  
def deleteConformation():
    if request.method == 'POST':
        data = request.form.get('campaign_name')
        campaign = Campaign.query.filter_by(campaign_name=data).first()  
        db.session.delete(campaign)
        db.session.commit()
        return redirect(url_for('sponsor_campiagn'))

    data = request.args.get('delete')

    return render_template('sponsor/deleteConformation.html',data=data)


@app.route(sponsor_influencer,methods =['GET','POST'])
@login_required
def sponsor_influencer():

    if request.method == 'POST':
        searchBox = request.form.get('searchBox')
        filter_by = request.form.get('filter_by')
       
        data =[]
        if filter_by == 'username':
            data = db.session.query(User,Influencer).join(User).filter(User.username==searchBox).all()
        elif filter_by == 'category':
            data = db.session.query(User,Influencer).join(User).filter(Influencer.category==searchBox).all()
        elif filter_by == 'niche':
            data = db.session.query(User,Influencer).join(User).filter(Influencer.niche==searchBox).all()
        elif filter_by == 'follower_count':
            data = db.session.query(User,Influencer).join(User).filter(Influencer.follower_count>=searchBox).all()
        else:
            pass
    

        print(data)
        searchedData = []
        for all in data:
            obj={
                'name':all[0].name,
                'username':all[0].username,
                'category':all[1].category,
                'niche':all[1].niche,
                'follower_count':all[1].follower_count,
                'following_count':all[1].following_count,
            }
            searchedData.append(obj)
        session['searchedData'] = searchedData
        print(searchedData)
    searchedData = session.get('searchedData',[])
    print(searchedData)
    campaign_all = Campaign.query.filter_by(active=1).all() # later upadte it to active as flagged is for admin
    campaigns=[]
    for campaign in campaign_all:
        campaigns.append(campaign.campaign_name)
    searchBox=None
    filter_by=None
    form = SearchBox()
    if form.validate_on_submit():
        searchBox=form.searchBox.data
        filter_by=form.filter_by.data

        form.searchBox.data=''
        form.filter_by.data=''

    return render_template('sponsor/influencer/search.html',
                        searchBox=searchBox,
                        filter_by=filter_by,
                        campaigns=campaigns,
                        searchedData=searchedData,
                        form=form)



@app.route(sponsor_create_ad_request,methods =['GET','POST'])
@login_required
def sponsor_ad_request():
    if request.method == 'POST':
        influencer_username = request.form.get('influencer')
        campaign = request.form.get('campaign')
        message = request.form.get('message')
        requirement = request.form.get('requirement')
        pay = request.form.get('pay')
        print(influencer_username,campaign,message,requirement,pay)


        influencer = User.query.filter_by(username=influencer_username).first()
        campaign = Campaign.query.filter_by(campaign_name=campaign).first()
        #Craete Ad request
        print(influencer.id,campaign.campaign_id)
        createAdRequest(message,requirement,pay,'sponsor','influencer',influencer.id,campaign.campaign_id)

        return redirect(url_for('sponsor_influencer'))
    return redirect(url_for('sponsor_influencer'))



@app.route('/clearSession',methods =['GET','POST'])
def clearSession():
    session.pop('searchedData',[])
    return redirect(url_for('sponsor_influencer'))


#Just use it once only for creating roles as per the requirement need to work aroud for proper implimentaion
@app.route('/create_route',methods = ['GET','POST'])

def create_routes():
    if request.method == 'POST':
        db.create_all()
        createAllRole()
        db.session.commit()
 

    return render_template('hidden.html',data='')
