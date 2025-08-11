from django import template

register =template.Library()
@register.inclusion_tag('partials/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    request = context['request']
    path_parts = request.path.strip('/').split('/')
    breadcrumbs_list - []
    url_accumulator = ''

    for part in path_parts:
        url_accumulator += '/' + part
        breadcrumbs_list.append({
            return:
        })
