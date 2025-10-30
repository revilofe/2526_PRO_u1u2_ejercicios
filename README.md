# Práctica 005 - Programación Modular y Algorítmica

## 📋 Descripción

Esta práctica contiene **10 ejercicios** que combinan algorítmica y problemas del mundo real para desarrollar habilidades de programación estructurada y modular. Los ejercicios están diseñados para ser evaluados automáticamente mediante tests unitarios en GitHub Classroom.

## 🎯 Objetivos de Aprendizaje

- ✅ Desarrollar algoritmos para resolver problemas reales
- ✅ Aplicar programación modular con funciones bien definidas
- ✅ Validar datos de entrada y manejar casos especiales
- ✅ Usar type hints para especificar tipos de datos
- ✅ Documentar código con docstrings
- ✅ Escribir código limpio sin `while True`, `break` o `continue`
- ✅ Aplicar el patrón: **Entrada → Procesamiento → Salida**

---

## 📚 Lista de Ejercicios

### **Ejercicio 01**: Calculadora de Propinas
**Problema**: Calcular propina según calidad del servicio (excelente 20%, bueno 15%, regular 10%)

**Función obligatoria**:
```python
def calcular_propina(importe: float, calidad: str) -> tuple[float, float]:
    """Retorna (propina, total_a_pagar)"""
```

---

### **Ejercicio 02**: Clasificador de Temperaturas
**Problema**: Clasificar temperatura en categorías y determinar si es extrema

**Función obligatoria**:
```python
def clasificar_temperatura(temperatura: float) -> tuple[str, bool]:
    """Retorna (clasificacion, es_extrema)
    Clasificaciones: "Helada", "Frío", "Templado", "Cálido", "Caluroso", "Inválida"
    es_extrema: True si temp < -10 o temp > 40"""
```

---

### **Ejercicio 03**: Contador de Dígitos Pares e Impares
**Problema**: Contar dígitos pares e impares usando solo operaciones matemáticas

**Función obligatoria**:
```python
def contar_digitos_pares_impares(numero: int) -> tuple[int, int]:
    """Retorna (cantidad_pares, cantidad_impares)
    Trabajar SOLO con operaciones matemáticas (% y //)"""
```

---

### **Ejercicio 04**: Calculadora de IMC
**Problema**: Calcular índice de masa corporal y determinar categoría

**Función obligatoria**:
```python
def calcular_imc(peso: float, altura: float) -> tuple[float, str]:
    """Retorna (imc, categoria)
    Categorías: "Bajo peso", "Normal", "Sobrepeso", "Obesidad"
    O mensajes de error: "Datos inválidos", "Peso fuera de rango", "Altura fuera de rango""""
```

---

### **Ejercicio 05**: Conversor de Tiempo
**Problema**: Convertir segundos a formato días, horas, minutos, segundos

**Función obligatoria**:
```python
def convertir_segundos(segundos_totales: int) -> tuple[int, int, int, int]:
    """Retorna (dias, horas, minutos, segundos)"""
```

---

### **Ejercicio 06**: Detector de Años Bisiestos
**Problema**: Determinar si un año es bisiesto y la razón

**Función obligatoria**:
```python
def es_bisiesto(anio: int) -> tuple[bool, int]:
    """Retorna (es_bisiesto, codigo_razon)
    Códigos: 0=fuera_rango, 1=div_400, 2=no_div_400, 3=div_4_no_100, 4=no_div_4"""
```

---

### **Ejercicio 07**: Calculadora de Descuentos Progresivos
**Problema**: Aplicar descuentos por volumen y cliente premium

**Función obligatoria**:
```python
def calcular_precio_final(importe: float, es_premium: bool) -> tuple[float, float, float]:
    """Retorna (descuento_volumen, descuento_premium, precio_final)
    Descuentos por volumen: <100→0%, 100-199→10%, 200-499→15%, ≥500→20%
    Descuento premium: 5% adicional sobre precio ya descontado"""
```

---

