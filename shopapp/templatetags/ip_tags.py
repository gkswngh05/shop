from django import template

register = template.Library()


import socket

@register.simple_tag
def get_ip():
    return str(socket.gethostbyname(socket.gethostname()))