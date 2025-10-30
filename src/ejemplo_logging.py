"""
Ejemplo de Uso de Logging en Python

Descripción:
    Este programa demuestra el uso de todos los niveles de logging en Python:
    - DEBUG: Información detallada para diagnóstico
    - INFO: Confirmación de que las cosas funcionan como se espera
    - WARNING: Indica que algo inesperado sucedió, pero el programa sigue funcionando
    - ERROR: Problema más serio, el programa no pudo ejecutar alguna función
    - CRITICAL: Error grave, el programa puede no poder continuar

Mas info: https://docs.python.org/es/3/howto/logging.html
Autor: Eduardo Fdez
Fecha: 2025-10-30
"""

import logging
import sys
from typing import Optional


# ==================== CONFIGURACIÓN DEL LOGGING ====================

def configurar_logging(nivel: int = logging.DEBUG, archivo: Optional[str] = None) -> None:
    """
    Configura el sistema de logging con formato personalizado.
    
    Args:
        nivel: Nivel mínimo de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        archivo: Si se especifica, guarda los logs en un archivo además de la consola
    """
    # Formato del mensaje de log
    formato = '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    formato_fecha = '%Y-%m-%d %H:%M:%S'
    
    # Configurar handlers
    handlers = [logging.StreamHandler(sys.stdout)]
    
    if archivo:
        handlers.append(logging.FileHandler(archivo, mode='w', encoding='utf-8'))
    
    # Configuración básica
    logging.basicConfig(
        level=nivel,
        format=formato,
        datefmt=formato_fecha,
        handlers=handlers
    )


# ==================== CREACIÓN DEL LOGGER ====================

# Crear logger específico para este módulo
logger = logging.getLogger(__name__)


# ==================== FUNCIONES DE EJEMPLO ====================

def dividir(a: float, b: float) -> float:
    """
    Divide dos números con manejo de errores y logging completo.
    
    Args:
        a: Numerador
        b: Denominador
        
    Returns:
        float: Resultado de la división
        
    Raises:
        ZeroDivisionError: Si b es cero
    """
    logger.debug(f"Iniciando división: {a} / {b}")
    
    if b == 0:
        logger.error(f"Intento de división por cero: {a} / {b}")
        raise ZeroDivisionError("No se puede dividir por cero")
    
    if abs(b) < 0.0001:
        logger.warning(f"División por un número muy pequeño: {b}. Resultado puede ser impreciso")
    
    resultado = a / b
    logger.info(f"División exitosa: {a} / {b} = {resultado}")
    logger.debug(f"Tipo del resultado: {type(resultado)}")
    
    return resultado


def procesar_usuario(nombre: str, edad: int) -> dict:
    """
    Procesa información de un usuario con validaciones y logging.
    
    Args:
        nombre: Nombre del usuario
        edad: Edad del usuario
        
    Returns:
        dict: Información procesada del usuario
    """
    logger.debug(f"Iniciando procesamiento de usuario: nombre='{nombre}', edad={edad}")
    
    # Validar nombre
    if not nombre or nombre.strip() == "":
        logger.error("Nombre vacío o inválido recibido")
        return {"error": "Nombre inválido"}
    
    if len(nombre) < 2:
        logger.warning(f"Nombre muy corto: '{nombre}' (longitud: {len(nombre)})")
    
    # Validar edad
    if edad < 0:
        logger.error(f"Edad negativa recibida: {edad}")
        return {"error": "Edad inválida"}
    
    if edad < 18:
        logger.info(f"Usuario menor de edad: {nombre} ({edad} años)")
        categoria = "menor"
    elif edad < 65:
        logger.info(f"Usuario adulto: {nombre} ({edad} años)")
        categoria = "adulto"
    else:
        logger.info(f"Usuario adulto mayor: {nombre} ({edad} años)")
        categoria = "adulto_mayor"
    
    usuario = {
        "nombre": nombre.strip(),
        "edad": edad,
        "categoria": categoria
    }
    
    logger.debug(f"Usuario procesado correctamente: {usuario}")
    return usuario


