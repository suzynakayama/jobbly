from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/team', views.team, name='team'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),
    path('accounts/index/', views.index, name='index'),
    path('accounts/delete/', views.delete, name='account_delete'),
    path('accounts/confirm_delete/', views.confirm_delete, name='account_confirm_delete'),
    path('applications/', views.application, name='application'),
    path('applications/<int:application_id>/', views.applications_detail, name='applications_detail'),
    path('applications/create/', views.ApplicationCreate.as_view(), name='applications_create'),
    path('applications/create_from_search/', views.application_create_from_search, name='application_create_from_search'),
    path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name='applications_update'),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='applications_delete'),
    path('applications/<int:application_id>/add_landmarks/', views.add_landmark, name='add_landmark'),
    path('applications/<int:application_id>/add_contacts/', views.add_contact, name='add_contact'),
    path('applications/<int:application_id>/remove_resume/', views.remove_resume, name='remove_resume'),
    path('contacts/index/', views.contacts_index, name='contacts_index'),
    path('contacts/create/', views.ContactCreate.as_view(), name='contacts_create'),
    path('contacts/<int:pk>/update/', views.ContactUpdate.as_view(), name='contacts_update'),
    path('contacts/<int:pk>/delete/', views.ContactDelete.as_view(), name='contacts_delete'),
    path('landmarks/<int:pk>/update/', views.LandmarkUpdate.as_view(), name='landmarks_update'),
    path('landmarks/<int:pk>/delete/', views.LandmarkDelete.as_view(), name='landmarks_delete'),
    path('landmarks/<int:landmark_id>/assoc_app/<int:application_id>/', views.assoc_landmark, name='assoc_landmark'),
    path('landmarks/<int:landmark_id>/unassoc_app/<int:application_id>/', views.unassoc_landmark, name='unassoc_landmark'),
    path('ajax/jobsearch/', views.job_search, name='job_search'),
    path('ajax/job_search_api/', views.job_search_api, name='job_search_api'),
    path('ajax/get_calendar/', views.get_calendar, name='get_calendar'),
    path('calendar/', views.calendar, name='calendar'),
    path('ajax/get_contacts/', views.get_contacts, name='get_contacts'),
]