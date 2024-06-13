from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class MyBooks(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=200)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'вашу книгу'
        verbose_name_plural = 'Книги с тегами'


class Books(models.Model):
    GENRE = (
        ('Романтика', 'Романтика'),
        ('Детектив', 'Детектив'),
        ('Фантастика', 'Фантастика'),
        ('Научная фантастика', 'Научная фантастика'),

    )

    name = models.CharField(max_length=100, verbose_name='Имя книги', null=True)
    email = models.EmailField(default='@gmail.com', verbose_name='Укажите email', blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите обложку книги', null=True)
    about_book = models.TextField(verbose_name='О книге', null=True)
    genre = models.CharField(max_length=20, choices=GENRE, verbose_name='Укажите жанр книги', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.genre}'

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Все книги'


class ReviewBooks(models.Model):
    reviews_book = models.ForeignKey(Books, on_delete=models.CASCADE,
                                     related_name='reviews_books')
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars} - {self.reviews_book}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
