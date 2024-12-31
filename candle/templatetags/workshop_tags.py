from django import template
register = template.Library()

@register.filter
def has_booked(workshop, user):
    return workshop.has_user_booked(user)