from sanic.response import json

from project.tables import books


def setup_routes(app):
    @app.route("/books")
    async def book_list(request):
        query = books.select()
        rows = await app.db.fetch_all(query)
        return json({
            'books': [{row['title']: row['author']} for row in rows]
        })
