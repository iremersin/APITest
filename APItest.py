import requests

def print_data(data):
    # Çıktıyı array formatında oluşturma

    for flight in data.get("data", []):
        print("Flight {")
        print(f'  "Id": {flight.get("id", "")},')
        print(f'  "From": "{flight.get("from", "")}",')
        print(f'  "To": "{flight.get("to", "")}",')
        print(f'  "Date": "{flight.get("date", "")}"')
        print("}")

def test_api_request():
    # API endpoint ve headers
    url = "https://flights-api.buraky.workers.dev"
    header_type = {"Content-Type": "application/json"}

    # GET isteği gönderme
    response = requests.get(url, headers=header_type)

    # Durum kodunu kontrol etme
    if response.status_code != 200:
        error_message = "Hata! Durum Kodu: {}".format(response.status_code)
        print(error_message)
        # Burada başka bir tepki gösterebilirsiniz, örneğin bir log kaydı oluşturabilir veya hata mesajını işleyebilirsiniz.
    else:
        # Durum kodu 200 ise devam et
        print("200 OK\n")

    # Content-Type header'ını kontrol etme
    content_type = response.headers.get("Content-Type")
    expected_content_type = "application/json"
    if content_type != expected_content_type:
        error_message = "Hata! İçerik Türü: {}".format(content_type)
        print(error_message)
        # Burada başka bir tepki gösterebilirsiniz, örneğin bir log kaydı oluşturabilir veya hata mesajını işleyebilirsiniz.
    else:
        # Content-Type doğru ise devam et
        print("Content-Type doğru.")
    # Yanıt içeriğini işleme
    json_data = response.json()

    # JSON içeriğini array formatında yazdırma
    print_data(json_data)

if __name__ == "__main__":
    test_api_request()
    
    
