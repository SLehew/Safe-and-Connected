from modeltranslation.translator import TranslationOptions, register
from .models import Event


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('event_title', 'general_notes')
