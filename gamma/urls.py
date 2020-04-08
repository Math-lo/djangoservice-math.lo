from django.urls import path,re_path
from . import views

app_name = 'gamma'
urlpatterns = [
    path('', views.index, name='index'),
    path('generalGroupQuestionnaire/<int:id_group>/<int:id_cue>/', views.generalGroupQuestionnaire, name='generalGroupQuestionnaire'),
    path('questionnaireGradeGroup/<int:id_group>/<int:id_cue>/', views.questionnaireGradeGroup,name='questionnaireGradeGroup'),
    path('generalQuestionnaire/<int:id_cue>/', views.generalQuestionnaire, name='generalQuestionnaire'),
    path('questionnaireGrades/<int:id_cue>/', views.questionnaireGrades, name='questionnaireGrades'),
    path('generalGrades/', views.generalGrades, name='generalGrades'),
    path('generalColumnGroupTopic/<int:id_group>/', views.generalColumnGroupTopic, name='generalColumnGroupTopic'),
    path('generalColumnTopic/', views.generalColumnTopic, name='generalColumnTopic'),
    ##POR ALUMNO#####################
    path('questionnaireAlumno/<int:id_alumno>/<int:id_cue>/', views.questionnaireAlumno, name='questionnaireAlumno'),
    path('questionnairesAlumnoTopic/<int:id_alumno>/<int:id_tem>/', views.questionnairesAlumnoTopic, name='questionnairesAlumnoTopic'),
]