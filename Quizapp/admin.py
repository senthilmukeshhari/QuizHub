from django.contrib import admin
from .models import NewUser,SportsQuestion,PlantsAndAnimalQuestion,ZoologyQuestion,HistoryQuestion,CurrentAffairsQuestion,Feedback,UserResult

# Register your models here.

class NewUserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name']

class SportsQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_no','question','correct_opt','related_img']

class PlantsAndAnimalQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_no','question','correct_opt','related_img']

class ZoologyQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_no','question','correct_opt','related_img']

class HistoryQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_no','question','correct_opt','related_img']

class CurrentAffairsQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_no','catagery','question','correct_opt','related_img']

class UserResultAdmin(admin.ModelAdmin):
    list_display = ['user_id','user_name','score']

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user_id','user_name','feedback']

admin.site.register(NewUser,NewUserAdmin)
admin.site.register(SportsQuestion,SportsQuestionAdmin)
admin.site.register(PlantsAndAnimalQuestion,PlantsAndAnimalQuestionAdmin)
admin.site.register(ZoologyQuestion,ZoologyQuestionAdmin)
admin.site.register(HistoryQuestion,HistoryQuestionAdmin)
admin.site.register(CurrentAffairsQuestion,CurrentAffairsQuestionAdmin)
admin.site.register(UserResult,UserResultAdmin)
admin.site.register(Feedback,FeedBackAdmin)