from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Branchs, Audiences, Positionings, Campaigns, Ads
from .serializer import BranchsSerializer, AudiencesSerializer, PositioningsSerializer, \
    CampaignsSerializer, AdsSerializer

# BRANCHS
@api_view(['GET'])
def get_branchs(request):
    branchs = Branchs.objects.all()
    serializer = BranchsSerializer(branchs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_branch(request):
    serializer = BranchsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def branch_detail(request, pk):
    try:
        branch = Branchs.objects.get(pk=pk)
    except Branchs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BranchsSerializer(branch)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = BranchsSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# AUDIENCES 
@api_view(['GET'])
def get_audiences(request):
    audiences = Audiences.objects.all()
    serializer = AudiencesSerializer(audiences, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_audience(request):
    serializer = AudiencesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def audience_detail(request, pk):
    try:
        audience = Audiences.objects.get(pk=pk)
    except Audiences.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AudiencesSerializer(audience)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = AudiencesSerializer(audience, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        audience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# POSITIONINGS
@api_view(['GET'])
def get_positionings(request):
    positionings = Positionings.objects.all()
    serielizer = PositioningsSerializer(positionings, many=True)
    return Response(serielizer.data)

@api_view(['POST'])
def create_positioning(request):
    serializer = PositioningsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def positioning_detail(request, pk):
    try:
        positioning = Positionings.objects.get(pk=pk)
    except Positionings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PositioningsSerializer(positioning)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = PositioningsSerializer(positioning, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        positioning.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CAMPAIGNS
@api_view(['GET'])
def get_campaigns(request):
    campaigns = Campaigns.objects.all()
    serializer = CampaignsSerializer(campaigns, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_campaign(request):
    serializer = CampaignsSerializer(data=request.data)
    if serializer.is_valid():
        try:
            branch_id = request.data.get("branch_id")
            positioning_id = request.data.get("positioning_id")
            audience_id = request.data.get("audience_id")
            branch = Branchs.objects.get(pk=branch_id)
            positioning = Positionings.objects.get(pk=positioning_id)
            audience = Audiences.objects.get(pk=audience_id)
            
            if branch.activated == "active" and positioning.activated == "active" \
                and audience.activated == "active":
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Cannot create a Campaign for an inactive branch, or positioning or audience"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        
        except Branchs.DoesNotExist:
            return Response({"error": "Branch not found!"}, \
                            status=status.HTTP_404_NOT_FOUND)
        except Positionings.DoesNotExist:
            return Response({"error": "Positioning not found!"}, \
                            status=status.HTTP_404_NOT_FOUND)
        except Audiences.DoesNotExist:
            return Response({"error": "Audiences not found!"}, \
                            status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def campaign_detail(request, pk):
    try:
        campaign = Campaigns.objects.get(pk=pk)
    except Campaigns.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CampaignsSerializer(campaign)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = CampaignsSerializer(campaign, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                branch_id = request.data.get("branch_id")
                positioning_id = request.data.get("positioning_id")
                audience_id = request.data.get("audience_id")
                daily_budget_data = request.data.get("daily_budget")

                branch = Branchs.objects.get(pk=branch_id) if branch_id else campaign.branch_id
                positioning = Positionings.objects.get(pk=positioning_id) if positioning_id \
                    else campaign.positioning_id
                audience = Audiences.objects.get(pk=audience_id) if audience_id \
                    else campaign.audience_id
                daily_budget = daily_budget_data if daily_budget_data else campaign.daily_budget

                message = "Campaign updated successfully."

                # Check if campaign should be deactivated based on daily_budget
                if daily_budget is not None and \
                    (daily_budget >= branch.daily_budget \
                     or daily_budget >= branch.monthly_budget):
                    campaign.activated = "inactive"
                    campaign.daily_budget = daily_budget
                    message = (
                        f"Warning: The daily budget of {daily_budget} has hit or exceeded the limit "
                        f"({branch.daily_budget} daily / {branch.monthly_budget} monthly). "
                        "The campaign has been inactive."
                    )

                if branch.activated == "active" and positioning.activated == "active" \
                    and audience.activated == "active":
                    campaign.branch_id = branch
                    campaign.positioning_id = positioning
                    campaign.audience_id = audience
                    serializer.save()
                    
                    content = {
                        "message": message,
                        "campaing": serializer.data
                    }
                    return Response(content, status=status.HTTP_201_CREATED)
                else:
                    return Response(
                        {"error": "Cannot update a Campaign for an inactive branch, or positioning or audience"},
                        status=status.HTTP_406_NOT_ACCEPTABLE
                    )
            except Branchs.DoesNotExist:
                return Response({"error": "Branch not found!"}, \
                                status=status.HTTP_404_NOT_FOUND)
            except Positionings.DoesNotExist:
                return Response({"error": "Positioning not found!"}, \
                                status=status.HTTP_404_NOT_FOUND)
            except Audiences.DoesNotExist:
                return Response({"error": "Audiences not found!"}, \
                                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ADS
@api_view(['GET'])
def get_ads(request):
    ads = Ads.objects.all()
    serializer = AdsSerializer(ads, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_ad(request):
    serializer = AdsSerializer(data=request.data)
    if serializer.is_valid():
        try:
            campaign_id = request.data.get("campaign_id")
            campaign = Campaigns.objects.get(pk=campaign_id)
            
            if campaign.activated == "active":
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Cannot create an Ad for an inactive campaign"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        
        except Campaigns.DoesNotExist:
            return Response({"error": "Campaign not found!"}, \
                            status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def ad_detail(request, pk):
    try:
        ad = Ads.objects.get(pk=pk)
    except Ads.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AdsSerializer(ad)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = AdsSerializer(ad, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                campaign_id = request.data.get("campaign_id")
                campaign = Campaigns.objects.get(pk=campaign_id) if campaign_id else ad.campaign_id
                
                message = "Ad updated successfully."

                if campaign.activated == "active":
                    ad.campaign_id = campaign
                    serializer.save()
                    
                    content = {
                        "message": message,
                        "ad": serializer.data
                    }
                    return Response(content, status=status.HTTP_201_CREATED)
                else:
                    return Response(
                        {"error": "Cannot update a Ad for an inactive campaign"},
                        status=status.HTTP_406_NOT_ACCEPTABLE
                    )
            except Campaigns.DoesNotExist:
                return Response({"error": "Campaign not found!"}, \
                                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)