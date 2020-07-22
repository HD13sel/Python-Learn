import easygui, sys

easygui.msgbox('Hello, World!')

while 1:

    msg = 'Qual o seu sabor favorito?'
    title = 'Uma pesquisa sobre sorvetes'
    choices = ['Baunilha', 'Chocolate', 'Morango', 'Flocos']
    choice = easygui.choicebox(msg, title, choices)

    # Observe a conversão p/ string de choice abaixo, porque o user pode ter cancelado a escolha, dessa forma seria None
    easygui.msgbox('Voce escolheu: ' + str(choice), 'como resultado da pesquisa.')

    msg = 'Você gostaria de continuar?'
    title = 'Confirmação'
    if easygui.ccbox(msg, title):  # um diálogo de 'Continue/Cancel'
        pass
    else:
        sys.exit()

