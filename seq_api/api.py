from tastypie.resources import ModelResource
from seq_api.models import Gene

class GeneResource(ModelResource):
  class Meta:
    queryset = Gene.objects.all()
    resource_name = 'gene'
