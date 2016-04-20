from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from core.models import Company, Project

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST']
OWNER_METHODS = ['PUT', 'PATCH', 'DELETE']

class IsCompanyOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Returns true if the user is the owner of the entity or is staff
        """
        if request.method in SAFE_METHODS:
            return True
        elif request.method in OWNER_METHODS:
            if obj.user == request.user or obj.user.is_staff:
                return True
            return False


class IsProjectOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Returns true if the authenticated user is the user who created the
        company that posted the project
        """
        if request.method in SAFE_METHODS:
            return True
        # Allow users to edit only projects that belong to their companies
        elif request.method in OWNER_METHODS:
            if obj.by_company.user == request.user:
                return True
            return False

    def has_permission(self, request, view):
        """
        Returns true if the authenticated user is the user who created the
        company that is posting a new project
        """
        if request.method == 'POST':
            companies = Company.objects.filter(user=request.user, id=request.data['by_company'])
            if len(companies) > 0:
                return True
            return False


class BidderIsCompanyOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Returns true if the user who wants to bid on a project is the owner
        of the company on which behalf he does the bidding
        """
        return True