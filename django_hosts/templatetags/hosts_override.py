"""
A template tag library that is automatically added to Django's
built-in template tags if the setting HOST_OVERRIDE_URL_TAG is set
to True.
"""
from django import template

from .hosts import host_url

register = template.Library()


@register.tag
def url(parser, token):
    """
    A tag to override the built-in url template tag. Accepts host parameters
    optionally.

    {% url 'view-name' host 'host-name'  %}
    {% url 'view-name' host 'host-name' 'spam' %}
    {% url 'view-name' host 'host-name' scheme 'https' %}
    {% url 'view-name' host 'host-name' as url_on_host_variable %}
    {% url 'view-name' varg1=vvalue1 host 'host-name' 'spam' 'hvalue1' %}
    {% url 'view-name' vvalue2 host 'host-name' 'spam' harg2=hvalue2 %}
    """
    return host_url(parser, token)
