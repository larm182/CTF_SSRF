SSRF e Inyección de Comandos

Autor: Ing. Larm182

📅 **Fecha:** 10 de febrero de 2025  
✍️ **Autor:** Ing. Larm  
🏷️ **Tags:** CTF, XSS, Flask, Bootstrap, Seguridad  

## 📖 Descripción  
Explotando vulnerabilidades comunes en aplicaciones web
Las vulnerabilidades de Server-Side Request Forgery (SSRF) e Inyección de Comandos son fallos críticos en la seguridad de aplicaciones web que pueden permitir a un atacante acceder a recursos internos o ejecutar comandos en el servidor.

🔥 SSRF (Server-Side Request Forgery)
SSRF ocurre cuando una aplicación web permite que un usuario controle las solicitudes realizadas desde el servidor. Esto puede llevar a:

Acceso a redes internas
Filtración de datos sensibles
Interacción con servicios internos como 169.254.169.254 en AWS
Escaneo de puertos internos

Ejemplo de explotación SSRF en una API vulnerable:

import requests

url = "http://victima.com/api/fetch"

data = {"url": "http://localhost/admin"}

response = requests.post(url, json=data)

print(response.text)  # ¿Información interna filtrada?

⚡ Inyección de Comandos
Este tipo de vulnerabilidad ocurre cuando una aplicación ejecuta comandos del sistema sin sanitizar adecuadamente la entrada del usuario.

Ejemplo de explotación:
Si un formulario permite ejecutar ping sin validación, podríamos inyectar un comando malicioso:

127.0.0.1 && cat /etc/passwd

Bypass común en filtros básicos:
Si el servidor bloquea "&&", podemos usar:

🛡️ Medidas de mitigación
Validación y sanitización estricta de entradas
Uso de listas blancas para URLs en SSRF
Evitar funciones peligrosas como system(), exec(), popen()
Aplicar políticas de seguridad como restricciones en el firewall

🎯 Desafío: Encuentra la flag oculta
Si llegaste hasta aquí, prueba buscando en este repositorio... quizás haya una flag oculta esperando ser encontrada. 😉

Video DEMO:

https://github.com/user-attachments/assets/f552aeba-682d-47af-9efd-b52a7f6558d8





