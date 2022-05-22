from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
	path( 'notes/', views.NoteView.as_view() ),
	path( 'notes/<int:pk>/', views.NoteView.as_view() ),

	path( 'routes/', views.GetRoutes.as_view() ),
]