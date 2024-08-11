version = 'v1'
base_url = f'/app/{version}'

def custom_url_for(route):
    return f"{base_url}/{route}"
def update_url_for(base,route):
    return f"{base}/{route}"



#LOGIN AND SIGNUP ROUTE MANAGEMENT
home_url = base_url
register_home_url = custom_url_for('register')
admin_signUp_url = custom_url_for('signup/admin')
influencer_signUp_url = custom_url_for('signup/influencer')
influencer_platform_signUp_url = custom_url_for('signup/influencer-platform')
sponsor_signUp_url = custom_url_for('signup/sponsor')
sign_in_url = custom_url_for('signin')

#SPONSOR ROUTE MANAGEMENT
sponsor_base_url = custom_url_for('dashboard/sponsor')
sponsor_profile = update_url_for(sponsor_base_url,'profile')
sponsor_campiagn = update_url_for(sponsor_base_url,'campaign')
sponsor_influencer= update_url_for(sponsor_base_url,'influencer')
sponsor_searched_influencer= update_url_for(sponsor_base_url,'influencer/search')
sponsor_create_campaign = update_url_for(sponsor_base_url,'createCampaign')
sponsor_upadte_campaign = update_url_for(sponsor_base_url,'updateCampaign')
sponsor_delete_campaign = update_url_for(sponsor_base_url,'deleteCampaign')


sponsor_create_ad_request = update_url_for(sponsor_base_url,'createAdRequest')


#INFLUENCER ROUTE MANAGEMENT
influencer_base_url = custom_url_for('dashboard/influencer')
influencer_profile = update_url_for(influencer_base_url,'profile')
influencer_campiagn = update_url_for(influencer_base_url,'campaign')
influencer_sponsor= update_url_for(influencer_base_url,'sponsor')

#ADMIN ROUTE MANAGEMENT
admin_base_url = custom_url_for('dashboard/admin')
admin_profile = update_url_for(admin_base_url,'profile')
admin_campiagn = update_url_for(admin_base_url,'campaign')
admin_influencer= update_url_for(admin_base_url,'influencer')
admin_sponsor= update_url_for(admin_base_url,'sponsor')





