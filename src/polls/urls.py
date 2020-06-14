from django.urls import path
from polls.views import index, detail, results, vote

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('<int:id>/results/', results, name='results'),
    path('<int:id>/vote/', vote, name='vote'),
]
