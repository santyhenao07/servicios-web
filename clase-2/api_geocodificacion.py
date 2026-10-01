import requests

CIUDAD = "Madrid"

# Servicio 1: Open-Meteo Geocoding (nombre de ciudad -> coordenadas)
geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": CIUDAD, "count": 10}
)

# TODO 1: imprimir el código de estado HTTP

print(geo.status_code)

# TODO 2: convertir la respuesta a JSON y tomar el primer resultado
lugar = geo.json()["results"][0]

# TODO 3: extraer latitud, longitud, nombre y país
lat, lon = lugar["latitude"], lugar["longitude"]
nombre, pais = lugar["name"], lugar["country"]

print(f"{nombre}, {pais} -> lat {lat}, lon {lon}")

if geo.status_code != 200:
    print(f"Error {geo.status_code}: {geo.json().get('reason')}")
    raise SystemExit(1)

resultados = geo.json().get("results")
if not resultados:
    print(f"No se encontró la ciudad: {CIUDAD}")
    raise SystemExit(1)

lugar = resultados[0]

# Servicio 2: Open-Meteo Forecast (coordenadas -> clima actual)
clima = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": lat, "longitude": lon, "current_weather": True}
)

# TODO 4: verificar el código de estado
print(clima.status_code)

# TODO 5: extraer la temperatura actual
temp = clima.json()["current_weather"]["temperature"]

print(f"En {nombre}, {pais} ahora hace {temp}°C")