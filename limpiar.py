import os
import re

directory = "content/posts"

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        path = os.path.join(directory, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Intentar extraer el título (lo que está debajo de los ===)
        title_match = re.search(r"\n(.*?)\n={2,}", content)
        title = title_match.group(1) if title_match else filename.replace(".md", "")

        # Intentar extraer la imagen
        image_match = re.search(r"!\[\]\(\.\.//images/(.*?)\)", content)
        image = f"/images/{image_match.group(1)}" if image_match else ""

        # Limpiar la basura (quitar menús, logos, etc.)
        # Buscamos donde empieza el contenido real (después del autor/categoría)
        split_content = content.split(
            "Aún así,"
        )  # Esto es solo un ejemplo, hay que ajustarlo

        # Crear el nuevo encabezado
        new_content = f'---\ntitle: "{title}"\ndate: 2025-02-28\nfeatured_image: "{image}"\n---\n\n'

        # Aquí añadiríamos la lógica para limpiar el resto...
        print(f"Procesado: {title}")
