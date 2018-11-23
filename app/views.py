from aiohttp import web

from app.clustering import (
    KMeans, DEFAULT_N_CLUSTERS, DEFAULT_MAX_ITERATIONS
)
from app.exceptions import ApplicationError
from app.mixins import FormattingMixin


class Clusterize(web.View, FormattingMixin):

    async def post(self) -> web.Response:

        body = await self.request.text()
        try:
            matrix = self.create_matrix(body)

            n_clusters = int(self.request.query.get(
                'n_clusters', DEFAULT_N_CLUSTERS))
            max_iterations = int(self.request.query.get(
                'max_iterations', DEFAULT_MAX_ITERATIONS))

            model = KMeans(n_clusters, max_iterations)

            clusters = await self.request.loop.run_in_executor(
                None, model.fit_predict, matrix)
            res = self.wrap_response(clusters)

        except ApplicationError as err:
            return web.Response(
                body=err.msg,
                status=400)
        except Exception as err:
            return web.Response(
                body=str(err),
                status=400
            )

        return web.Response(
            body=res,
            status=200)
