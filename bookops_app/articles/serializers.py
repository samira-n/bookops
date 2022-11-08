from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'datetime', 'category']