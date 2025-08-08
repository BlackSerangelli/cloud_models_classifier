"""
Módulo que contiene los casos de prueba para el clasificador de modelos de nube.
"""

from typing import List, Dict, Any

class CasosPrueba:
    """Clase que contiene todos los casos de prueba para el clasificador."""
    
    @staticmethod
    def obtener_casos_basicos() -> List[Dict[str, Any]]:
        """
        Retorna los casos de prueba básicos con texto y resultado esperado.
        
        Returns:
            List[Dict[str, Any]]: Lista de casos de prueba
        """
        return [
            {
                "texto": "AWS EC2 proporciona servidores virtuales escalables en la nube",
                "modelo_esperado": "IaaS",
                "descripcion": "Servicio de infraestructura con servidores virtuales"
            },
            {
                "texto": "Heroku ofrece una plataforma para desplegar aplicaciones web fácilmente",
                "modelo_esperado": "PaaS",
                "descripcion": "Plataforma de desarrollo y despliegue"
            },
            {
                "texto": "Salesforce es una aplicación CRM que se accede desde el navegador",
                "modelo_esperado": "SaaS",
                "descripcion": "Aplicación de software accesible desde navegador"
            },
            {
                "texto": "AWS Lambda ejecuta funciones sin servidor basadas en eventos",
                "modelo_esperado": "FaaS",
                "descripcion": "Servicio de funciones sin servidor"
            },
            {
                "texto": "Google Cloud Storage es un servicio de almacenamiento en la nube",
                "modelo_esperado": "IaaS",
                "descripcion": "Servicio de almacenamiento de infraestructura"
            },
            {
                "texto": "Docker y Kubernetes para orquestación de contenedores",
                "modelo_esperado": "PaaS",
                "descripcion": "Plataforma de contenedores y orquestación"
            },
            {
                "texto": "Microsoft Office 365 es una suite de productividad en la nube",
                "modelo_esperado": "SaaS",
                "descripcion": "Suite de software como servicio"
            },
            {
                "texto": "Azure Functions permite ejecutar código sin gestionar servidores",
                "modelo_esperado": "FaaS",
                "descripcion": "Servicio de funciones sin servidor"
            },
            {
                "texto": "Necesito CPU, RAM y disco duro para mi aplicación",
                "modelo_esperado": "IaaS",
                "descripcion": "Recursos de infraestructura básicos"
            },
            {
                "texto": "Base de datos MySQL en la nube con autenticación",
                "modelo_esperado": "PaaS",
                "descripcion": "Servicio de base de datos en plataforma"
            }
        ]
    
    @staticmethod
    def obtener_casos_avanzados() -> List[Dict[str, Any]]:
        """
        Retorna casos de prueba más complejos y específicos.
        
        Returns:
            List[Dict[str, Any]]: Lista de casos de prueba avanzados
        """
        return [
            {
                "texto": "Amazon RDS proporciona bases de datos relacionales gestionadas",
                "modelo_esperado": "PaaS",
                "descripcion": "Base de datos gestionada como plataforma"
            },
            {
                "texto": "Netflix streaming de películas y series online",
                "modelo_esperado": "SaaS",
                "descripcion": "Aplicación de entretenimiento como servicio"
            },
            {
                "texto": "Google Cloud Functions para procesamiento de eventos",
                "modelo_esperado": "FaaS",
                "descripcion": "Funciones sin servidor para eventos"
            },
            {
                "texto": "DigitalOcean droplets para servidores virtuales",
                "modelo_esperado": "IaaS",
                "descripcion": "Servidores virtuales de infraestructura"
            },
            {
                "texto": "Slack para comunicación y colaboración en equipos",
                "modelo_esperado": "SaaS",
                "descripcion": "Aplicación de comunicación como servicio"
            }
        ]
    
    @staticmethod
    def obtener_casos_edge() -> List[Dict[str, Any]]:
        """
        Retorna casos de prueba edge (límite) para validar robustez.
        
        Returns:
            List[Dict[str, Any]]: Lista de casos de prueba edge
        """
        return [
            {
                "texto": "Servicio de nube para aplicaciones",
                "modelo_esperado": "No determinado",
                "descripcion": "Texto genérico sin contexto específico"
            },
            {
                "texto": "Plataforma de desarrollo en la nube",
                "modelo_esperado": "PaaS",
                "descripcion": "Texto con palabras clave de PaaS"
            },
            {
                "texto": "Software como servicio en la nube",
                "modelo_esperado": "SaaS",
                "descripcion": "Texto con palabras clave de SaaS"
            },
            {
                "texto": "Infraestructura como servicio cloud",
                "modelo_esperado": "IaaS",
                "descripcion": "Texto con palabras clave de IaaS"
            },
            {
                "texto": "Funciones como servicio serverless",
                "modelo_esperado": "FaaS",
                "descripcion": "Texto con palabras clave de FaaS"
            }
        ]
    
    @staticmethod
    def obtener_todos_los_casos() -> List[Dict[str, Any]]:
        """
        Retorna todos los casos de prueba combinados.
        
        Returns:
            List[Dict[str, Any]]: Lista completa de casos de prueba
        """
        casos_basicos = CasosPrueba.obtener_casos_basicos()
        casos_avanzados = CasosPrueba.obtener_casos_avanzados()
        casos_edge = CasosPrueba.obtener_casos_edge()
        
        return casos_basicos + casos_avanzados + casos_edge
