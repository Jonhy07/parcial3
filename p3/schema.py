import graphene
import proyecto.schema

class Query(proyecto.schema.Query, graphene.ObjectType):
    pass

class Mutation(proyecto.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)