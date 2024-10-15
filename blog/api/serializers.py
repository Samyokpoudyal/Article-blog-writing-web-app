from rest_framework import serializers
from ..models import Articles

class Blog_list_view_LISTAPIVIEW_serializers(serializers.ModelSerializer):
    username =serializers.SerializerMethodField()
    Profiles=serializers.SerializerMethodField()
    url=serializers.HyperlinkedIdentityField(
        view_name='blog.api.detail',
        lookup_field='id',
        
    )
    class Meta:
        model =Articles
        fields=['title','content','date_posted','url','username','Profiles']

    def get_username(self,obj):
        user=obj.author.username
        return user

    def get_Profiles(self,obj):
        profile=obj.author.profiles.img.url
        return str(profile)
    
class Blog_list_view_LISTDETAILAPIVIEW_serializers(serializers.ModelSerializer):
    username =serializers.SerializerMethodField()
    Profiles=serializers.SerializerMethodField()
    class Meta:
        model =Articles
        fields='__all__'

    def get_username(self,obj):
        user=obj.author.username
        return user

    def get_Profiles(self,obj):
        profile=obj.author.profiles.img.url
        return profile

class Blog_list_view_LISTCREATEUPDATEAPIVIEW_serializers(serializers.ModelSerializer):
    class Meta:
        model =Articles
        fields=['title','content','date_posted']

