from django.urls import path
from .views import HomeListView, BookListView, BookDetailView, BookRandomView, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('new/', BookListView.as_view(), name='new'),
    path('view/<int:pk>', BookDetailView.as_view(), name='read'),
    path('random/', BookRandomView.as_view(), name='random'),
    path('create/', BookCreate.as_view(), name='create'),
    path('edit/<int:pk>', BookUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),
]