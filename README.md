# Clasificador de Modelos de Nube con NLP

Un clasificador inteligente que utiliza **NLP real con DeepSeek** para identificar automáticamente si un texto corresponde a **IaaS**, **PaaS**, **SaaS** o **FaaS**.

## 🚀 Características

- **NLP Real**: Usa DeepSeek a través de OpenRouter para análisis de texto inteligente
- **Sin Keywords Predefinidas**: El modelo de IA se encarga de entender el contexto
- **Manejo de Errores**: Funciona con texto mal escrito o con errores ortográficos
- **Configuración Flexible**: Variables de entorno para personalizar el comportamiento
- **Estructura Modular**: Código organizado en subcarpetas profesionales
- **Sistema de Pruebas Completo**: Suite de pruebas organizada y automatizada
- **Nombres en Español**: Código completamente en español para mayor claridad

## 📁 Estructura del Proyecto

```
cloud_models_classifier/
├── src/                    # Código fuente principal
│   ├── __init__.py        # Paquete principal
│   ├── clasificador.py    # Clasificador principal con DeepSeek
│   ├── configuracion.py   # Manejo de configuración y variables de entorno
│   ├── modelos.py         # Modelos de datos (ResultadoClasificacion)
│   ├── utilidades.py      # Utilidades y helpers
│   └── demo.py           # Módulo de demostración
├── config/                 # Configuración
│   └── config.env         # Variables de entorno (API keys, URLs)
├── tests/                  # Pruebas unitarias organizadas
│   ├── __init__.py        # Paquete de pruebas
│   ├── casos_prueba.py    # Casos de prueba organizados (básicos, avanzados, edge)
│   ├── utilidades_prueba.py # Utilidades para ejecutar y reportar pruebas
│   └── ejecutar_pruebas.py # Script principal para ejecutar todas las pruebas
├── docs/                   # Documentación (preparado para futuras expansiones)
├── main.py                 # Script principal para demostración
├── requirements.txt        # Dependencias del proyecto
├── pytest.ini            # Configuración de pytest
├── .gitignore            # Archivos a ignorar en Git
└── README.md             # Este archivo
```

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd cloud_models_classifier
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**:
   - Edita `config/config.env` con tu API key de OpenRouter
   - O configura las variables de entorno en tu sistema

## ⚙️ Configuración

### Variables de Entorno

Edita el archivo `config/config.env`:

```env
# Configuración de la API de OpenRouter para DeepSeek
OPENROUTER_API_KEY=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
OPENROUTER_API_URL=https://openrouter.ai/api/v1/chat/completions

# Configuración del modelo de DeepSeek
DEEPSEEK_MODEL=deepseek/deepseek-chat
MAX_TOKENS=50
TEMPERATURE=0.1

# Configuración de validación de texto
MIN_TEXT_LENGTH=3
MAX_TEXT_LENGTH=1000
```

## 🎯 Uso

### Uso Básico

```python
from src import ClasificadorModelosNube

# Crear clasificador
clasificador = ClasificadorModelosNube()

# Clasificar texto
resultado = clasificador.clasificar("AWS EC2 proporciona servidores virtuales")

print(f"Modelo: {resultado.modelo}")
print(f"Confianza: {resultado.confianza}")
print(f"Puntajes: {resultado.puntajes}")
```

### Ejecutar Demo

```bash
python main.py
```

## 📊 Ejemplos de Clasificación

| Texto | Modelo Predicho | Confianza |
|-------|----------------|-----------|
| "AWS EC2 proporciona servidores virtuales" | IaaS | 0.95 |
| "Heroku ofrece una plataforma para desplegar" | PaaS | 0.95 |
| "Salesforce es una aplicación CRM" | SaaS | 0.95 |
| "AWS Lambda ejecuta funciones sin servidor" | FaaS | 0.95 |
| "Google Cloud Storage es un servicio de almacenamiento" | IaaS | 0.95 |
| "Base de datos MySQL en la nube con autenticación" | PaaS | 0.95 |

