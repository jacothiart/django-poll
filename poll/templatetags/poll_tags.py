from django import template
from django.conf import settings

from project.polls.methods import get_poll_form, get_poll_vote_form

from project.coffee.mixins import FormMixin

register = template.Library()

@register.inclusion_tag('polls/poll/partial/poll.html')
def poll_form(instance, request):
    form, formset = get_poll_form(instance, request)
    
    coffee = FormMixin()
    
    placeholders = {
        'question': 'Question'
    }
    
    coffee.construct_widgets(form.fields, placeholders, must_delete=False)
    
    placeholders = {
        'choice_text': 'Choice'
    }
    
    for formset_form in formset:
        coffee.construct_widgets(formset_form.fields, placeholders, must_delete=False)
    
    return {'form': form, 'formset': formset}


@register.inclusion_tag('polls/partial/vote.html')
def poll_vote(instance):
    form = get_poll_vote_form(instance)
    
    return {'form': form, 'instance': instance}


@register.simple_tag(takes_context=True)
def set_data(context):
    poll = context['poll']

    data = []

    for choice in poll.choice_set.all():
        data.append([str(choice.choice_text), float(choice.percentage)])

    context['pie_data'] = data
    
    return ''

@register.simple_tag(takes_context=True)
def set_bar_data(context):
    poll = context['poll']

    data = []

    for choice in poll.choice_set.all():
        data.append([float(choice.percentage)])

    context['bar_data'] = data
    
    return ''
    
@register.simple_tag(takes_context=True)
def set_bar_labels(context):
    poll = context['poll']

    data = []

    for choice in poll.choice_set.all():
        data.append(str(choice.choice_text))

    context['bar_labels'] = data
    
    return ''
    
@register.simple_tag(takes_context=True)
def set_chart_types(context):
    chart_types = getattr(
            settings,
            'POLL_CHART_TYPES',
            ['pie', 'bar'])
    
    context['chart_types'] = chart_types
    
    return ''