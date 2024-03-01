from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    authors = models.ManyToManyField(Author, through='BookAuthor')

    def __str__(self):
        return self.title

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loandate = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"Loan {self.loan_id}"

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.author.name}"