### **Ejercicio 08**: Validador de Contraseñas Seguras
**Problema**: Verificar requisitos de seguridad de contraseña

**Función obligatoria**:
```python
def validar_contrasena(contrasena: str) -> tuple[bool, int, int, int, int, int]:
    """Retorna (es_valida, tiene_longitud, tiene_mayuscula, tiene_minuscula, tiene_digito, tiene_especial)
    Requisitos: ≥8 caracteres, mayúscula, minúscula, dígito, carácter especial (!@#$%&*)"""
```

---

### **Ejercicio 09**: Simulador de Carrera de Caracoles
**Problema**: Simular carrera de 3 caracoles con velocidades diferentes

**Función obligatoria**:
```python
def simular_carrera(velocidad1: int, velocidad2: int, velocidad3: int, distancia_meta: int) -> tuple[int, int]:
    """Retorna (ganador, turnos_necesarios)
    ganador: 1, 2 o 3 (o 0 si hay error)
    Velocidades válidas: 1-10 cm/turno"""
```

---

### **Ejercicio 10**: Calculadora de Estadísticas Básicas
**Problema**: Calcular estadísticas de números introducidos por el usuario

**Función obligatoria**:
```python
def calcular_promedio(suma_total: int, cantidad: int) -> float:
    """Retorna promedio (suma/cantidad) o 0.0 si hay error"""
```

---

Consulta [la descripción de cada ejercicio.](PROG-U2.-Practica005.md)

---
## Flujo de Trabajo y Uso de Tests

### **Flujo de Trabajo del Alumno**

1. **Aceptar assignment** → Se crea repositorio personal
2. **Clonar repositorio**:
   ```bash
   git clone https://github.com/tu-organizacion/practica005-nombre-alumno.git
   cd practica005-nombre-alumno
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

   Esto instalará:
   - `pytest` para ejecutar tests
   - `pytest-cov` para medir cobertura de código

4. **Desarrollar un ejercicio** (por ejemplo, ejercicio01.py)

   Los ejercicios deben estar en la carpeta `src/`:
   ```bash
   # Editar el archivo
   nano src/ejercicio01.py
   # o usar tu editor preferido
   code src/ejercicio01.py
   ```

5. **Ejecutar tests localmente**:
   ```bash
   # Test individual
   pytest test/test_ejercicio01.py -v
   
   # Todos los tests
   pytest test/ -v
   
   # Con cobertura de un ejercicio específico
   pytest --cov=ejercicio01 test/test_ejercicio01.py
   
   # Con cobertura de todos los ejercicios
   pytest --cov=src test/ -v
   ```

6. **Commit y push**:
   ```bash
   git add src/ejercicio01.py
   git commit -m "Ejercicio 01 completado"
   git push
   ```

7. **Ver resultados automáticos**:
   - GitHub Actions ejecuta tests automáticamente
   - Ver resultados en pestaña "Actions" del repositorio
   - ✅ Verde = todos los tests pasaron
   - ❌ Rojo = hay errores (ver logs para detalles)


### **Ejecución de Tests Localmente**

```bash
# Ejecutar todos los tests
pytest test/ -v

# Ejecutar solo un ejercicio
pytest test/test_ejercicio01.py -v

# Ver cobertura de código
pytest --cov=src test/ -v

# Ver reporte detallado de cobertura
pytest --cov=src --cov-report=html test/
```

---

## 📊 Evaluación

- ✅ **Tests automáticos**: Los tests validan que tu función obligatoria funciona correctamente
- 📝 **Código limpio**: Documenta tu código con docstrings y comentarios
- 🎯 **Buenas prácticas**: Usa type hints, valida entradas, modulariza el código

---

## 🚀 Comenzar

1. Acepta el assignment de GitHub Classroom
2. Clona tu repositorio
3. Instala dependencias: `pip install -r requirements.txt`
4. Implementa las funciones en `src/ejercicio01.py`, `src/ejercicio02.py`, etc.
5. Ejecuta tests: `pytest test/ -v`
6. Haz commit y push de tus cambios

¡Buena suerte! 🎓
