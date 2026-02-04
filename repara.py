import os
import re

path = "content/posts"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            text = f.read()

        # 1. Extraer Título (Texto arriba de ===)
        title_match = re.search(r"\n(.*?)\n={3,}", text)
        title = (
            title_match.group(1).strip() if title_match else filename.replace(".md", "")
        )

        # 2. Extraer Imagen principal
        img_match = re.search(r"!\[\]\(\.\.//images/(.*?)\)", text)
        img_path = f"/images/{img_match.group(1)}" if img_match else ""

        # 3. Extraer Fecha (formato: Feb 28, 2025)
        date_match = re.search(r"\[([A-Z][a-z]{2}\s\d{1,2},\s\d{4})\]", text)
        date_str = date_match.group(1) if date_match else "2025-02-02"

        # 4. LIMPIEZA: Cortar todo lo que esté antes del Título (menús, logos, etc)
        # Buscamos donde termina el título y las categorías
        content_parts = re.split(r"in \[.*?\]\(.*?\)", text)
        real_content = content_parts[-1].strip() if len(content_parts) > 1 else text

        # Quitar líneas sobrantes del inicio del contenido
        real_content = re.sub(
            r"^.*?—\s*by\s*\[.*?\]\(.*?\)", "", real_content, flags=re.DOTALL
        ).strip()

        # 5. Escribir el nuevo archivo con formato HUGO
        new_file = f"""---
title: "{title}"
date: {date_str}
featured_image: "{img_path}"
---

{real_content}
"""
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_file)
        print(f"✅ Procesado: {title}")
