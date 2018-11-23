import ast
from app.exceptions import MatrixParsingError


class FormattingMixin:

    @staticmethod
    def create_matrix(body: str) -> list:
        try:
            matrix = []
            for item in body.split(';'):
                stripped = item.strip(' []')

                if stripped:
                    matrix.append(ast.literal_eval(stripped))
        except Exception as err:
            raise MatrixParsingError()

        return matrix

    @staticmethod
    def wrap_response(clusters) -> str:
        response = '[\n'
        for cl_key, cl_points in clusters.items():
            for point in cl_points:
                response += ', '.join(map(str, [*point, cl_key])) + ';\n'

        response += ']'

        return response
