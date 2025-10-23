import numpy as np

# Ejercicio 1: Votación representante estudiantil
np.random.seed(0)  
votos = np.random.randint(1, 31, size=5000) 
candidatos, conteo = np.unique(votos, return_counts=True)
orden = np.argsort(conteo)[::-1]  

print("Resultados de la votacion:")
for i in range(10):  
    cand = candidatos[orden[i]]
    cnt = conteo[orden[i]]
    porcentaje = (cnt/5000)*100
    print(f"Candidato {cand}: {cnt} votos ({porcentaje:.1f}%)")

print(f"\nTotal votos: {len(votos)}")
print(f"Ganador: candidato {candidatos[orden[0]]} con {conteo[orden[0]]} votos")

# Ejercicio 2: Base de datos estudiantes UIS
np.random.seed(42)
n = 6500
codigos = np.random.randint(2000000, 2999999, n)

nombres = []
for i in range(n):
    nombres.append(f'estudiante{i+1}')
nombres = np.array(nombres)

promedios = np.random.uniform(1.5, 4.8, n)
buenos = np.random.randint(0, n, 200)  
promedios[buenos] = np.random.uniform(4.2, 5.0, len(buenos))
promedios = np.round(promedios, 2)

# Carreras disponibles en la UIS
carreras_lista = ['BIOLOGIA', 'FISICA', 'LIC_MATEMATICAS', 'MATEMATICAS', 'QUIMICA', 
                  'DISEÑO_INDUSTRIAL', 'ING_CIVIL', 'ING_IA', 'ING_ELECTRICA', 'ING_ELECTRONICA',
                  'ING_INDUSTRIAL', 'ING_MECANICA', 'ING_SISTEMAS', 'ING_BIOMEDICA', 'ING_CIENCIA_DATOS',
                  'GEOLOGIA', 'ING_METALURGICA', 'ING_PETROLEOS', 'ING_QUIMICA', 'DERECHO',
                  'ECONOMIA', 'FILOSOFIA', 'HISTORIA_ARCHIVISTICA', 'LIC_EDUCACION_BASICA', 
                  'LIC_LITERATURA', 'LIC_LENGUAS_EXTRANJERAS', 'LIC_MUSICA', 'TRABAJO_SOCIAL',
                  'ENFERMERIA', 'FISIOTERAPIA', 'MEDICINA', 'MICROBIOLOGIA', 'NUTRICION',
                  'ADMIN_AGROINDUSTRIAL', 'ARTES_PLASTICAS', 'ARQUITECTURA', 'GESTION_EMPRESARIAL',
                  'ING_CONSTRUCCION', 'ING_FORESTAL', 'TURISMO', 'ZOOTECNIA']

pesos = np.ones(len(carreras_lista))
pesos[carreras_lista.index('ING_SISTEMAS')] = 3
pesos[carreras_lista.index('ING_INDUSTRIAL')] = 2.5
pesos[carreras_lista.index('MEDICINA')] = 2
pesos[carreras_lista.index('DERECHO')] = 2
pesos[carreras_lista.index('ING_CIVIL')] = 1.8
pesos = pesos / np.sum(pesos)

carreras = np.random.choice(carreras_lista, n, p=pesos)

años = []
for i in range(n):
    if np.random.random() < 0.7: 
        año = np.random.randint(2018, 2024)
    else:
        año = np.random.randint(1995, 2018)
    años.append(año)
ingresos = np.array(años)

condicional = np.random.choice([True, False], n, p=[0.15, 0.85])

print("\n" + "="*50)
print("SISTEMA DE CONSULTAS UIS")
print("="*50)

def buscar_carrera():
    # Buscar estudiantes por carrera y promedio mínimo
    print("\nCarreras disponibles:", ', '.join(np.unique(carreras)))
    carrera = input("Carrera a buscar:").upper()
    
    if carrera not in carreras:
        print("No se encontró la carrera especificada.")
        return
        
    try:
        prom_min = float(input("Promedio minimo (default 4.0): ") or "4.0")
    except:
        prom_min = 4.0
    
    mask = (carreras == carrera) & (promedios >= prom_min)
    encontrados = np.where(mask)[0]
    
    if len(encontrados) == 0:
        print(f"No hay estudiantes de {carrera} con promedio >= {prom_min}")
        return
    
    print(f"\nEstudiantes encontrados: {len(encontrados)}")
    print("Codigo      Nombre          Promedio  Año")
    print("-" * 45)
    
    mostrar = min(20, len(encontrados))
    for i in range(mostrar):
        idx = encontrados[i]
        print(f"{codigos[idx]}  {nombres[idx]:15} {promedios[idx]:6.2f}   {ingresos[idx]}")
    
    if len(encontrados) > 20:
        print(f"... y {len(encontrados)-20} mas")

def buscar_historicos():
    # Estudiantes antiguos en condición condicional
    año_limite = int(input("Ingrese año limite (default 2000): ") or "2000")
    
    mask = (ingresos < año_limite) & (condicional == True)
    encontrados = np.where(mask)[0]
    
    if len(encontrados) == 0:
        print(f"No hay estudiantes de antes de {año_limite} que esten condicionales")
        return
        
    print(f"\nEstudiantes historicos condicionales: {len(encontrados)}")
    print("Codigo      Nombre          Carrera  Promedio  Año")
    print("-" * 50)
    
    for i in range(len(encontrados)):
        idx = encontrados[i]
        print(f"{codigos[idx]}  {nombres[idx]:25} {carreras[idx]:12} {promedios[idx]:6.2f}   {ingresos[idx]}")

def estadisticas():
    print(f"\nTotal estudiantes: {n}")
    print(f"Promedio general: {np.mean(promedios):.2f}")
    
    carr_unicas, conteos = np.unique(carreras, return_counts=True)
    print("\nPor carreras:")
    for carr, cont in zip(carr_unicas, conteos):
        print(f"{carr}: {cont} estudiantes")
    
    total_cond = np.sum(condicional)
    print(f"\nCondicionales: {total_cond} ({100*total_cond/n:.1f}%)")

while True:
    print("\n1. Buscar por carrera")
    print("2. Estudiantes historicos condicionales")  
    print("3. Estadisticas")
    print("4. Salir")

    op = input("\nSeleccione una opción: ")
    
    if op == '1':
        buscar_carrera()
    elif op == '2':
        buscar_historicos()
    elif op == '3':
        estadisticas()
    elif op == '4':
        print("Se ha cerrado la sesión.")
        break
    else:
        print("Opción inválida")