import requests
import json
from django.shortcuts import render

def earthquake_data(request):
    url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"

    payload = {}
    headers = {}

    response = requests.request("GET", url)

    result = json.loads(response.text)

    count = 0
    data_to_display = []
    for i in result["result"]:
        if count > 300:
            break
        if i["mag"] > 1:
            data_to_display.append({
                "Tarih": i["date"],
                "Bölge": i["title"],
                "Büyüklük": i["mag"],
                "Derinlik": i["depth"]
            })
            count += 1

    return render(request, 'earthquake/earthquake_data.html', {'data': data_to_display})
