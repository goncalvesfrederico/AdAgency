from django.db import models
from api.utils.enum_options import ActivationStatus, Interesting, YesOrNo, Devices, ObjectiveOfTheCampaign, \
    AdFormat

class Branchs(models.Model):
    name = models.TextField(max_length=100, null=False, verbose_name="Branch Name")
    monthly_budget = models.FloatField(verbose_name="0.00", null=False)
    daily_budget = models.FloatField(verbose_name="0.00", null=False)
    pixel = models.TextField(max_length=150, verbose_name="Pixel ID", null=False)
    activated = models.CharField(
        max_length=10, 
        choices=ActivationStatus.choices, 
        default=ActivationStatus.ACTIVE,
        verbose_name="Activation Status",
        null=False
    )
    instagram = models.TextField(max_length=100, verbose_name="Instagram URL", null=False)
    facebook = models.TextField(max_length=100, verbose_name="Facebook URL", null=False)
    website = models.TextField(max_length=100, verbose_name="Website URL", null=False)

    def __str__(self):
        return self.name


class Audiences(models.Model):
    name = models.TextField(max_length=100, null=False, verbose_name="Audience Name")
    locations = models.TextField(max_length=50, null=False, default="United States")
    age = models.IntegerField(verbose_name="18", default=18)
    language = models.TextField(max_length=15, verbose_name="English", default="English")
    interest = models.CharField(
        max_length=15,
        choices=Interesting.choices,
        default=Interesting.ALL,
        verbose_name="Interest Options",
        null=False
    )
    activated = models.CharField(
        max_length=10,
        choices=ActivationStatus.choices,
        default=ActivationStatus.ACTIVE,
        verbose_name="Activation Status",
        null=False
    )

    def __str__(self):
        return self.name


class Positionings(models.Model):
    name = models.TextField(max_length=100, null=False, verbose_name="Audience Name")
    facebook = models.CharField(
        max_length=1,
        choices=YesOrNo.choices,
        default=YesOrNo.YES,
        verbose_name="Facebook Enabled",
        null=False
    )
    instagram = models.CharField(
        max_length=1,
        choices=YesOrNo.choices,
        default=YesOrNo.YES,
        verbose_name="Instagram Enabled",
        null=False
    )
    devices = models.CharField(
        max_length=10,
        choices=Devices.choices,
        default=Devices.ALL,
        verbose_name="Device Option",
        null=False
    )
    activated = models.CharField(
        max_length=10,
        choices=ActivationStatus.choices,
        default=ActivationStatus.ACTIVE,
        verbose_name="Activation Status",
        null=False
    )

    def __str__(self):
        return self.name


class Campaigns(models.Model):
    name = models.TextField(max_length=100, null=False, verbose_name="Campaign Name")
    activated = models.CharField(
        max_length=10,
        choices=ActivationStatus.choices,
        default=ActivationStatus.ACTIVE,
        verbose_name="Activation Status"
    )
    daily_budget = models.FloatField(verbose_name="0.00", null=False)
    dayparting = models.BooleanField(default=False, verbose_name="Dayparting Enabled")
    dayparting_hours = models.JSONField(blank=True, null=True, verbose_name="Dayparting Hours")
    objetive_of_the_compaign = models.CharField(
        max_length=10,
        choices=ObjectiveOfTheCampaign.choices,
        default=ObjectiveOfTheCampaign.SALES,
        verbose_name="Choose a campaign Objetve",
        null=False
    )
    branch_id = models.ForeignKey(
        Branchs, 
        on_delete=models.CASCADE, 
        verbose_name="Choose the Branch"
    )
    positioning_id = models.ForeignKey(
        Positionings, 
        on_delete=models.PROTECT, 
        verbose_name="Choose the Positions"
    )
    audience_id = models.ForeignKey(
        Audiences,
        on_delete=models.PROTECT,
        verbose_name="Choose the Audience"
    )

    def __str__(self):
        return self.name
    

class Ads(models.Model):
    name = models.TextField(max_length=100, null=False, verbose_name="Campaign Name")
    format = models.CharField(
        max_length=10,
        choices=AdFormat.choices,
        default=AdFormat.IMAGE,
        verbose_name="Choose the format",
        null=False
    )
    destination = models.TextField(max_length=200, null=False)
    activated = models.CharField(
        max_length=10,
        choices=ActivationStatus.choices,
        default=ActivationStatus.ACTIVE,
        verbose_name="Activation Status"
    )
    campaign_id = models.ForeignKey(
        Campaigns, 
        verbose_name="Choose the Campaign", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name