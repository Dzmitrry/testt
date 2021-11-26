import telebot

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status

from main.serializers import FeedbackSerializer
from main.forms import FeedBackForm
from main.models import Feedback


@api_view(("GET", "POST",))
def feedback_list(request):
    serializer_class = FeedbackSerializer

    if request.method == "GET":
        queryset = Feedback.objects.all()

        serializer = serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


def index(request):
    if request.method == "POST":
        feedbackform = FeedBackForm(request.POST)


    feedbackform = FeedBackForm()
    data = {'feedbackform' : feedbackform}
    return render(request, 'main/index.html', data)