def conectar_base_datos(host: str, puerto: int, timeout: int = 5) -> bool:
    """
    Simula una conexión a base de datos con diferentes escenarios de logging.
    
    Args:
        host: Dirección del servidor
        puerto: Puerto de conexión
        timeout: Tiempo máximo de espera en segundos
        
    Returns:
        bool: True si la conexión fue exitosa, False en caso contrario
    """
    logger.debug(f"Intentando conectar a {host}:{puerto} (timeout: {timeout}s)")
    
    # Simular diferentes escenarios
    if puerto < 1 or puerto > 65535:
        logger.critical(f"Puerto inválido: {puerto}. El sistema no puede continuar")
        return False
    
    if host == "localhost" or host == "127.0.0.1":
        logger.info(f"Conectando a servidor local: {host}:{puerto}")
        logger.debug("Conexión local establecida exitosamente")
        return True
    
    if timeout < 1:
        logger.warning(f"Timeout muy bajo: {timeout}s. Puede causar fallos de conexión")
    
    if host.startswith("prod"):
        logger.warning(f"Conectando a servidor de PRODUCCIÓN: {host}")
        logger.info("Conexión a producción establecida")
        return True
    
    if host == "":
        logger.error("Host vacío. No se puede establecer conexión")
        return False
    
    logger.info(f"Conexión establecida a {host}:{puerto}")
    return True


def procesar_archivo(nombre_archivo: str) -> bool:
    """
    Procesa un archivo con manejo completo de errores y logging.
    
    Args:
        nombre_archivo: Ruta del archivo a procesar
        
    Returns:
        bool: True si se procesó correctamente, False en caso contrario
    """
    logger.debug(f"Iniciando procesamiento de archivo: {nombre_archivo}")
    
    if not nombre_archivo:
        logger.critical("Nombre de archivo NULL o vacío. Operación abortada")
        return False
    
    if not nombre_archivo.endswith(('.txt', '.csv', '.json')):
        logger.warning(f"Extensión de archivo no estándar: {nombre_archivo}")
    
    # Simular procesamiento
    try:
        logger.info(f"Abriendo archivo: {nombre_archivo}")
        logger.debug(f"Leyendo contenido de {nombre_archivo}")
        
        # Simular error en algunos casos
        if "error" in nombre_archivo.lower():
            raise IOError(f"Error simulado al leer {nombre_archivo}")
        
        logger.info(f"Archivo {nombre_archivo} procesado correctamente")
        logger.debug(f"Cerrando archivo: {nombre_archivo}")
        return True
        
    except IOError as e:
        logger.error(f"Error de I/O al procesar archivo: {e}")
        return False
    except Exception as e:
        logger.critical(f"Error crítico inesperado: {e}", exc_info=True)
        return False


def calcular_estadisticas(numeros: list[float]) -> dict:
    """
    Calcula estadísticas de una lista de números con logging detallado.
    
    Args:
        numeros: Lista de números
        
    Returns:
        dict: Diccionario con estadísticas calculadas
    """
    logger.debug(f"Calculando estadísticas para {len(numeros)} números")
    
    if not numeros:
        logger.warning("Lista vacía recibida para calcular estadísticas")
        return {"error": "Lista vacía"}
    
    if len(numeros) < 5:
        logger.warning(f"Muestra pequeña: solo {len(numeros)} elementos")
    
    logger.debug(f"Números recibidos: {numeros}")
    
    # Calcular estadísticas
    promedio = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    logger.info(f"Estadísticas calculadas: promedio={promedio:.2f}, max={maximo}, min={minimo}")
    
    if maximo - minimo > 1000:
        logger.warning(f"Gran dispersión en los datos: rango = {maximo - minimo}")
    
    return {
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "cantidad": len(numeros)
    }


# ==================== DEMOSTRACIÓN DE TODOS LOS NIVELES ====================

