from django .urls import path
from task.views import add_task,show_task,details_task,edit_task,delete_task,complete_task,search

urlpatterns = [
    path('add_task/',add_task, name='add_task'),
    path('show_task/',show_task,name='show_task'),
    path('',search, name='find'),
    path('edit_task/<int:id>/', edit_task,name='edit_task'),
    path('delete_task/<int:id>/', delete_task,name='delete_task'),
    path('details_task/<int:id>/',details_task, name='details'),
    path('complete_task/<int:id>/',complete_task, name='status'),
]

