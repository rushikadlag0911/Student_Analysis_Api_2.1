from rest_framework import serializers
from .models import studdetails, studmarks

class studserializers(serializers.ModelSerializer):
    class Meta:
        model = studdetails
        fields = ('name','roll_num','DOB')

    def validate(self, attrs):
        roll_num = attrs.get('roll_num')
        if studdetails.objects.filter(roll_num=roll_num).exists():
            raise serializers.ValidationError(
                {'roll_num': ('roll_num is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return studdetails.objects.create(**validated_data)
        
    
class studmarksserializers(serializers.ModelSerializer):
    name = serializers.CharField(source="roll_num.name")
    DOB =  serializers . DateField (source="roll_num.DOB")
    
    class Meta:
        model = studmarks
        fields = ('roll_num','name','DOB','English','Maths','History')

        def validate(self, attrs):
            roll_num = attrs.get('roll_num')
            if studmarks.objects.filter(roll_num=roll_num).exists():
                raise serializers.ValidationError(
                    {'roll_num': ('roll_num is already in use')})
            return super().validate(attrs)
        
        def create(self, validated_data):
            return studmarks.objects.create(**validated_data)


class smarkserializer(serializers.ModelSerializer):

    class Meta:
        model = studmarks
        fields = ('English','Maths', 'History', 'roll_num')
    
        def validate(self, attrs):
            roll_num = attrs.get('roll_num')
            if studmarks.objects.filter(roll_num=roll_num).exists():
                raise serializers.ValidationError(
                    {'roll_num': ('roll_num is already in use')})
            return super().validate(attrs)
        
        def create(self, validated_data):
            return studmarks.objects.create(**validated_data)
    
