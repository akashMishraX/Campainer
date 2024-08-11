from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy() # intiliaze db
from datetime import date

#User Table
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)#primary key 
    username =  db.Column(db.String(25),  nullable=False ,unique=True)
    password = db.Column(db.String(25),  nullable=False)
    name = db.Column(db.String(25),  nullable=False)
    email = db.Column(db.String(25),unique=True, nullable=False)
    phone_number  = db.Column(db.String(15), nullable=False)
    #many-to-many
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    #one-to-one

    influencer = db.relationship('Influencer',uselist=False,backref='user')
    sponsors = db.relationship('Sponsors',uselist=False,backref='user')
    address = db.relationship('Address',uselist=False,backref='user')

    
    def createUser(self, username,password,name,email,phone_number,role_name):
        try:
            role = Roles.query.filter_by(role_name=role_name).first()
            if role:
                newUser = User(
                    username=username,
                    password=password,
                    name=name,
                    email=email,
                    phone_number=phone_number,
                    role=role
                )
                db.session.add(newUser)
                db.session.commit()  
            else:
                raise ValueError('No such role exist')
            return {
                'id':newUser.id
                }
        except Exception as error:
            raise ValueError(error)

    
class Roles(db.Model,UserMixin):
    role_id = db.Column(db.Integer,primary_key=True , autoincrement=True) #primary key
    role_name = db.Column(db.String(25),nullable=False,unique=True)
    user = db.relationship('User',backref='role')

    def createNewRole(self,role_name):
        try:
                role = Roles(role_name=role_name)
                db.session.add(role)
                db.session.commit()
        except Exception as error:
            raise ValueError(error)

    def updateRoleName(self,role_id,new_role_name):
        try:
        
             
                role = Roles.query.filter_by(role_id=role_id).first()
                role.role_name = new_role_name
                db.session.commit()
        except Exception as error:
              
            raise ValueError(error)


    def deleteRole(self,role_name):
        try:
            
             
                role_name = Roles.query.filter_by(role_name=role_name).first()
                db.session.delete(role_name)
                db.session.commit()
        except Exception as error:
              
            raise ValueError(error)

#Address Table
class Address(db.Model,UserMixin):
    id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)#foreign key #primary key
    country = db.Column(db.String(25),nullable=False)
    state = db.Column(db.String(25),nullable=False)
    city = db.Column(db.String(25),nullable=False)
    pin_code = db.Column(db.Integer,nullable=False)
    address_desscription = db.Column(db.String(25),nullable=False)

    def addAddress(self,country,state,city,pin_code,address_desscription,id):      
        try:  
                user = User.query.filter_by(id=id).first()
                address = Address(
                    country = country,
                    state = state,
                    city = city,
                    pin_code = pin_code,
                    address_desscription = address_desscription,
                    user = user
                )
                db.session.add(address)
                db.session.commit()
                    
        except Exception as error:
              
            raise ValueError(error)

#Influencer Table
class Influencer(db.Model,UserMixin):
    influencer_id = db.Column(db.Integer,db.ForeignKey('user.id'), primary_key=True) #foreign key #primary key
    username = db.Column(db.String(25), unique=True, nullable=False)
    category = db.Column(db.String(25), nullable=False)
    niche = db.Column(db.String(25), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)
    following_count = db.Column(db.Integer, nullable=False)
    flagged = db.Column(db.Boolean, nullable=False)

    #one-to-many
    ad_request = db.relationship('Ad_request',backref='influencer',lazy=True)

    def changeFlag(self,flag,influencer_id):
        try: 
                influencer = Influencer.query.filter_by(influencer_id=influencer_id).first()
                influencer.flagged = flag
                db.session.commit()
            
        except Exception as error:
              
            raise ValueError(error)


    def addInfluencer(self,username,category,niche,follower_count,following_count,id):
        try:       
            user = User.query.filter_by(id=id).first()
            influencer = Influencer(
            username=username,
            category = category,
            niche=niche,
            follower_count=follower_count,
            following_count=following_count,
            flagged = False,
            user=user
            )
            db.session.add(influencer)
            db.session.commit()
            return {
                'influencer_id':influencer.influencer_id,
                }
        except Exception as error:
              
            raise ValueError(error)
  
    #delete

