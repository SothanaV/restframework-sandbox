from django.urls import path
from .views import snippet_list, snippet_detail, SnippetList, SnippetDetail, api_root, SnippetHighlight
from rest_framework.urlpatterns import format_suffix_patterns
from .api.viewsets import UserList, UserDetail 

# urlpatterns = [
#     ## function
#     # path('snippets/', snippet_list),
#     # path('snippets/<int:pk>/', snippet_detail),

#     # clase based
#     path('snippets/', SnippetList.as_view()),
#     path('snippets/<int:pk>/', SnippetDetail.as_view()),

#     path('users/',UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', api_root),
#     path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/',
        SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        UserDetail.as_view(),
        name='user-detail')
])