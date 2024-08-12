import requests

def tarama():
    def test_sql_injection(url, parameter):
        payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #"]
        for payload in payloads:
            test_url = f"{url}?{parameter}={payload}"
            response = requests.get(test_url)
            if "database error" in response.text.lower():
                print(f"[!] SQL Injection Detected with payload: {payload}")
            else:
                print(f"[+] No SQL Injection detected with payload: {payload}")

    def test_xss(url, parameter):
        payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>"]
        for payload in payloads:
            test_url = f"{url}?{parameter}={payload}"
            response = requests.get(test_url)
            if payload in response.text:
                print(f"[!] XSS Detected with payload: {payload}")
            else:
                print(f"[+] No XSS detected with payload: {payload}")

    # Burada __name__ == "__main__" kullanımı gereksizdir, direkt fonksiyon çağrısı yeterlidir.
    target_url = input("Test edilecek URL'yi girin: ")
    parameter_name = input("Test edilecek parametreyi girin (örnek: id): ")

    print("\nSQL Injection Testi Başlıyor...")
    test_sql_injection(target_url, parameter_name)

    print("\nXSS Testi Başlıyor...")
    test_xss(target_url, parameter_name)