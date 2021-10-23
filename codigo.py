#from signal import pause

import phonenumbers

#telefone = "+5527997158002"
retorno = "y"
while retorno != "n":
    print("Digite o numero EX: +5521987654321 ")
    telefone = input()

    

#print(telefone)

#input("Digite o numero telefonico: "+telefone)

    telefone_ajustado = phonenumbers.parse(telefone)
    print(telefone_ajustado)

# descobri a localizacao do telefone
    from phonenumbers import geocoder
    local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
    print(local)

    telefone_formulario = telefone
    telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, " BR")
    telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,
                                                phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print(telefone_formatado)

# descobrir operadora
    from phonenumbers import carrier
    operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
    print(operadora)
    print("Se quiser fazer outra pesquisa e so teclar entre, se nao Feche manualmente")
    retorno = input("")