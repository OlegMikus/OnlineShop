from django.db import models
from PIL import Image


class Author(models.Model):
    full_name = models.CharField(max_length=152, blank=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50, blank=True)
    biography = models.TextField()
    age = models.IntegerField()
    is_alive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.full_name = self.last_name + ' ' + self.first_name + ' ' + self.fathers_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='book_picture')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        output_size = (800, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)
