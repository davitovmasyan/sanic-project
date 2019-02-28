import sqlalchemy


metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    'books',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String(length=100)),
    sqlalchemy.Column('author', sqlalchemy.String(length=60)),
)
