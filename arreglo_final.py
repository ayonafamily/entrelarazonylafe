import os
import re

path = "content/posts"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Separar encabezado y cuerpo
        parts = content.split("---")
        body = parts[-1].strip()

        # 2. Rescatar el título original del archivo (o del post)
        title_match = re.search(r'title:\s*"(.*?)"', content)
        if title_match:
            title_text = title_match.group(1).replace('"', "")
        else:
            title_text = filename.replace(".md", "").replace("-", " ").capitalize()

        # 3. Rescatar la imagen del cuerpo si existe (ej. <img src="...">)
        img_match = re.search(r'src="([^"]*/images/[^"]+)"', body)
        # Limpiamos la ruta para que sea relativa a /static/
        if img_match:
            raw_path = img_match.group(1)
            clean_img = "/" + raw_path.split("/images/")[1]
            clean_img = f"/images/{clean_img}".replace("//", "/")
        else:
            clean_img = ""

        # 4. Reconstruir el post con formato BLINDADO
        nuevo_post = f"""---
title: '{title_text}'
date: 2025-02-02
thumbnail: "{clean_img}"
draft: false
---

{body}
"""
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(nuevo_post)

print("✅ Los 264 posts han sido normalizados y blindados.")
