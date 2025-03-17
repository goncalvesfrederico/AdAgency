from django.core.management.base import BaseCommand
from django.utils.timezone import now
from api.models import Campaigns

class Command(BaseCommand):
    help = "Reset campaign budgets and reactivate campaigns at midnight"

    def handle(self, *args, **kwargs):
        today = now().date()
        campaigns = Campaigns.objects.all()
        for campaign in campaigns:
            campaign.daily_budget = 0.0
            campaign.activated = "active"
            campaign.save()

        self.stdout.write(f"{len(campaigns)} campaigns reset on {today}")
