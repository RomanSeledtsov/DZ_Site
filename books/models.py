from django.db import models


class Books(models.Model):

    GENRE = (
        ('Романтика', 'Романтика'),
        ('Детектив', 'Детектив'),
        ('Фантастика', 'Фантастика'),
        ('Научная фантастика', 'Научная фантастика'),

    )

    name = models.CharField(max_length=100)
    email = models.EmailField(default='@gmail.com')
    image = models.ImageField(upload_to='images/')
    about_book = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.genre}'

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
