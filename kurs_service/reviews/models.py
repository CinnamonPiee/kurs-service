from django.db import models
from base_page.models import SiteVisitor


class ReviewsReview(models.Model):
    user = models.ForeignKey(
        SiteVisitor,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="reviews"
    )
    content = models.TextField(verbose_name="Отзыв")
    image = models.ImageField(upload_to="reviews/", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    has_response = models.BooleanField(default=False, verbose_name="Есть ответ")
    response = models.OneToOneField(
        "ReviewsResponse",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Ответ на отзыв",
        related_name="review"
    )

    def __str__(self):
        return f"{self.user.first_name} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {self.has_response}"

    class Meta:
        db_table = "reviews_review"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class ReviewsResponse(models.Model):
    img = models.ImageField(default="img-logo/sport-car-auto", blank=True, null=True, verbose_name="Изображение")
    content = models.TextField(verbose_name="Ответ на отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Ответ от {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        db_table = "reviews_response"
        verbose_name = "Ответ на отзыв"
        verbose_name_plural = "Ответы на отзывы"


class ReviewsTitles(models.Model):
	visitor_reviews = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отзывы посетителей")
	leave_a_review_or_request = models.CharField(max_length=255, blank=True, null=True, verbose_name="Оставить отзыв или запросить обратный звонок")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "reviews_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
