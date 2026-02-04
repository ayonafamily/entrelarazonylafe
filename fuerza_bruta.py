import re
import os

archivo_xml = 'entrelaraznylafe.WordPress.2026-02-03.xml'
carpeta_posts = 'content/posts'

with open(archivo_xml, 'r', encoding='utf-8') as f:
    xml_data = f.read()

# 1. Mapeamos IDs de imágenes a su ruta de carpetas (año/mes/archivo)
rutas_imagenes = {}
items = re.findall(r'<item>(.*?)</item>', xml_data, re.DOTALL)

for item in items:
    if 'attachment' in item:
        post_id = re.search(r'<wp:post_id>(\d+)</wp:post_id>', item).group(1)
        # Extrae desde el año en adelante: 2016/05/foto.jpg
        ruta_match = re.search(r'wp-content/uploads/(.*?)]]>', item)
        if ruta_match:
            rutas_imagenes[post_id] = ruta_match.group(1)

# 2. Inyectamos la ruta en los archivos Markdown
for item in items:
    if '<wp:post_type><![CDATA[post]]>' in item or '<wp:post_type>post</wp:post_type>' in item:
        slug_match = re.search(r'<wp:post_name><!\[CDATA\[(.*?)\]\]>', item)
        thumb_match = re.search(r'_thumbnail_id.*?<wp:meta_value><!\[CDATA\[(\d+)\]\]>', item, re.DOTALL)
        
        if slug_match and thumb_match:
            slug = slug_match.group(1)
            thumb_id = thumb_match.group(1)
            archivo_md = os.path.join(carpeta_posts, f"{slug}.md")
            
            if thumb_id in rutas_imagenes and os.path.exists(archivo_md):
                ruta_final = f"/images/{rutas_imagenes[thumb_id]}"
                
                with open(archivo_md, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                
                # Si no tiene cover, se lo ponemos en la línea 4
                if not any("cover:" in l for l in lineas):
                    lineas.insert(4, f"cover:\n    image: \"{ruta_final}\"\n    relative: false\n")
                    with open(archivo_md, 'w', encoding='utf-8') as f:
                        f.writelines(lineas)
                    print(f"✅ Vinculado: {slug} -> {ruta_final}")

print("Terminado.")