from django.urls import path

from gogsiteapi_app.views import PlayerList, DeveloperList, DeveloperDetail

gogsiteapp_patterns = ((
                           path('players/', PlayerList.as_view()),
                           # path ('players/<int:pk>'),
                           path('developers/', DeveloperList.as_view()),
                           path ('developers/<int:pk>', DeveloperDetail.as_view()),

                       ), 'gogsiteapp')
