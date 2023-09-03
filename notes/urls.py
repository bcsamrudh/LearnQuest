from django.urls import path
from . import views

urlpatterns = [
    path("upload_notes",views.upload_notes,name="upload_notes"),
    path("notes/<int:search>",views.notes,name="notes"),
    path("note/<str:slug>",views.note,name="note"),
    path("delete_notes/<str:slug>",views.delete_notes,name="delete_notes"),
    # path("edit/<str:slug>",views.update_notes,name="edit_notes"),
    path("upvote/<int:id>",views.upvote,name="upvote"),
    path("generate_questions/<str:topic>/<str:subject>",views.generate_questions,name="generate_questions"),
]