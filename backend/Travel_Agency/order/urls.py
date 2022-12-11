from django.urls import path
from .views import thanks, orderHistory, orderDetail

app_name = 'order'

urlpatterns = [
    path('thanks/<int:order_id>/', thanks, name='thanks'),
    path("history/", orderHistory.as_view(), name="order_history"),
    path("<int:order_id>/", orderDetail.as_view(), name="order_detail")
]
