from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, allow_blank=False
    )

    class Meta:
        model = User
        fields = ("email", "password")
        # extra_kwargs = {
        #     "password": {"write_only": True}
        # }

    def validate(self, attrs):
        email = attrs.get("email")
        user = User.objects.filter(email=email)
        password = attrs.get("password")

        if not user.exists():
            raise serializers.ValidationError({"error": "not found email"})

        user = user.get()

        if not user.check_password(password):
            raise serializers.ValidationError({"error": "wrong password"})

        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, allow_blank=False
    )

    class Meta:
        model = User
        fields = ("email", "password", "name",)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "this email already registered"})
        
        return attrs
    
    def save(self):
        account = User(
            email=self.validated_data['email'],
            name=self.validated_data['name']
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account
