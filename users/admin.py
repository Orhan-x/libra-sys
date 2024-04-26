from django.contrib import admin
from .models import Registration, Book


admin.site.register(Registration)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','borrow_date', 'updated_at')
    fields = ('id', 'book_name','borrow_date', 'updated_at')
    readonly_fields = ('id','borrow_date', 'updated_at')
admin.site.register(Book, BookAdmin)


