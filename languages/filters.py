from django_filters import CharFilter, FilterSet

from languages.models import OriginalWord


class WordsFilterSet(FilterSet):
    catalog = CharFilter(field_name="catalog__name")

    class Meta:
        model = OriginalWord
        fields = ["catalog"]
