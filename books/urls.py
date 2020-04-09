from django.urls import path
from .views import HomeListView, BookListView, book_detail_view, BookRandomView, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('novelty/', BookListView.as_view(), name='novelty'),
    path('detail/<int:pk>', book_detail_view, name='detail'),
    path('random/', BookRandomView.as_view(), name='random'),
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),
]