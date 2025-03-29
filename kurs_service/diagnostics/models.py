from django.db import models

class DiagnosticsBlocksText(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Блок диагностики"

    class Meta:
        db_table = "diagnostics_blocks_text"


class DiagnosticMethods(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    description_text = models.TextField(blank=True, null=True)
    services_data = models.IntegerField(blank=True, null=True)
    title_data_modal = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Метод диагностики"

    class Meta:
        db_table = "diagnostic_methods"
