from django.urls import path

from gogsiteapi_app.views import PlayerView

gogsiteapp_patterns = ((
                           path('players/', PlayerView.as_view()),
                           # path ('player/<int:pk>',)

                       ), 'gogsiteapp')