def demo_niveles_logging() -> None:
    """
    Demuestra el uso de todos los niveles de logging disponibles.
    """
    logger.debug("=" * 70)
    logger.debug("INICIO DE DEMOSTRACIÓN DE NIVELES DE LOGGING")
    logger.debug("=" * 70)
    
    # DEBUG - Información muy detallada, típicamente de interés solo para diagnosticar problemas
    logger.debug("Este es un mensaje DEBUG - información detallada para desarrolladores")
    logger.debug(f"Variables del sistema: Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # INFO - Confirmación de que las cosas están funcionando como se esperaba
    logger.info("Este es un mensaje INFO - confirma que el programa funciona correctamente")
    logger.info("Aplicación iniciada correctamente")
    
    # WARNING - Indica que algo inesperado sucedió o puede suceder (ej: espacio en disco bajo)
    # El software sigue funcionando como se esperaba
    logger.warning("Este es un mensaje WARNING - algo inesperado pero no crítico")
    logger.warning("El sistema está usando el 80% de memoria disponible")
    
    # ERROR - Debido a un problema más serio, el software no pudo realizar alguna función
    logger.error("Este es un mensaje ERROR - el programa no pudo completar una operación")
    logger.error("Falló la conexión a la base de datos, reintentando...")
    
    # CRITICAL - Un error muy grave, indica que el programa puede no poder continuar ejecutándose
    logger.critical("Este es un mensaje CRITICAL - error grave que puede detener el programa")
    logger.critical("Sistema de archivos lleno, no se pueden guardar datos")
    
    logger.debug("=" * 70)
    logger.debug("FIN DE DEMOSTRACIÓN DE NIVELES DE LOGGING")
    logger.debug("=" * 70)


# ==================== PROGRAMA PRINCIPAL ====================

def main() -> None:
    """
    Función principal que demuestra el uso completo de logging.
    """
    # Configurar logging
    # Cambia el nivel a logging.INFO, logging.WARNING, etc. para filtrar mensajes
    configurar_logging(nivel=logging.DEBUG, archivo='app_ejemplo.log')
    #logging.disable(logging.CRITICAL)

    logger.info("="*70)
    logger.info("INICIO DEL PROGRAMA DE EJEMPLO DE LOGGING")
    logger.info("="*70)
    
    # 1. Demostración de todos los niveles
    print("\n--- DEMOSTRACIÓN DE NIVELES DE LOGGING ---")
    demo_niveles_logging()
    
    # 2. Ejemplo de división
    print("\n--- EJEMPLO DE DIVISIÓN ---")
    try:
        resultado1 = dividir(10, 2)
        print(f"Resultado 1: {resultado1}")
        
        resultado2 = dividir(10, 0.00001)
        print(f"Resultado 2: {resultado2}")
        
        resultado3 = dividir(10, 0)  # Esto generará un error
    except ZeroDivisionError as e:
        logger.error(f"Error capturado en main: {e}")
    
    # 3. Ejemplo de procesamiento de usuarios
    print("\n--- EJEMPLO DE PROCESAMIENTO DE USUARIOS ---")
    usuarios = [
        ("Juan Pérez", 25),
        ("María García", 17),
        ("Pedro López", 70),
        ("", 30),  # Nombre inválido
        ("A", 15),  # Nombre muy corto
        ("Ana Torres", -5),  # Edad inválida
    ]
    
    for nombre, edad in usuarios:
        resultado = procesar_usuario(nombre, edad)
        logger.debug(f"Resultado procesamiento: {resultado}")
    
    # 4. Ejemplo de conexión a base de datos
    print("\n--- EJEMPLO DE CONEXIÓN A BASE DE DATOS ---")
    servidores = [
        ("localhost", 5432),
        ("prod-server-01", 3306),
        ("", 5432),  # Host vacío
        ("dev-server", 999999),  # Puerto inválido
        ("backup-server", 8080, 1),  # Timeout bajo
    ]
    
    for config in servidores:
        if len(config) == 2:
            host, puerto = config
            conectar_base_datos(host, puerto)
        else:
            host, puerto, timeout = config
            conectar_base_datos(host, puerto, timeout)
    
    # 5. Ejemplo de procesamiento de archivos
    print("\n--- EJEMPLO DE PROCESAMIENTO DE ARCHIVOS ---")
    archivos = [
        "datos.txt",
        "config.json",
        "reporte.csv",
        "documento.docx",  # Extensión no estándar
        "archivo_con_error.txt",  # Simulará error
        "",  # Archivo vacío
    ]
    
    for archivo in archivos:
        procesar_archivo(archivo)
    
    # 6. Ejemplo de cálculo de estadísticas
    print("\n--- EJEMPLO DE CÁLCULO DE ESTADÍSTICAS ---")
    conjuntos = [
        [10.5, 20.3, 15.7, 30.2, 25.8],
        [1, 2, 3],  # Muestra pequeña
        [100, 1500, 200],  # Gran dispersión
        [],  # Lista vacía
    ]
    
    for i, numeros in enumerate(conjuntos, 1):
        logger.info(f"Procesando conjunto #{i}")
        stats = calcular_estadisticas(numeros)
        print(f"Estadísticas conjunto {i}: {stats}")
    
    logger.info("="*70)
    logger.info("FIN DEL PROGRAMA - Ejecución completada")
    logger.info("="*70)
    logger.info("Logs guardados en: app_ejemplo.log")


if __name__ == "__main__":
    main()

