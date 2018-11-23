import ast

from aiohttp import web

from app.clustering import (
    KMeans, DEFAULT_N_CLUSTERS, DEFAULT_MAX_ITERATIONS
)
from app.exceptions import ApplicationError, MatrixParsingError


class Clusterize(web.View):

    @staticmethod
    async def create_matrix(body: str) -> list:
        try:
            matrix = []

            for item in body.split(';'):
                stripped = item.strip(' []')
                matrix.append(ast.literal_eval(stripped))
        except Exception as err:
            raise MatrixParsingError()

        return matrix

    @staticmethod
    async def wrap_response(clusters) -> str:

        return str(clusters)

    async def post(self) -> web.Response:

        body = await self.request.text()
        try:
            matrix = await self.create_matrix(body)
            n_clusters = int(self.request.query.get(
                'n_clusters', DEFAULT_N_CLUSTERS))
            max_iterations = int(self.request.query.get(
                'max_iterations', DEFAULT_MAX_ITERATIONS))

            model = KMeans(n_clusters, max_iterations)

            clusters = await self.request.loop.run_in_executor(
                None, model.fit_predict, matrix)

            clusters_matrix_str = await self.wrap_response(clusters)

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
            body=clusters_matrix_str,
            status=200
        )