
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Additional teacher model fields

    def __str__(self):
        return self.user.username

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    quizzes_taken = models.ManyToManyField(Quiz, through='QuizResult')

    def __str__(self):
        return self.user.username

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} - {self.text}"

class QuizResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.user.username}'s result for {self.quiz.title}"
