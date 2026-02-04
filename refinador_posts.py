import os

path = "content/posts"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            continue

        # Limpiar el título de caracteres que rompen el YAML
        new_lines = []
        for line in lines:
            if line.startswith("title: "):
                # Extrae el título, quita comillas existentes y lo limpia
                title_text = line.replace("title: ", "").strip().strip('"')
                # Lo vuelve a escribir con comillas seguras
                new_lines.append(f'title: "{title_text}"\n')
            else:
                new_lines.append(line)

        with open(full_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

print("✅ Cabeceras YAML corregidas en todos los posts.")
