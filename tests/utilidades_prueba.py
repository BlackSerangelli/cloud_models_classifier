"""
Utilidades para las pruebas del clasificador de modelos de nube.
"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Agregar el directorio raíz al path para importar el módulo src
directorio_raiz = Path(__file__).parent.parent
sys.path.insert(0, str(directorio_raiz))

from src import ClasificadorModelosNube, ResultadoClasificacion

class UtilidadesPrueba:
    """Clase con utilidades para las pruebas del clasificador."""
    
    @staticmethod
    def crear_clasificador() -> ClasificadorModelosNube:
        """
        Crea una instancia del clasificador para pruebas.
        
        Returns:
            ClasificadorModelosNube: Instancia del clasificador
        """
        return ClasificadorModelosNube(usar_nlp=True)
    
    @staticmethod
    def ejecutar_prueba(clasificador: ClasificadorModelosNube, caso: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta una prueba individual con el clasificador.
        
        Args:
            clasificador: Instancia del clasificador
            caso: Caso de prueba a ejecutar
            
        Returns:
            Dict[str, Any]: Resultado de la prueba
        """
        texto = caso["texto"]
        modelo_esperado = caso["modelo_esperado"]
        descripcion = caso["descripcion"]
        
        try:
            resultado = clasificador.clasificar(texto)
            
            return {
                "texto": texto,
                "modelo_esperado": modelo_esperado,
                "modelo_obtenido": resultado.modelo,
                "confianza": resultado.confianza,
                "descripcion": descripcion,
                "exito": resultado.modelo == modelo_esperado,
                "error": None,
                "resultado": resultado
            }
        except Exception as e:
            return {
                "texto": texto,
                "modelo_esperado": modelo_esperado,
                "modelo_obtenido": "Error",
                "confianza": 0.0,
                "descripcion": descripcion,
                "exito": False,
                "error": str(e),
                "resultado": None
            }
    
    @staticmethod
    def ejecutar_suite_pruebas(casos: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Ejecuta una suite completa de pruebas.
        
        Args:
            casos: Lista de casos de prueba
            
        Returns:
            Dict[str, Any]: Resumen de resultados de las pruebas
        """
        clasificador = UtilidadesPrueba.crear_clasificador()
        resultados = []
        
        for caso in casos:
            resultado = UtilidadesPrueba.ejecutar_prueba(clasificador, caso)
            resultados.append(resultado)
        
        # Calcular estadísticas
        total_pruebas = len(resultados)
        pruebas_exitosas = sum(1 for r in resultados if r["exito"])
        pruebas_fallidas = total_pruebas - pruebas_exitosas
        tasa_exito = (pruebas_exitosas / total_pruebas) * 100 if total_pruebas > 0 else 0
        
        return {
            "total_pruebas": total_pruebas,
            "pruebas_exitosas": pruebas_exitosas,
            "pruebas_fallidas": pruebas_fallidas,
            "tasa_exito": tasa_exito,
            "resultados": resultados
        }
    
    @staticmethod
    def imprimir_resultado_prueba(resultado: Dict[str, Any], numero: int = None):
        """
        Imprime el resultado de una prueba individual.
        
        Args:
            resultado: Resultado de la prueba
            numero: Número de la prueba (opcional)
        """
        prefijo = f"📋 Prueba {numero}: " if numero is not None else "📋 Prueba: "
        
        print(f"{prefijo}")
        print(f"Texto: {resultado['texto']}")
        print(f"Descripción: {resultado['descripcion']}")
        
        if resultado["error"]:
            print(f"❌ Error: {resultado['error']}")
        else:
            print(f"🎯 Modelo esperado: {resultado['modelo_esperado']}")
            print(f"🎯 Modelo obtenido: {resultado['modelo_obtenido']}")
            print(f"📊 Confianza: {resultado['confianza']:.2f}")
            
            if resultado["exito"]:
                print("✅ Resultado: CORRECTO")
            else:
                print("❌ Resultado: INCORRECTO")
        
        print("-" * 50)
    
    @staticmethod
    def imprimir_resumen_pruebas(resumen: Dict[str, Any]):
        """
        Imprime el resumen de una suite de pruebas.
        
        Args:
            resumen: Resumen de resultados de las pruebas
        """
        print("=" * 60)
        print("📊 RESUMEN DE PRUEBAS")
        print("=" * 60)
        print(f"Total de pruebas: {resumen['total_pruebas']}")
        print(f"Pruebas exitosas: {resumen['pruebas_exitosas']}")
        print(f"Pruebas fallidas: {resumen['pruebas_fallidas']}")
        print(f"Tasa de éxito: {resumen['tasa_exito']:.1f}%")
        print("=" * 60)
        
        # Mostrar casos fallidos si los hay
        casos_fallidos = [r for r in resumen["resultados"] if not r["exito"]]
        if casos_fallidos:
            print("\n❌ CASOS FALLIDOS:")
            for i, caso in enumerate(casos_fallidos, 1):
                print(f"{i}. '{caso['texto']}'")
                print(f"   Esperado: {caso['modelo_esperado']}, Obtenido: {caso['modelo_obtenido']}")
                if caso["error"]:
                    print(f"   Error: {caso['error']}")
                print()
