from django.contrib import admin

from books.models import Book, Category, Author


@admin.action(description='Unavailable for now')
def now_unavailable(modeladmin, request, queryset):
    queryset.update(available=False)


@admin.action(description='Now available')
def now_available(modeladmin, request, queryset):
    queryset.update(available=True)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'is_alive',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'category', 'author', 'price', 'available')
    list_filter = ('author', 'category',)
    actions = [now_available, now_unavailable]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
