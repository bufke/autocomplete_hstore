import autocomplete_light
from .models import Foobar

autocomplete_light.register(Foobar,
    search_fields = ['name']
                            )
