from rest_framework import serializers

from .models import Page


class PageSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ["name", "children", "url"]

    def get_children(self, obj):
        children = Page.objects.filter(parent=obj)
        serializer = PageSerializer(children, many=True)
        return serializer.data
