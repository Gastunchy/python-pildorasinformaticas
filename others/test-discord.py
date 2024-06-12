import requests

# Mensaje simple

url = "https://discord.com/api/webhooks/1240805872779919505/1xmv4a5OXswmtdceDNhqPYukNLOFXW-ndQECm2R-EqswyVd6-6KDoBsr9P_XMuI3MAVV"

data = {
    "content":"Ejemplo simple",
    "embeds":[{"description":"Esto es un mensaje del ejemplo simple"}]
}

y = requests.post(url,json=data)
print(y)

# Mensaje complejidad media

url = "https://discord.com/api/webhooks/1240805872779919505/1xmv4a5OXswmtdceDNhqPYukNLOFXW-ndQECm2R-EqswyVd6-6KDoBsr9P_XMuI3MAVV"

mensaje = "Ejempo complejidad media"

embed = {
    'title': 'Título del Embed', #obligatorio
    'description': 'Descripción del embed con más detalles',# obligatorio
    'fields': [
        {'name': 'Campo 1', 'value': 'Este es el valor del campo 1', 'inline': False},
    ]}
data = {
    "content":mensaje, # Obligatorio
    "embeds":[embed], # Obligatorio
}

x = requests.post(url,json=data)
print(x)

# Ejemplo de un mensaje pro (chatgpt)

# Reemplaza 'your_webhook_url' con la URL de tu webhook
webhook_url = 'https://discord.com/api/webhooks/1240805872779919505/1xmv4a5OXswmtdceDNhqPYukNLOFXW-ndQECm2R-EqswyVd6-6KDoBsr9P_XMuI3MAVV'

# Mensaje principal
message = 'Ejemplo de un mensaje pro (chatgpt)'

# Datos adicionales
embed = {
    'title': 'Título del Embed',
    'description': 'Descripción del embed con más detalles',
    'url': 'https://example.com',
    'color': 0x3498db,
    'fields': [
        {'name': 'Campo 1', 'value': 'Este es el valor del campo 1', 'inline': False},
        {'name': 'Campo 2', 'value': 'Este es el valor del campo 2', 'inline': True},
        {'name': 'Campo 3', 'value': 'Este es el valor del campo 3', 'inline': True}
    ],
    'footer': {'text': 'Este es el texto del pie de página', 'icon_url': 'https://c0.klipartz.com/pngpicture/620/835/gratis-png-logo-azul-y-amarillo-logo-de-python.png'},
    'thumbnail': {'url': 'https://e7.pngegg.com/pngimages/761/45/png-clipart-professional-python-programmer-computer-programming-android-android-blue-logo.png'},
    'image': {'url': 'https://st2.depositphotos.com/1606646/48825/i/450/depositphotos_488252618-stock-illustration-python-symbol-white-background-rendering.jpg'}
}

# Payload
data = {
    'content': message,
    'username': 'Mi Bot',
    'embeds': [embed]
}

headers = {
    'Content-Type': 'application/json'
}

# Enviar solicitud POST
response = requests.post(webhook_url, json=data, headers=headers)

# Manejar la respuesta
if response.status_code == 204:
    print('Mensaje enviado exitosamente')
else:
    print(f'Error al enviar mensaje: {response.status_code}, {response.text}')

