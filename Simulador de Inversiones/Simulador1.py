continuar ="si"

while continuar == "si":

    print("=" * 45)
    print("       SIMULADOR DE INVERSIONES")
    print("=" * 45)

    print("\n--- DATOS DE LA INVERSIÓN ---")

    capital = float(input("¿Cuánto dinero quieres invertir? € "))
    while capital < 0:
       print("❌ El capital no puede ser negativo.")
       capital = float(input("Introduce un capital válido: € "))
    aporte_mensual = float(input("¿Cuánto dinero aportarás cada mes? €"))
    while aporte_mensual < 0:
       print("❌ El Aporte mensual no puede ser negativo.")
       aporte_mensual = float(input("Introduce un Aporte mensual válido: € "))
    años = int(input("¿Durante cuántos años? "))
    while años < 0:
        print(" Los años no pueden ser negativos.")
        años = int(input("❌ Introduce una cantidad de años válida: "))
    rentabilidad = float(input("¿Qué rentabilidad anual estimas? % "))
    while rentabilidad < 0:
        print("La rentabilidad no puede ser negativa.")
        rentabilidad = float(input("❌ Introduce una rentabilidad válida: "))

    meses = años * 12
    tasa_mensual = rentabilidad /100/12

    if tasa_mensual == 0:
       valor_aportes = aporte_mensual * meses
    else:
       valor_aportes = aporte_mensual * ((1 + tasa_mensual) ** meses - 1) / tasa_mensual

    resultado = capital * (1 + tasa_mensual)** meses + valor_aportes
    total_aportes_mensuales = aporte_mensual * meses
    total_aportado = capital + total_aportes_mensuales 
    ganancia = resultado - total_aportado
    saldo = capital 

    print("\n--- RESULTADO DE LA INVERSIÓN ---")
    print("-" * 45)

    print("Capital inicial:", capital, "€")
    print("Aportes Mensuales:", round(total_aportes_mensuales,2), "€")
    print("Total Aportado:", round(total_aportado,2), "€")
    print("Años de inversión:", años)
    print("Rentabilidad anual:", rentabilidad, "%")
    print("Capital Final:",round(resultado,2), "€")


    if ganancia > 0:
        print("\n" + "=" * 45)
        print ("La inversión ha generado ganancias de:", round(ganancia,2), "€")
        print("=" * 45)
    elif ganancia == 0:
        print("\n" + "=" * 45)
        print ("La inversión ha quedado en equilibrio.")
        print("=" * 45)
    else:
        print("\n" + "=" * 45)
        print ("La inversión ha generado una pérdida de:", round(abs(ganancia),2), "€")
        print("=" * 45)

    print("\n--- EVOLUCIÓN ANUAL ---")
    print("-" * 45)

    for mes in range (1, meses + 1):
        saldo = saldo * (1 + tasa_mensual)
        saldo = saldo + aporte_mensual
        
        aportado_hasta_ahora = capital + (aporte_mensual * mes)

        if mes %12 == 0:
           año = mes // 12
           ganancia_año = saldo - aportado_hasta_ahora
           print ("Año", año, ":", round(saldo,2), "€ | Aportado:", round(aportado_hasta_ahora,2), "€| Ganancia:", round(ganancia_año,2), "€")

    print("\n" + "=" * 45)
    print("          FIN DE LA SIMULACIÓN")
    print("=" * 45)

    continuar = input("¿Quieres hacer otra simulación? si/no ").lower()
