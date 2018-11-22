from .views import clusterize


app_routes = [
    ('POST', '/clustering/labels', clusterize),
]
