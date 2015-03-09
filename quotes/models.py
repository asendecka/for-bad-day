from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class ModeratedQuoteManager(models.Manager):
    def get_queryset(self):
        return super(ModeratedQuoteManager, self).get_queryset().filter(
                is_ok=True)


class Quote(models.Model):
    text = models.TextField(_("Quote"))
    is_ok = models.NullBooleanField(_("Is approved?"), null=True)
    added_on = models.DateTimeField(_("Added on"), default=timezone.now())

    objects = models.Manager()
    moderated = ModeratedQuoteManager()

    def __unicode__(self):
        return self.text
