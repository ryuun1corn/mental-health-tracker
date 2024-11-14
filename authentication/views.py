import json

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse(
                {"status": False, "message": "Passwords do not match."}, status=400
            )

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"status": False, "message": "Username already exists."}, status=400
            )

        # Create the new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        return JsonResponse(
            {
                "username": user.username,
                "status": "success",
                "message": "User created successfully!",
            },
            status=200,
        )

    else:
        return JsonResponse(
            {"status": False, "message": "Invalid request method."}, status=400
        )


@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse(
                {
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!",
                    # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                },
                status=200,
            )
        else:
            return JsonResponse(
                {"status": False, "message": "Login gagal, akun dinonaktifkan."},
                status=401,
            )

    else:
        return JsonResponse(
            {
                "status": False,
                "message": "Login gagal, periksa kembali email atau kata sandi.",
            },
            status=401,
        )
