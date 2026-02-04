import os
import re

# RUTAS
carpeta_posts = '/home/jorgelai/entrelarazonylafe/content/posts'
carpeta_static = '/home/jorgelai/entrelarazonylafe/static'

def buscar_archivo_en_subcarpetas(nombre_base):
    """Busca un archivo ignorando la extensión en todas las subcarpetas de static/images"""
    extensiones = ['.webp', '.jpg', '.jpeg', '.png', '.JPG']
    # Recorremos todas las carpetas dentro de static/images
    for raiz, dirs, archivos in os.walk(os.path.join(carpeta_static, "images")):
        for ext in extensiones:
            nombre_buscado = nombre_base + ext
            if nombre_buscado in archivos:
                # Retornamos la ruta relativa desde 'static' para Hugo
                ruta_completa = os.path.join(raiz, nombre_buscado)
                return ruta_completa.replace(carpeta_static, "")
    return None

def corregir_definitivo_recursivo():
    actualizados = 0
    
    for archivo_md in os.listdir(carpeta_posts):
        if archivo_md.endswith(".md"):
            ruta_path = os.path.join(carpeta_posts, archivo_md)
            
            with open(ruta_path, 'r', encoding='utf-8') as f:
                contenido = f.read()

            # Buscamos el nombre del archivo de imagen (sin importar la ruta que tenga ahora)
            # Esto busca el nombre entre la última barra y el punto de la extensión
            match = re.search(r'/?(?:images/|img/)?(?:[\w\-/]+/)?([\w\-]+)\.(?:jpg|webp|jpeg|png)', contenido)
            
            if match:
                nombre_imagen = match.group(1)
                ruta_hugo = buscar_archivo_en_subcarpetas(nombre_imagen)
                
                if ruta_hugo:
                    # Limpiamos el frontmatter
                    partes = contenido.split('---', 2)
                    if len(partes) >= 3:
                        fm = partes[1]
                        # Borramos rastros de cover, thumbnail o image anteriores
                        fm = re.sub(r'cover:.*?\n(?:\s+.*\n)*', '', fm)
                        fm = re.sub(r'thumbnail:.*?\n', '', fm)
                        fm = re.sub(r'image:.*?\n', '', fm)
                        
                        # Escribimos el bloque para PaperMod
                        nuevo_fm = fm.strip() + f'\ncover:\n    image: "{ruta_hugo}"\n    relative: false\n'
                        nuevo_contenido = f"--- \n{nuevo_fm}\n---{partes[2]}"
                        
                        with open(ruta_path, 'w', encoding='utf-8') as f:
                            f.write(nuevo_contenido)
                        print(f"✅ ENCONTRADO Y CORREGIDO: {archivo_md} -> {ruta_hugo}")
                        actualizados += 1
                else:
                    print(f"❌ No se halló el archivo físico para: {archivo_md}")

    print(f"\nPROCESO TERMINADO. Se arreglaron {actualizados} archivos recorriendo subdirectorios.")

if __name__ == "__main__":
    corregir_definitivo_recursivo()