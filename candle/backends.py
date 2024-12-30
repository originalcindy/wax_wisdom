from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        try:
            # check if the input matches either username or email
            user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
            
            # check the password
            if user.check_password(password):
                return user
                
        except UserModel.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None