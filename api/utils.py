from django.db import models

class ActivationStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"


class Interesting(models.TextChoices):
    CARS = "cars", "Cars"
    MOTORCYCLES = "motorcycles", "Motorcycles"
    TECNOLOGIES = "tecnologies", "Tecnologies"
    MEN = "men", "Men"
    WOMEN = "women", "Women"
    BOOKS = "books", "Books"
    ALL = "all", "All"


class YesOrNo(models.TextChoices):
    YES = "Y"
    NO = "N"


class Devices(models.TextChoices):
    MOBILES = "Mobile"
    PCS = "PCs"
    ALL = "All"


class ObjectiveOfTheCampaign(models.TextChoices):
    LEADS = "Leads"
    TRAFFIC = "Traffic"
    SALES = "Sales"


class AdFormat(models.TextChoices):
    VIDEO = "Video"
    IMAGE = "Image"