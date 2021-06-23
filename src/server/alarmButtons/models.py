from django.db import models

# Create your models here.
class Button(models.Model):
    macAddr = models.CharField(max_length=30)
    buttonNum = models.IntegerField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return "%s:%s = %s" % (self.macAddr, self.buttonNum, self.status)

    class Meta:
        unique_together = ('macAddr', 'buttonNum')
class History(models.Model):
    macAddr = models.CharField(max_length=30)
    buttonNum = models.IntegerField()
    status = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s:%s => %s (%s)" % (self.macAddr, self.buttonNum, self.status, self.time.strftime('%m/%d/%Y'))
