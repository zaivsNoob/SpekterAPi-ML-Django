from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from setfit import SetFitModel
# Create your views here.

@api_view(["POST"])
def analyzer(request):
    text=request.data.get("text")

    model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
    prediction = model([text])
    if prediction==0:
        return Response({"Sentiment":"Negative/Neutral"})
    elif prediction==1:
        return Response({"Sentiment":"Positive"})
