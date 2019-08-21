import graphene

import documents.schema

class Query(documents.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
