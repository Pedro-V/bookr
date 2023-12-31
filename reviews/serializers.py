from rest_framework import serializers
from .models import Book, Publisher, Contributor, BookContributor

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']

class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']

class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookContributor
        fields = ['book', 'role']

class ContributorSerializer(serializers.ModelSerializer):
    bookcontributor_set = ContributionSerializer(many=True)
    amount_contributions = serializers.ReadOnlyField()
    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names', 'email', 'bookcontributor_set',
                  'amount_contributions']
        
