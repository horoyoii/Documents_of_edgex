import graphene

from graphene_django.types import DjangoObjectType

from .models import *

from django.views.decorators.csrf import csrf_exempt

class DoneType(DjangoObjectType):
    class Meta:
        model = Done


class Query(object):
    done = graphene.Field(DoneType, id=graphene.Int(), title=graphene.String(), pubDate=graphene.String())
    
    all_dones = graphene.List(DoneType)

    
    def resolve_done(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('name')

        if id is not None:
            return Done.objects.get(pk=id)

        if title is not None:
            return Done.objects.get(title=title)
        
        return None

    
    def resolve_all_dones(self, info, **kwargs):
        print("Resolver called")
        return Done.objects.all()
