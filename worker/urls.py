from .views import WorkersUnit, MakeVisit, WorkersDetail, UnitDetail, VisitDetail, WorkerList, WorkersApiView, VisitApiView
from django.urls import path

urlpatterns = [
    path("visit/api/<str:phone>/", VisitApiView.as_view(), name="visitapi"),
    path("worker/api/<str:phone>/", WorkersApiView.as_view(), name="workerapi"),
    path("units/", WorkersUnit.as_view(), name="units"),
    path("visits/", MakeVisit.as_view(), name="visits"),
    path("workers/", WorkerList.as_view(), name="workers"),
    path("worker/<int:pk>/", WorkersDetail.as_view(), name="worker" ),
    path("unit/<int:pk>/", UnitDetail.as_view(), name="unit"),
    path("visit/<int:pk>/", VisitDetail.as_view(), name="visit")
]
