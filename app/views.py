# from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from .models import User
import datetime
import pandas as pd
import numpy as np
from django.views.decorators.csrf import ensure_csrf_cookie
from plotly.offline import plot
from plotly.graph_objs import *
from django.contrib import messages
import plotly.express as px
from django.views.generic import TemplateView
import logging
from . import plots

logger = logging.getLogger(__name__)


class Graph(TemplateView):
    template_name = "app/predvis.html"

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        context['plot'] = plots.graph()

        return context

def index(request):

    # Authenticated users can use the prediction tool
    # if request.user.is_authenticated:
        return render(request, "app/index.html")

    # Everyone else is prompted to sign in
    # else:
    #     return HttpResponseRedirect(reverse("app:login"))


# Predict using Facebook Prophet (ML model)
# @ensure_csrf_cookie
# @login_required
def predict(request):
    if request.method == "POST":
        '''
        For rendering results on HTML GUI
        '''
        RequestDate = request.POST.get('market_dt')

        forecast = plots.predict()
        result = forecast.loc[forecast['ds']==RequestDate]
        pred= result['yhat']
        opti_pred = result['yhat_upper']
        pers_pred = result['yhat_lower']

    return render(request, 'app/index.html', {
        "prediction_text": round(pred.values[0], 2),
        "optimistic_pred": round(opti_pred.values[0], 2),
        "perssimistic_pred": round(pers_pred.values[0], 2),
        "RequestDate": RequestDate})

# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("app:index"))
#         else:
#             return render(request, "app/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "app/login.html")


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("app:index"))


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "app/register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, "app/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("app:index"))
#     else:
#         return render(request, "app/register.html")

    