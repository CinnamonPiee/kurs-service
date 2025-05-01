from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class SiteVisitor(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    password = models.CharField(max_length=128, verbose_name="Пароль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Последний вход")
    is_frequent = models.BooleanField(default=False, verbose_name="Частый клиент")
    visit_count = models.PositiveIntegerField(default=0, verbose_name="Количество посещений")
    notes = models.TextField(blank=True, null=True, verbose_name="Заметки")

    def set_password(self, raw_password):
        """Устанавливает хэшированный пароль."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Проверяет, соответствует ли пароль хэшу."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.first_name + " " + self.last_name}" if self.first_name else self.email

    class Meta:
        db_table = "base_page_site_visitor"
        verbose_name = "Посетитель сайта"
        verbose_name_plural = "Посетители сайта"
