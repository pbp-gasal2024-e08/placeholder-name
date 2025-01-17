from django.urls import path
from .views import (
    create_announcement_ajax,
    delete_announcement,
    edit_announcement,
    get_announcement_by_id,
    get_announcements_by_store,
    create_announcement_flutter,
    edit_announcement_flutter,
    delete_announcement_flutter,
    get_announcements_flutter,
    is_merchant_flutter
)

app_name = "announcement"

urlpatterns = [
    path("get-flutter/", get_announcements_flutter, name="get_announcements_flutter"),
    path("is-merchant-flutter/", is_merchant_flutter, name="is_merchant_flutter"),
    path('create-flutter/', create_announcement_flutter, name='create_announcement_flutter'),
    path("edit-flutter/<uuid:id>", edit_announcement_flutter, name="edit_announcement_flutter"),
    path("delete-flutter/<uuid:id>", delete_announcement_flutter, name="delete_announcement_flutter"),
    path("create", create_announcement_ajax, name="create_announcement_ajax"),
    path(
        "store/<int:store_id>",
        get_announcements_by_store,
        name="get_announcements_by_store",
    ),
    path("edit/<uuid:id>", edit_announcement, name="edit_announcement"),
    path("delete/<uuid:id>", delete_announcement, name="delete_announcement"),
    # path("<str:id>", get_announcement_by_id, name="get_announcement_by_id"),
]
