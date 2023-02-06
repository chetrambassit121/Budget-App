from users.models import User, UserProfile
# from users.api.serializers import UserDetailSerializer
from family_budget.models import Project, Category, Expense
from rest_framework.serializers import (  
    ModelSerializer,
)


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
        
class ProjectSerializer(ModelSerializer):
    author = UserDetailSerializer()
    class Meta:
        model = Project
        fields= [
            "name",
            "budget",
            "slug",
            "author"
        ]


class CategorySerializer(ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Category
        fields = [
            "project",
            "name"
        ]



class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            # "project",
            "name"
        ]
from rest_framework import serializers
class ProjectCreateSerializer(ModelSerializer):
    # author = UserListSerializer()
    # category = CategoryCreateSerializer()
    # category = serializers.StringRelatedField(many=True)
    # category = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Project
        fields= [
            "name",
            "budget",
            # "author"
            # "category"
        ]
    # class Meta:
    #     model = Category
    #     fields= [
    #         # "project",
    #         "name",
    #         # "author"
    #         # "category"
    #     ]



class ExpenseSerializer(ModelSerializer):
    project = ProjectSerializer()
    category = CategorySerializer()
    class Meta:
        model = Expense
        fields = [
            "project",
            "title",
            "amount",
            "category"
        ]

class CreateExpenseSerializer(ModelSerializer):
    # project = ProjectSerializer()
    # category = CategorySerializer()
    class Meta:
        model = Expense
        fields = [
            "project",
            "title",
            "amount",
            "category"
        ]
