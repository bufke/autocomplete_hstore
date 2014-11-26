from django.db import models
from django_hstore import hstore


class Foobar(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class SomethingWithSchema(models.Model):
    foobar = models.ForeignKey(Foobar, blank=True, null=True)
    data = hstore.DictionaryField(schema=[
        {
            'name': 'number',
            'class': 'IntegerField',
            'kwargs': {
                'default': 0
            }
        },
    ])

