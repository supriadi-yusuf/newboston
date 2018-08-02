from rest_framework import serializers
from . models import Stock

# spd - name convention : object + Serializer.
# spd - ex. : we want to serializer Stock so class name should be StockSerializer
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock # spd - specify model's name
        # fields = '__all__' # spd - display all fields
        fields = ('ticker', 'volume') # spd - suppose we only display these two fields
