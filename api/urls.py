from django.urls import path
from .views import get_branchs, create_branch, branch_detail, get_audiences, create_audience, \
    audience_detail, get_positionings, create_positioning, positioning_detail, get_campaigns, \
    create_campaign, campaign_detail, get_ads, create_ad, ad_detail

urlpatterns = [
    # BRANCHS
    path('branchs/', get_branchs, name="get_branchs"),
    path('branchs/create/', create_branch, name="create_branch"),
    path('branchs/<int:pk>', branch_detail, name="branch_detail"),
    # AUDIENCES
    path('audiences/', get_audiences, name="get_audiences"),
    path('audiences/create/', create_audience, name="create_audience"),
    path('audiences/<int:pk>', audience_detail, name="audience_detail"),
    # POSITIONINGS
    path('positionings/', get_positionings, name="get_positionings"),
    path('positionings/create/', create_positioning, name="create_positioning"),
    path('positionings/<int:pk>', positioning_detail, name="positioning_detail"),
    # CAMPAIGNS
    path('campaigns/', get_campaigns, name="get_campaigns"),
    path('campaigns/create/', create_campaign, name="create_campaign"),
    path('campaigns/<int:pk>', campaign_detail, name="campaign_detail"),
    # ADS
    path('ads/', get_ads, name="get_ads"),
    path('ads/create/', create_ad, name="create_ad"),
    path('ads/<int:pk>', ad_detail, name="ad_detail"),
]
