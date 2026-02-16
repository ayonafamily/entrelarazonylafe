---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
author: "Jorge Luis Ayona Inglis"
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
