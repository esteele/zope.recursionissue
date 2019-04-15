# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BaseTemplate(BrowserView):

    def __call__(self):
        return ViewPageTemplateFile('base_template.pt')()

    @property
    def macros(self):
        return ViewPageTemplateFile('base_template.pt').macros


class BaseTemplateBroken(BrowserView):

    base_template = ViewPageTemplateFile('base_template.pt')

    def __call__(self):
        return self.template()

    @property
    def template(self):
        return self.base_template

    @property
    def macros(self):
        return self.template.macros
