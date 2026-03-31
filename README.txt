# Monitoring usług HTTP (Python)

Prosty system monitoringu usług HTTP napisany w Pythonie. 
Projekt sprawdza dostępność wybranych URL-i, zapisuje wyniki do pliku logów 
oraz wyświetla kolorowe komunikaty w terminalu.

## Funkcje
- Health-check usług HTTP
- Logowanie do pliku (UTF-8)
- Kolorowe logi w terminalu (ANSI)
- Obsługa błędów i wyjątków
- Alerty w przypadku awarii

## Uruchomienie
python monitoring.py

## Przykład logów
[2026-03-31 19:05:12] OK     https://google.com -> 200
[2026-03-31 19:05:12] FAIL   https://nieistniejaca-strona.pl -> ConnectionError
