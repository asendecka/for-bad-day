from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Quote(models.Model):
    text = models.TextField(_("Quote"))
    is_ok = models.NullBooleanField(_("Is approved?"))
    added_on = models.DateTimeField(_("Added on"), default=timezone.now())

    def __unicode__(self):
        return self.text
