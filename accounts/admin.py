# admin.py

from django.contrib import admin
from .models import Quiz, Question, Answer, Student, Teacher, QuizResult,CustomUser

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(QuizResult)
admin.site.register(CustomUser)
