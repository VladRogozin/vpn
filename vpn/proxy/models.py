from django.db import models
from account.models import CustomUser


class Site(models.Model):
    user_site = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=255)


class VpnUsageStat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    page_transitions = models.IntegerField(default=0)
    data_volume_sent = models.BigIntegerField(default=0)
    data_volume_received = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.site_name}"
