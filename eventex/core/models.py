# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    class Meta:
        verbose_name = _('Palestrante')
        verbose_name_plural = _('Palestrantes')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})

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

    class Meta:
        verbose_name = _('Contato')
        verbose_name_plural = _('Contatos')

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField(_(u'Título'), max_length=255)
    description = models.TextField(_(u'Descrição'))
    start_time = models.TimeField(_(u'Hora início'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'Palestrantes'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _('Palestra')
        verbose_name_plural = _('Palestras')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/palestras/%d/' % self.pk

class Course(Talk):
    slots = models.IntegerField(_('Slots'))
    notes = models.TextField(_('Notas'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

class Media(models.Model):
    MEDIAS = (
        ('YT', _('YouTube')),
        ('SL', _('SlideShare')),
    )

    talk = models.ForeignKey('Talk', verbose_name=_('Palestra'))
    title = models.CharField(_(u'Título'), max_length=255)
    kind = models.CharField(_('Tipo'), max_length=2, choices=MEDIAS)
    media_id = models.CharField(_('Ref'), max_length=255)

    @property
    def videos(self):
        return self.objects.filter(kind='YT')

    @property
    def slides(self):
        return self.objects.filter(kind='SL')

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)
