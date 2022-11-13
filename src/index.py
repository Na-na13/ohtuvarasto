from varasto import Varasto

def tulosta_varasto(varasto):
    print(f"{varasto}")

def tulosta_varasto_otsikolla(varasto, otsikko):
    print(f"{otsikko.title()}varasto: {varasto}")

def varasto_getterien_tulostaja(varasto, tuote):
    print(f"{tuote.title()} getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def varasto_setterien_tulostaja(varasto, tuote):
    print(f"{tuote.title()} setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    tulosta_varasto_otsikolla(varasto, tuote)
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    tulosta_varasto_otsikolla(varasto, tuote)

def virhetilannetulostaja(tilavuus, alkusaldo=0):
    if alkusaldo == 0:
        print(f"Varasto({tilavuus})")
    else:
        print(f"Varasto({tilavuus}, {alkusaldo})")
    huono = Varasto(tilavuus, alkusaldo)
    tulosta_varasto(huono)

def lisaa_varastoon_tulostaja(varasto, tuote, maara):
    tulosta_varasto_otsikolla(varasto, tuote)
    print(f"{tuote}.lisaa_varastoon({maara})")
    varasto.lisaa_varastoon(maara)
    print(f"{tuote.title()}varasto: {varasto}")

def ota_varastosta_tulostaja(varasto, tuote, maara):
    tulosta_varasto_otsikolla(varasto, tuote)
    print(f"{tuote}.otaVarastosta({maara})")
    saatiin = varasto.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"{tuote.title()}varasto: {varasto}")





def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulosta_varasto_otsikolla(mehua, "mehu")
    tulosta_varasto_otsikolla(olutta, "olut")

    varasto_getterien_tulostaja(olutta, "olut")
    varasto_setterien_tulostaja(mehua, "mehu")

    print("Virhetilanteita:")
    virhetilannetulostaja(-100.0)
    virhetilannetulostaja(100.0, -50.7)

    lisaa_varastoon_tulostaja(olutta, "olut", 1000.0)
    lisaa_varastoon_tulostaja(mehua, "mehu", -666.0)

    ota_varastosta_tulostaja(olutta, "olut", 1000.0)
    ota_varastosta_tulostaja(mehua, "mehu", -32.9)


if __name__ == "__main__":
    main()
