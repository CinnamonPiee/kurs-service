from django.db import models


class WarrantyObligations(models.Model):
    general_provisions = models.TextField(blank=True, null=True, verbose_name="1. Общие положения")
    warranty_period = models.TextField(blank=True, null=True, verbose_name="2. Гарантийный срок")
    execution_conditions = models.TextField(blank=True, null=True, verbose_name="3. Условия выполнения гарантийных обязательств")
    cancellation_conditions = models.TextField(blank=True, null=True, verbose_name="4. Условия отказа в выполнении гарантийных обязательств")
    list_types_work = models.TextField(blank=True, null=True, verbose_name="5. Перечень видов работ и запчастей, на которые гарантия не распространяется:")
    parking_conditions = models.TextField(blank=True, null=True, verbose_name="6. Условия стоянки транспорта на территории сервиса ООО 'КУРС' по истечении ремонтных работ.")

    def __str__(self):
        return "Текст на странице Гарантия"

    class Meta:
        db_table: str = "warranty_obligations"
        verbose_name: str = "гарантию"
        verbose_name_plural: str = "Гарантии"
