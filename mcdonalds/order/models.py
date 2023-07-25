from django.db import models


class Order(models.Model):
    CREATED_STATUS = 'Created'
    READY_STATUS = 'Ready'
    COMPLETED_STATUS = 'Completed'
    ARCHIVED_STATUS = 'Archived'

    CHECK_STATUSES = [
        (CREATED_STATUS, 'Created'),
        (READY_STATUS, 'Ready'),
        (COMPLETED_STATUS, 'Completed'),
        (ARCHIVED_STATUS, 'Archived')
    ]

    type = models.CharField(max_length=100, choices=CHECK_STATUSES)
    order_number = models.IntegerField()
    
    
    
