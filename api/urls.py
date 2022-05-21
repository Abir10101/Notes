from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
	path( 'notes/', views.getNotes, name="notes" ),
	path( 'notes/<int:pk>/view', views.getSingleNote, name="single_note" ),
	path( 'notes/create', views.createNote, name="create_note" ),
	path( 'notes/<int:pk>/update', views.updateNote, name="update_note" ),
	path( 'notes/<int:pk>/delete', views.deleteNote, name="delete_note" ),

	path( 'routes/', views.getRoutes, name="routes" ),
]

# Redirect Routes
urlpatterns += [
	path( '', RedirectView.as_view( url="notes/", permanent=True ) )		
]