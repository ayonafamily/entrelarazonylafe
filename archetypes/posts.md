---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
author: "Jorge Luis Ayona Inglis"
ShowReadingTime: true
draft: true

# Descripción larga del artículo (SEO / metadata)
description: ""

# Resumen usado en listados y previews (PaperMod)
summary: ""

# Categorías y etiquetas (listas YAML)
categories: []
tags: []

# Imagen destacada del post (PaperMod)
# IMPORTANTE:
# - La imagen debe estar físicamente en: static/images/AAAA/nombre.webp
# - Aquí se usa ENLACE ABSOLUTO para compatibilidad visual y OG
# - Nota: La imagen se vera solo cuando esta desplegado en vercel

cover:
  image: "https://entrelarazonylafe.vercel.app/images/AAAA/nombre-imagen.webp"
  alt: ""
  relative: false

# Imágenes OpenGraph / WhatsApp
# - SIEMPRE enlaces absolutos
# - WhatsApp ignora rutas relativas
images:
  - "https://entrelarazonylafe.vercel.app/images/AAAA/nombre-imagen.webp"
---
