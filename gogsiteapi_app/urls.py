from django.urls import path

from gogsiteapi_app.views import (
    PlayerList, PlayerDetail,
    DeveloperList, DeveloperDetail,
    PostList, PostDetail
)

gogsiteapp_patterns = ((
                           path('players/', PlayerList.as_view()),
                           path('players/<int:pk>', PlayerDetail.as_view()),
                           path('developers/', DeveloperList.as_view()),
                           path('developers/<int:pk>', DeveloperDetail.as_view()),
                           path('posts/', PostList.as_view()),
                           path('posts/<int:pk>', PostDetail.as_view()),
                       ), 'gogsiteapp')
