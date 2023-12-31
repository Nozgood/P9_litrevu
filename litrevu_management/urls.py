"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
import litrevu_management.views as views

app_name = "litrevu"

urlpatterns = [
    path('', views.home, name='home'),
    path('review/ticket/create/', views.create_ticket, name='create_ticket'),
    path('review/ticket/update/<int:ticket_id>', views.create_ticket,
         name='update_ticket'),
    path('review/ticket/delete/<int:ticket_id>', views.delete_ticket,
         name='delete_ticket'),
    path('review/create/', views.create_review, name='create_review'),
    path('review/create/<int:ticket_id>', views.create_review_from_ticket,
         name='create_review_from_ticket'),
    path('review/update/<int:review_id>', views.update_review,
         name='update_review'),
    path('review/delete/<int:review_id>', views.delete_review,
         name='delete_review'),
    path('posts/', views.posts, name='posts'),
]