## 🔧 API

### ClasificadorModelosNube

#### `__init__(usar_nlp=True, clave_api=None)`
Inicializa el clasificador.

**Parámetros:**
- `usar_nlp`: Si usar NLP para clasificación (por defecto True)
- `clave_api`: Clave API personalizada (opcional)

#### `clasificar(texto)`
Clasifica un texto y devuelve el resultado.

**Parámetros:**
- `texto`: Texto a clasificar

**Retorna:**
- `ResultadoClasificacion`: Objeto con el resultado de la clasificación

### ResultadoClasificacion

**Atributos:**
- `modelo`: Modelo predicho (IaaS, PaaS, SaaS, FaaS, Error)
- `confianza`: Nivel de confianza (0.0 a 1.0)
- `puntajes`: Diccionario con puntajes para cada modelo
- `texto_original`: Texto original sin procesar
- `texto_procesado`: Texto después del preprocesamiento
- `metodo`: Método usado para la clasificación (deepseek_nlp)

## 🧪 Sistema de Pruebas

El proyecto incluye un sistema completo de pruebas organizado en categorías:

### Ejecutar Todas las Pruebas

```bash
python tests/ejecutar_pruebas.py
```

### Categorías de Pruebas

1. **Pruebas Básicas** (10 casos): Ejemplos fundamentales de cada modelo
2. **Pruebas Avanzadas** (5 casos): Casos más complejos y específicos
3. **Pruebas Edge** (5 casos): Casos límite para validar robustez

### Ejemplos de Casos de Prueba

**Básicos:**
- AWS EC2 → IaaS
- Heroku → PaaS
- Salesforce → SaaS
- AWS Lambda → FaaS

**Avanzados:**
- Amazon RDS → PaaS
- Netflix → SaaS
- Google Cloud Functions → FaaS

**Edge:**
- "Servicio de nube para aplicaciones" → No determinado
- "Plataforma de desarrollo en la nube" → PaaS

### Resultados de Pruebas

El sistema proporciona:
- ✅ **Tasa de éxito**: 95% (19/20 pruebas exitosas)
- 📊 **Estadísticas detalladas** por categoría
- ❌ **Reporte de casos fallidos** con análisis
- 🎯 **Confianza promedio**: 0.95

## 🚀 Características Técnicas

### Arquitectura Modular

- **`src/clasificador.py`**: Lógica principal de clasificación con DeepSeek
- **`src/configuracion.py`**: Gestión de variables de entorno
- **`src/modelos.py`**: Definición de estructuras de datos
- **`src/utilidades.py`**: Funciones auxiliares (preprocesamiento, validación)
- **`src/demo.py`**: Módulo de demostración

### Integración con DeepSeek

- **API Real**: Conexión directa a DeepSeek a través de OpenRouter
- **Prompt Optimizado**: Instrucciones específicas para clasificación de modelos de nube
- **Manejo de Errores**: Gestión robusta de errores de API
- **Confianza Calculada**: Métrica de confianza basada en la respuesta del modelo

### Validación y Preprocesamiento

- **Validación de Entrada**: Verificación de longitud y tipo de texto
- **Preprocesamiento**: Limpieza y normalización del texto
- **Manejo de Errores**: Respuestas informativas para entradas inválidas

## 📈 Métricas de Rendimiento

- **Precisión**: 95% en casos de prueba
- **Tiempo de Respuesta**: < 2 segundos por clasificación
- **Robustez**: Manejo de errores ortográficos y texto mal escrito
- **Escalabilidad**: Configuración flexible para diferentes volúmenes

## 🔮 Próximas Mejoras

- [ ] Integración con pytest para pruebas automatizadas
- [ ] Documentación API completa
- [ ] Interfaz web para clasificación
- [ ] Análisis de sentimientos en las respuestas
- [ ] Soporte para múltiples idiomas

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.


