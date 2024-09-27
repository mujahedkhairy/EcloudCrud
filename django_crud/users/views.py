from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import User
from .forms import UserForm, LoginForm



class HomeView(ListView):
    template_name = 'users/home.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('get_users')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = form.cleaned_data['password']  # Directly store the password for testing
        user.save()
        messages.success(self.request, "User created successfully.")
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('get_users')

    def form_valid(self, form):
        # Save the form without hashing the password
        user = form.save(commit=False)
        # If a new password is provided, update it directly
        if form.cleaned_data['password']:
            user.password = form.cleaned_data['password']  # Directly assign the password
        user.save()
        messages.success(self.request, "User updated successfully.")
        return super().form_valid(form)



class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('get_users')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "User deleted successfully.")
        return super().delete(request, *args, **kwargs)


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('get_users')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.password == password:  # Directly compare for testing
                user.active = True  # Set user active status
                user.save()  # Save the updated user status
                messages.success(self.request, f"{user.username} logged in successfully.")
                return redirect(self.get_success_url())  # Redirect to success URL
            else:
                messages.error(self.request, "Incorrect password.")
        except User.DoesNotExist:
            messages.error(self.request, "User does not exist.")
        return self.form_invalid(form)



def logout_user(request, id):
    user = get_object_or_404(User, id=id)
    user.active = False
    user.save()
    messages.success(request, f"{user.username} logged out successfully.")
    return redirect('get_users')
