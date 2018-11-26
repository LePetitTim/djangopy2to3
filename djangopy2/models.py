# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Test(models.Model):
    boolean_1 = models.BooleanField(db_column='boolean1', default=True, verbose_name=_(u"Boolean_1"),
                                    help_text=_(u"This is the first boolean"))
    boolean_2 = models.BooleanField(db_column='boolean2', default=False, verbose_name=_(u"Boolean_2"),
                                    help_text=_(u"This is the second boolean"))
    char_1 = models.CharField(null=True, blank=True, max_length=10, db_column='char1', verbose_name=_(u"Char_1"),
                              help_text=_(u"This is the first char"), default='char1')
    char_2 = models.CharField(null=False, blank=False, max_length=20, db_column='char2', verbose_name=_(u"Char_2"),
                              help_text=_(u"This is the second char"), default='char2')
    char_3 = models.CharField(null=True, blank=False, max_length=30, db_column='char3', verbose_name=_(u"Char_3"),
                              help_text=_(u"This is the third char"), default='char3')
    char_4 = models.CharField(null=False, blank=True, max_length=250, db_column='char4',
                              verbose_name=_(u"Char_4"), help_text=_(u"This is the fourth char"), default='char4')

    class Meta:
        db_table = 'db_table_custom'
        verbose_name = _(u"DB table custom")
        verbose_name_plural = _(u"DB tables custom")
