from django.db import models


class WarrantyObligations(models.Model):
    general_provisions = models.TextField(blank=True, null=True)
    warranty_period = models.TextField(blank=True, null=True)
    execution_conditions = models.TextField(blank=True, null=True)
    cancellation_conditions = models.TextField(blank=True, null=True)
    list_types_work = models.TextField(blank=True, null=True)
    parking_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.general_provisions[:50]  # Возвращает первые 50 символов общего положения для отображения

    class Meta:
        db_table = "warranty_obligations"
