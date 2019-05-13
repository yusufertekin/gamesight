from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()


#class Churn7(models.Model):
#
#    def upload_from_excel(self):
#        pass
#
#    def upload_from_csv(self):
#        pass
#
#class Churn9(models.Model):
#    pass
