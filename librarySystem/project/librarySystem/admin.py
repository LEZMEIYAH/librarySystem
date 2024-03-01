from django.contrib import admin
from .models import Author, Book, Member, Loan, BookAuthor

class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline]

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline]

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'book', 'member', 'loandate', 'return_date')
    list_filter = ('book__title', 'member__name', 'loandate')
    search_fields = ('book__title', 'member__name')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Member)
admin.site.register(Loan, LoanAdmin)
