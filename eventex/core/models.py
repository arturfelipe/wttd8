# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    KINDS = (
        ('E', _('E-mail')),
        ('P', _('Telefone')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_('Palestrante'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('Valor'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField(_(u'Título'), max_length=255)
    description = models.TextField(_(u'Descrição'))
    start_time = models.TimeField(_(u'Hora início'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'Palestrantes'))

    def __unicode__(self):
        return self.title
