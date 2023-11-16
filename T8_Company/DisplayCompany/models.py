from django.db import models
from django.core.validators import MinValueValidator

class Errors(models.Model):
    ErrorID = models.AutoField(primary_key=True)
    ErrorCode = models.CharField(max_length=10)
    Description = models.CharField(max_length=250)
    DateReceived = models.DateField()
    ErrorLevel = models.CharField(max_length=9, choices=[('Критична', 'критична'), ('Важлива', 'важлива'), ('Незначна', 'незначна')])
    FunctionalityCategory = models.CharField(max_length=30, choices=[('Інтерфейс', 'інтерфейс'), ('Дані', 'дані'), ('Розрахунковий алгоритм', 'розрахунковий алгоритм'), ('Інше', 'інше'), ('Невідома категорія', 'невідома категорія')])
    Source = models.CharField(max_length=20, choices=[('Користувач', 'користувач'), ('Тестувальник', 'тестувальник')])

    def __str__(self):
        return self.ErrorCode

    class Meta:
        verbose_name = 'Помилка'
        verbose_name_plural = 'Помилки'


class Programmers(models.Model):
    ProgrammerID = models.AutoField(primary_key=True)
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=13)

    def __str__(self):
        return self.Surname

    class Meta:
        verbose_name = 'Програміст'
        verbose_name_plural = 'Програмісти'


class BugFixes(models.Model):
    FixID = models.AutoField(primary_key=True)
    ErrorCode = models.ForeignKey(Errors, on_delete=models.CASCADE)
    StartDate = models.DateField()
    FixDurationDay = models.IntegerField(validators=[MinValueValidator(1)])
    ProgrammerCode = models.ForeignKey(Programmers, on_delete=models.CASCADE)
    WorkCostPerDay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.StartDate)

    class Meta:
        verbose_name = 'Виправленна помилка'
        verbose_name_plural = 'Виправленні помилки'
