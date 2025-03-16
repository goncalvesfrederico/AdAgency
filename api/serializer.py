from rest_framework import serializers
from .models import Branchs, Audiences, Positionings, Campaigns, Ads

class BranchsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branchs
        fields = "__all__"


class AudiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiences
        fields = "__all__"


class PositioningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positionings
        fields = "__all__"


class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = "__all__"


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"