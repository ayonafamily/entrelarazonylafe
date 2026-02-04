import os
import re

path = "content/posts"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            if line.startswith("title:"):
                # Extraemos el texto del título quitando 'title:' y espacios
                content = line.replace("title:", "").strip()
                # Quitamos TODAS las comillas que tenga al principio y al final
                clean_content = content.strip('"').strip("'")
                # Lo envolvemos en una comilla simple externa y comillas dobles internas
                new_line = f"title: '\"{clean_content}\"'\n"
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        with open(full_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

print("✅ Todos los títulos han sido blindados con comillas simples externas.")
