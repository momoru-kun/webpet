from webpet.routers import HTTPRouter, URL
import views

# Define router
router = HTTPRouter(routes=[
    URL('/', views.Index),
    URL('/exception', views.TestRaise),
    URL('/longpool', views.TestLong)
])