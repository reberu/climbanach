from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        id = serializers.IntegerField()
        article_header = serializers.CharField(max_length=250)
        article_body = serializers.CharField()

        def create(self, validated_data):
            return Article.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.article_header = validated_data.get('article_header', instance.article_header)
            instance.article_body = validated_data.get('article_body', instance.article_body)

            instance.save()
            return instance