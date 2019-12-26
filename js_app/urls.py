from django.urls import path
from . import views
urlpatterns = [
    path('test1/',views.fn_js_ass),
    path('test2/',views.fn_js_ass2),
    path('eg1/',views.fn_js_eg1),
    path('eg_armstrong/',views.fn_js_eg_armstrong),
    path('ass1/',views.fn_js_ass1),
    path('ass2/',views.fn_js_ass2),
    path('ass3/',views.fn_js_ass3),
    path('ass4/',views.fn_js_ass4),
    path('ass5/',views.fn_js_ass5),
    path('ass6/',views.fn_js_ass6),
    path('ass7/',views.fn_js_ass7),
    path('ass8_1/',views.fn_js_ass8_1),
    path('ass8_2/',views.fn_js_ass8_2),
    path('ass8_1/',views.fn_js_ass8_1),
    path('ass9/',views.fn_js_ass9),
    path('ass10/',views.fn_js_ass10),
    path('ass11/',views.fn_js_ass11),
]

