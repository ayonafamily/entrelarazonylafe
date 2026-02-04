import os
import re

path = "content/posts"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Buscamos cualquier línea de imagen (featured_image o thumbnail)
        # 2. Limpiamos la ruta: quitamos '..', '//', etc.
        def limpiar_ruta(match):
            ruta = match.group(2)
            ruta_limpia = ruta.replace("..", "").replace("//", "/").strip()
            if not ruta_limpia.startswith("/"):
                ruta_limpia = "/" + ruta_limpia
            return f'thumbnail: "{ruta_limpia}"'

        new_content = re.sub(
            r'(featured_image|thumbnail):\s*"(.*?)"', limpiar_ruta, content
        )

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)

print("✅ Rutas de imágenes normalizadas en los 264 posts.")