#Sponsors Table
class Sponsors(db.Model,UserMixin):
    sponsors_id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)#foreign key #primary key
    industry = db.Column(db.String(25), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    flagged = db.Column(db.Boolean, nullable=False)
    #one-to-one
    campaign = db.relationship('Campaign',backref='sponsors')

    def changeFlag(self,flag,sponsors_id):
        try:

            sponsor = Sponsors.query.filter_by(sponsors_id=sponsors_id).first()
            sponsor.flagged = flag
            db.session.commit()
            return True
        except Exception as error:
              
            raise ValueError(error)

    def addSponsor(self,industry,budget,id):
        try:
            
            
            user = User.query.filter_by(id=id).first()
            sponsor = Sponsors(
                industry=industry,
                budget=budget,                   
                flagged = False,
                user=user)
            db.session.add(sponsor)
            db.session.commit()
            return {
                'sponsors_id':sponsor.sponsors_id,
                }
        except Exception as error:
              
            raise ValueError(error)
    
    def deleteSponsor(self,sponsors_id):
        try:
        
            
            sponsor = Sponsors.query.filter_by(sponsors_id=sponsors_id).first()
            db.session.delete(sponsor)
            db.session.commit()
        except Exception as error:
              
            raise ValueError(error)

# campaign_visibility_enum = db.Enum('public','private' ,name='campaign_visibility_enum')
#Campaign Table
class Campaign(db.Model,UserMixin):
    campaign_id = db.Column(db.Integer, primary_key=True, autoincrement=True)#primary key
    sponsors_id = db.Column(db.Integer, db.ForeignKey('sponsors.sponsors_id')) #foreign key
    campaign_name = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(25),nullable=False)
    goal = db.Column(db.String(25),nullable=False)
    budget = db.Column(db.Integer,nullable=False)
    start_date = db.Column(db.Date,nullable=False)
    end_date = db.Column(db.Date,nullable=False)
    numberOfActiveAds = db.Column(db.Integer,nullable=False)# with each new ad_request update it
    visibilty = db.Column(db.String(25),nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    flagged = db.Column(db.Boolean, nullable=False)

    #one-to-many
    ad_request = db.relationship('Ad_request',backref='campaign',lazy=True)


     
    def checkNumberOfActiveAds(self,campaign_id):
    
        campaign = Campaign.query.filter_by(campaign_id=campaign_id).first()
        return campaign.numberOfActiveAds
    
    def updateNumberOfActiveAds(self,campaign_id):
        try:
     
                campaign = Campaign.query.filter_by(campaign_id=campaign_id).first()
                result = Accepted_ad_request.query.filter_by(campaign_id=campaign.campaign_id).all()
                campaign.numberOfActiveAds = result.len()
                db.session.commit()
        except Exception as error:
              
            raise ValueError(error)

    def deleteCampaign(self,campaign_id):
        if Campaign.checkNumberOfActiveAds(campaign_id) != 0:
            raise ValueError("Can only delete if cmapiagn has no active ad_request")
        else:
            try:
            
                 
                    campaign = Campaign.query.filter_by(campaign_id=campaign_id).first()
                    db.session.delete(campaign)
                    db.session.commit()

            except Exception as error:
                  
                raise ValueError(error)

# ad_request_status_enum = db.Enum('pending','accepted','rejected','negotation',name='ad_request_status_enum')
# request_enum = db.Enum('sponsor','influencer' ,name='request_by_enum')
#Ad_request Table
class Ad_request(db.Model,UserMixin):
    influencer_id = db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'), primary_key=True) #foreign key #primary key
    campaign_id = db.Column(db.Integer,db.ForeignKey('campaign.campaign_id'), primary_key=True)#foreign key #primary key
    message = db.Column(db.String(25),nullable=False)
    requirement = db.Column(db.String(25),nullable=False)
    pay = db.Column(db.Integer,nullable=False)
    status = db.Column(db.String(25),nullable=False)# add contraint here 
    requested_by =  db.Column(db.String(25),nullable=False)
    requested_to = db.Column(db.String(25),nullable=False)


    def checkStatus(self,influencer_id,campaign_id):
    
        ad_request = Ad_request.query.filter_by(influencer_id=influencer_id,campaign_id=campaign_id).first()
        return ad_request.status
    
    def updateStatus(self,newStatus,influencer_id,campaign_id,):
        try:
        
             
                ad_request = Ad_request.query.filter_by(influencer_id=influencer_id,campaign_id=campaign_id).first()
                ad_request.status = newStatus
                db.session.commit()
        except Exception as error:
              
            raise ValueError(error)

    def negotiate(self,requested_by ,requested_to,new_pay,influencer_id,campaign_id):
        try:
        
             
                ad_request = Ad_request.query.filter_by(influencer_id=influencer_id,campaign_id=campaign_id).first()
                if ad_request.status != 'negotation':
                    ad_request.updateStatus('negotation')
                ad_request.requested_by = requested_by
                ad_request.requested_to = requested_to
                ad_request.pay = new_pay
                db.session.commit()
        except Exception as error:
              
            raise ValueError(error)

    def accept(self,finalpay,influencer_id,campaign_id,):
        try:
            
             
                ad_request = Ad_request.query.filter_by(influencer_id=influencer_id,campaign_id=campaign_id).first()
                ad_request.updateStatus('accepted')
                ad_request.pay = finalpay
                newacceptedadrequest = Accepted_ad_request.add(ad_request.campaign_id,ad_request.influencer_id,ad_request.message,ad_request.requirement,ad_request.pay)
                db.session.add(newacceptedadrequest)
                db.session.commit()
        except Exception as error:
              
            raise ValueError(error)

    def createAdRequest(self,message,requirement,pay,requested_by,requested_to,influencer_id,campaign_id):
        try:
        
            
            new_ad_request = Ad_request(
                message = message,
                requirement = requirement,
                pay = pay,
                status = 'pending',
                requested_by = requested_by,
                requested_to = requested_to,
                influencer = influencer_id,
                campaign = campaign_id
            )
            db.session.add(new_ad_request)
            db.session.commit()
            return {
                'campaign_id':new_ad_request.campaign_id,
                'influencer_id':new_ad_request.influencer_id
                }
        except Exception as error:
              
            raise ValueError(error)
    

    def getDetail(self,influencer_id,campaign_id):
    
        ad_request = Ad_request.query.filter_by(influencer_id=influencer_id,campaign_id=campaign_id).first()
        return {
            'influencer_id' : ad_request.influencer_id,
            'campaign_id' : ad_request.campaign_id,
            'message' : ad_request.message,
            'requirement' : ad_request.requirement,
            'pay' : ad_request.pay,
            'status':ad_request.status
        }


# This is completely seperated table jsut to store actve ads
# ad_completion_percentage = db.Enum('0','10','25','50','75','90','100',name='ad_completion_percentage')
class Accepted_ad_request(db.Model,UserMixin):
    ad_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key
    campaign_id = db.Column(db.Integer, nullable=False)
    influencer_id = db.Column(db.Integer, nullable=False)
    requirement = db.Column(db.String(25), nullable=False)
    message = db.Column(db.String(25), nullable=False)
    
    finalized_pay = db.Column(db.Integer, nullable=True)  # New column for finalized pay amount  
    ad_completion_percentage = db.Column(db.String(25), nullable=False)  # New column for working status

    def checkCompletionStatus(self,campaign_id,influencer_id):
        accepted_ad_request = Accepted_ad_request.query.filter_by(campaign_id=campaign_id,influencer_id=influencer_id).first()
        return accepted_ad_request.ad_completion_percentage
        
    def add (self,campaign_id,influencer_id,message,requirement,pay):
        try:          
            new_accepted_ad_request = Accepted_ad_request(
                campaign_id = campaign_id,
                influencer_id = influencer_id,
                message = message,
                requirement = requirement,
                finalized_pay = pay,
                ad_completion_percentage = '0'
            )
            db.session.add(new_accepted_ad_request)
            db.session.commit()
            return {
                'ad_id':new_accepted_ad_request.ad_id,
                'campaign_id':new_accepted_ad_request.campaign_id,
                'influencer_id':new_accepted_ad_request.influencer_id
                }
        except Exception as error:
              
            raise ValueError(error)
    def delete(self,campaign_id,influencer_id):
        try:
            
             
                accepted_ad_request = Accepted_ad_request.query.filter_by(campaign_id=campaign_id,influencer_id=influencer_id).first()
                if accepted_ad_request.checkCompletionStatus() == '100':
                    db.session.delete(accepted_ad_request)
                    db.session.commit()
                else:
                    raise ValueError('Campaign ads is not completed')
        except Exception as error:
              
            raise ValueError(error)

#MODEL CUSTOM FUNCTION

 #CREATING ROLES:
def createAllRole():
    role_instance = Roles()
    role_instance.createNewRole('influencer')
    role_instance.createNewRole('sponsor')
    role_instance.createNewRole('admin')

#CREATING ADMIN:
def createAdmin(name,username,password,email,phone_number,country,state,city,pin_code,address_description):
    user_instance = User()
    address_instance = Address()
    user_obj = user_instance.createUser(username,password,name,email,phone_number,'admin') 
    address_instance.addAddress(country,state,city,pin_code,address_description,user_obj['id'])
    db.session.commit()
    return user_obj['id']


#CREATING INFLUENCER:
def createInfluencer(name,username,password,email,phone_number,country,state,city,pin_code,address_description,category,niche,follower_count,following_count):
    user_instance = User()  
    address_instance = Address()
    influencer_instance = Influencer()
    user_obj = user_instance.createUser(username,password,name,email,phone_number,'influencer') 
    address_instance.addAddress(country,state,city,pin_code,address_description,user_obj['id'])
    influencer_instance.addInfluencer(username,category,niche,follower_count,following_count,user_obj['id'])
    db.session.commit()
    return user_obj['id']
  

#CREATING SPONSORS:
def createSponsor(name,username,password,email,phone_number,country,state,city,pin_code,address_description,industry,budget):
    user_instance = User()
    address_instance = Address()
    sponsor_instance = Sponsors()
    user_obj = user_instance.createUser(username,password,name,email,phone_number,'sponsor') 
    address_instance.addAddress(country,state,city,pin_code,address_description,user_obj['id'])
    sponsor_instance.addSponsor(industry,budget,user_obj['id'])
    db.session.commit()
    return user_obj['id']  

def createCampaign(campaign_name,description,goal,budget,start_date,end_date,visibilty,sponsor_id):
    campaign_instance = Campaign()
    sponsor_1 = Sponsors.query.filter_by(sponsors_id=sponsor_id).first()
    campaign_1 = Campaign(campaign_name=campaign_name,description=description,goal=goal,budget=budget,start_date=start_date,end_date=end_date,numberOfActiveAds=0, visibilty=visibilty,active=True,flagged=False,sponsors=sponsor_1)
    db.session.add_all([campaign_1])
    db.session.commit()
    return True

def createAdRequest(message,requirement,pay,requested_by,requested_to,influencer_id,campaign_id):
    ad_instance = Ad_request()
    influencer_1 = Influencer.query.filter_by(influencer_id=influencer_id).first()
    campaign_1 = Campaign.query.filter_by(campaign_id=campaign_id).first()
    ad_1 = Ad_request(message=message,requirement=requirement,pay=pay,status='pending',requested_by=requested_by,requested_to=requested_to,influencer=influencer_1,campaign=campaign_1)
    db.session.add(ad_1)
    db.session.commit()
    return True

