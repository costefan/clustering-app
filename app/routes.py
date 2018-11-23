from .views import Clusterize


app_routes = [
    ('POST', '/clustering/labels', Clusterize),
]
