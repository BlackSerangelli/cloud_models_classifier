"""
Script principal para ejecutar todas las pruebas del clasificador de modelos de nube.
"""

from casos_prueba import CasosPrueba
from utilidades_prueba import UtilidadesPrueba

def ejecutar_pruebas_basicas():
    """Ejecuta las pruebas básicas del clasificador."""
    print("🧪 EJECUTANDO PRUEBAS BÁSICAS")
    print("=" * 60)
    
    casos = CasosPrueba.obtener_casos_basicos()
    resumen = UtilidadesPrueba.ejecutar_suite_pruebas(casos)
    
    # Imprimir resultados individuales
    for i, resultado in enumerate(resumen["resultados"], 1):
        UtilidadesPrueba.imprimir_resultado_prueba(resultado, i)
    
    # Imprimir resumen
    UtilidadesPrueba.imprimir_resumen_pruebas(resumen)
    
    return resumen

def ejecutar_pruebas_avanzadas():
    """Ejecuta las pruebas avanzadas del clasificador."""
    print("\n🧪 EJECUTANDO PRUEBAS AVANZADAS")
    print("=" * 60)
    
    casos = CasosPrueba.obtener_casos_avanzados()
    resumen = UtilidadesPrueba.ejecutar_suite_pruebas(casos)
    
    # Imprimir resultados individuales
    for i, resultado in enumerate(resumen["resultados"], 1):
        UtilidadesPrueba.imprimir_resultado_prueba(resultado, i)
    
    # Imprimir resumen
    UtilidadesPrueba.imprimir_resumen_pruebas(resumen)
    
    return resumen

def ejecutar_pruebas_edge():
    """Ejecuta las pruebas edge del clasificador."""
    print("\n🧪 EJECUTANDO PRUEBAS EDGE")
    print("=" * 60)
    
    casos = CasosPrueba.obtener_casos_edge()
    resumen = UtilidadesPrueba.ejecutar_suite_pruebas(casos)
    
    # Imprimir resultados individuales
    for i, resultado in enumerate(resumen["resultados"], 1):
        UtilidadesPrueba.imprimir_resultado_prueba(resultado, i)
    
    # Imprimir resumen
    UtilidadesPrueba.imprimir_resumen_pruebas(resumen)
    
    return resumen

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del clasificador."""
    print("🚀 EJECUTANDO TODAS LAS PRUEBAS DEL CLASIFICADOR")
    print("=" * 60)
    
    # Ejecutar cada suite de pruebas
    resumen_basicas = ejecutar_pruebas_basicas()
    resumen_avanzadas = ejecutar_pruebas_avanzadas()
    resumen_edge = ejecutar_pruebas_edge()
    
    # Resumen general
    print("\n🎯 RESUMEN GENERAL")
    print("=" * 60)
    
    total_pruebas = (
        resumen_basicas["total_pruebas"] + 
        resumen_avanzadas["total_pruebas"] + 
        resumen_edge["total_pruebas"]
    )
    
    total_exitosas = (
        resumen_basicas["pruebas_exitosas"] + 
        resumen_avanzadas["pruebas_exitosas"] + 
        resumen_edge["pruebas_exitosas"]
    )
    
    total_fallidas = total_pruebas - total_exitosas
    tasa_exito_general = (total_exitosas / total_pruebas) * 100 if total_pruebas > 0 else 0
    
    print(f"Total de pruebas ejecutadas: {total_pruebas}")
    print(f"Pruebas exitosas: {total_exitosas}")
    print(f"Pruebas fallidas: {total_fallidas}")
    print(f"Tasa de éxito general: {tasa_exito_general:.1f}%")
    print("=" * 60)
    
    return {
        "total_pruebas": total_pruebas,
        "pruebas_exitosas": total_exitosas,
        "pruebas_fallidas": total_fallidas,
        "tasa_exito": tasa_exito_general,
        "resumenes": {
            "basicas": resumen_basicas,
            "avanzadas": resumen_avanzadas,
            "edge": resumen_edge
        }
    }

def main():
    """Función principal para ejecutar las pruebas."""
    try:
        resumen_general = ejecutar_todas_las_pruebas()
        
        if resumen_general["tasa_exito"] >= 80:
            print("\n🎉 ¡PRUEBAS EXITOSAS! El clasificador funciona correctamente.")
        elif resumen_general["tasa_exito"] >= 60:
            print("\n⚠️  PRUEBAS PARCIALMENTE EXITOSAS. Hay algunos casos que necesitan atención.")
        else:
            print("\n❌ PRUEBAS FALLIDAS. El clasificador necesita mejoras.")
            
    except Exception as e:
        print(f"\n❌ Error al ejecutar las pruebas: {e}")

if __name__ == "__main__":
    main()
