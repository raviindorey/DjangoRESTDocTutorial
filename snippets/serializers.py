from rest_framework import serializers
from snippets.models import Snippet


# Default create() and update()
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
