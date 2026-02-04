import os

path = "content/posts"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(
            full_path, "r", encoding="utf-8-sig"
        ) as f:  # 'utf-8-sig' quita basura invisible
            content = f.read().strip()  # Quitamos espacios al inicio y final

        # Separamos el encabezado del cuerpo para reconstruirlo limpio
        # Buscamos el contenido después de los guiones
        parts = content.split("---")

        # Si el archivo tiene el formato esperado (--- metadata --- contenido)
        if len(parts) >= 3:
            metadata = parts[1]
            body = "---".join(parts[2:])

            # Limpiamos líneas vacías en la metadata
            meta_lines = [line.strip() for line in metadata.split("\n") if line.strip()]
            clean_meta = "\n".join(meta_lines)

            new_content = f"---\n{clean_meta}\n---\n\n{body.strip()}"

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(new_content)

print("✅ Archivos normalizados. Todos empiezan ahora con '---' en la línea 1.")
