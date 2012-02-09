from tastypie.utils import now
from django.contrib.auth.models import User
from django.db import models # this was the only default in this file
from django.template.defaultfilters import slugify

class Gene(models.Model):
  # I think these are safe to comment out
#  user = models.ForeignKey(User)
#  pub_date = models.DateTimeField(default=now)
  name = models.CharField(max_length=100)
  sequence = models.CharField(max_length=100000)
  chromosome = models.CharField(max_length=10)
  slug = models.SlugField()

  def __unicode__(self):
    return self.title

  def save(self, *args, **kwargs):
    # For automatic slug generation.
    if not self.slug:
      self.slug = slugify(self.title)[:50]

    return super(Entry, self).save(*args, **kwargs)







