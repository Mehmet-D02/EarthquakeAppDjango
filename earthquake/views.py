import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def earthquake_data(request):
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        
        data_to_display = []
        rows = table.find_all('tr')[1:]  # İlk satır başlık olduğu için atlıyoruz
        for row in rows:
            columns = row.find_all('td')
            yer = columns[6].text.strip()
            tarih = columns[0].text.strip()
            buyukluk = columns[5].text.strip()
            derinlik = columns[3].text.strip()
            
            
            
            data_to_display.append({
                "Yer": yer,
                "Tarih": tarih,
                "Büyüklük": buyukluk,
                "Derinlik": derinlik,
                
                
            })
        
        return render(request, 'earthquake/earthquake_data.html', {'data': data_to_display})
    
    return render(request, 'earthquake/earthquake_data.html', {'error': 'Veri çekilemedi.'})
