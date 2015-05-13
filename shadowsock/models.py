from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s<%s %s %s %s>' % (self.name,self.imei,self.email,self.create_at,self.deadline)
class account(models.Model):
    name = models.CharField(max_length=100)
    proxy = models.CharField(max_length=100)
    sitekey = models.CharField(max_length=100)
    encMethod = models.CharField(max_length=100)
    remotePort = models.CharField(max_length=100)
    localPort = models.CharField(max_length=100)
    def __str__(self):
        return '%s<%s %s %s %s %s>' % (self.name,self.proxy,self.sitekey,self.encMethod,self.remotePort,self.localPort)
    