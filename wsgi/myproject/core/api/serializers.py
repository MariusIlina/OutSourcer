from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer #HyperlinkedModelSerializer
from rest_framework.serializers import ValidationError #HyperlinkedRelatedField
from core.models import Company, Country, PaymentTypes, Currency
from core.models import TimeUnit, Project, Bid, Recommendation, Category, Comment
from django.core.validators import validate_email


class PaymentTypesSerializer(ModelSerializer):
    class Meta:
        model = PaymentTypes
        fields = ('id', 'type_name')


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'currency_name', 'currency_short_name')


class TimeUnitSerializer(ModelSerializer):
    class Meta:
        model = TimeUnit
        fields = ('id', 'unit_name')


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'country_name', 'country_code')

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'employees_no', 'description', 'country', 'county',
                  'city', 'slug_name', 'email', 'phone', 'external_link', 'user')
        read_only_fields = ('user',)

    def validate(self, data):
        if validate_email(data['email']) is False:
            raise ValidationError()
        return data


class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = ('id', 'payment_type', 'payment_amount', 'currency', 'project', 'by_company')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'on_project', 'comment', 'by_company')


class RecommendationSerializer(ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('id', 'by_company', 'for_company')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')


class ProjectSerializer(ModelSerializer):
    comments = CommentSerializer(read_only=True)
    recommendations = RecommendationSerializer(read_only=True)
    bids = BidSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'pub_date', 'by_company', 'approximate_duration',
                  'approximate_duration_time_unit', 'description', 'work_description',
                  'slug_name', 'required_techs', 'approximate_hours_per_week', 'payment_type',
                  'payment_amount', 'currency', 'min_ppl_required', 'category', 'comments',
                  'recommendations', 'bids')
