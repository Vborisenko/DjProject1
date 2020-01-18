from django.db import models


# Create your models here.
class Worker(models.Model):
    POSITION_SHOICE = (
        ('MANAGER', 'MANAGER'),
        ('developer', 'DEVELOPER'),
        ('teamlead', 'TEAMLEAD'),
        ('pm', 'PM'),
        ('hr', 'HR'),
    )
    f_name = models.CharField(max_length=50)
    s_name = models.CharField(max_length=50)
    position = models.CharField(max_length=10, choices=POSITION_SHOICE, default='developer')
    work_time = models.DecimalField(max_digits=1000, decimal_places=0)
    cost_in_hour = models.DecimalField(max_digits=1000, decimal_places=2)
    salary = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
