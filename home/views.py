from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *


class IndexTemplateView(TemplateView):
    """
    A class-based view to render the index page template.

    Attributes:
        template_name (str): The name of the template to be rendered ('pages/index.html').

    Methods:
        get_context_data(**kwargs):
            Retrieves the context data for rendering the template.
            Adds a context variable 'segment' with the value 'index'.
            Args:
                **kwargs: Additional keyword arguments.
            Returns:
                dict: A dictionary containing the context data for the template.
    """
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for rendering the template.

        Adds a context variable 'segment' with the value 'index'.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing the context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["segment"] = 'index'
        return context


class TablesTemplateView(TemplateView):
    """
    A class-based view to render the dynamic tables page template.

    Attributes:
        template_name (str): The name of the template to be rendered ('pages/dynamic-tables.html').

    Methods:
        get_context_data(**kwargs):
            Retrieves the context data for rendering the template.
            Adds a context variable 'segment' with the value 'tables'.
            Args:
                **kwargs: Additional keyword arguments.
            Returns:
                dict: A dictionary containing the context data for the template.
    """
    template_name = 'pages/dynamic-tables.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for rendering the template.

        Adds a context variable 'segment' with the value 'tables'.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing the context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["segment"] = 'tables'
        return context

