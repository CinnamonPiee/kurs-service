from django.db import models



class Warranty180(models.Model):
    img = models.ImageField(upload_to="big_png_with_text", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return "Текст на странице - Гарантии - гарантия до 180 дней"

    class Meta:
        db_table = "warranty_180"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Гарантия до 180 дней"


class WarrantyObligations(models.Model):
    general_provisions = models.TextField(blank=True, null=True, 
    verbose_name="1. Общие положения")
    warranty_period = models.TextField(blank=True, null=True, 
    verbose_name="2. Гарантийный срок")
    execution_conditions = models.TextField(blank=True, null=True, 
    verbose_name="3. Условия выполнения гарантийных обязательств")
    cancellation_conditions = models.TextField(blank=True, null=True, 
    verbose_name="4. Условия отказа в выполнении гарантийных обязательств")
    list_types_work = models.TextField(blank=True, null=True, 
    verbose_name="5. Перечень видов работ и запчастей, на которые гарантия не распространяется:")
    parking_conditions = models.TextField(blank=True, null=True, 
    verbose_name="6. Условия стоянки транспорта на территории сервиса ООО 'КУРС' по истечении ремонтных работ.")

    def __str__(self):
        return f"Текст на странице - Гарантии - Гарантии"

    class Meta:
        db_table = "warranty_obligations"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Гарантии"
        

class WarrantyHeaders(models.Model):
    warranty = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок1")
    

    def __str__(self):
        return "Текст"

    class Meta:
        db_table = "warranty_headers"
        verbose_name: str = "заголовок"
        verbose_name_plural: str = "Заголовки"
