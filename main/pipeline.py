from django.contrib.auth.models import Group

def save_to_group(backend, user, response, *args, **kwargs):
    defaultgroup = Group.objects.get(name = 'Visitor')
    user.groups.add(defaultgroup)


