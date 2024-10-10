define a = Character("Angel")
define l = Character("Lucca")

label start:
    scene telapreta

    "Anteriormente em Rotten Carnis, Angel luta para sobreviver ao apocalipse dos Rotten Carnis, infectados que se alimentam de sangue e carne humana."
    "Em meio ao caos do apocalipse, Angel encontra um garoto que estava fugindo de um dos infectados."

    scene apocalipse

    show lucca at right

    l "Socorro!"

    show angel at left

    "Você deseja salvar o garoto?"

    menu:
        "Salvar":
            "Você decide salvar o garoto."
            jump game
        
        "Não salvar":
            "Você foge com medo do infectado."
            jump end_game_transition

label end_game_transition:

    scene telapreta
    "Você perdeu o jogo."

    return

label game:

    "Você pega a sua pistola e dá um tiro no infectado."

    show angel at left

    "O infectado fica atordoado, e de repente, o garoto joga uma bomba nele"

    a "O que foi isso?!"

    show lucca

    l "Uma das minhas pequenas criações."

    a "Como um pirralho como você sabe fazer essas coisas?"

    l "Tive que me virar depois que fiquei sozinho, então aprendi a fazer algumas coisinhas."

    a "Nossa... parece que você não é só um pirralho qualquer, estou impressionada."

    scene telapreta
    with fade

    "Assim que os dois se recuperam do susto e se livram dos restos do infectado, eles se abrigam no bar onde Angel se alojava."

    scene bar
    with fade

    "Nos fundos do bar haviam alguns mantimentos que Angel havia guardado. Ela pega os mantimentos médicos e os usa no garoto, que estava um pouco ferido."

    show angel at left

    a "Está se sentindo melhor, garoto?"

    show lucca

    l "Sim, estou melhor... obrigado."

    hide angel
    hide lucca

    scene fogueira
    with fade
    "Angel faz uma fogueira nos fundos do bar e prepara alguns enlatados para ela e Lucca, que estava preparando um pouco mais de suas bombas caseiras. Curiosa, Angel pergunta:"

    show angel at left

    a "Então garoto, como você acabou assim?"

    "Ele logo muda a expressão para algo mais triste."

    show lucca at right

    l "Bem…eu e minha família nos mudamos para um sítio que meu avô tinha, com a intenção de nos manter em quarentena. Mas essa foi a pior escolha que nós tomamos..."

    l "De repente, animais do sítio começaram a vomitar sangue por causa da 'RC'. Foi um processo muito rápido; eles vomitaram sangue, começaram a apodrecer e, em seguida..."

    l "Morreram."

    a "Sim, eu já sabia disso tudo…Eu era uma cientista"
    l "Ué mas por que “era”? "
    a "Porque agora sou uma sobrevivente"
    "Logo após o diálogo os enlatados ficam prontos e eles comem"

    "Angel que já está acostumada fica de vigilância enquanto Lucca dorme, de manhã logo cedo Angel decide permanecer junto ao garoto"

    "Porque ela pensou consigo mesma:"

    "”Se ele chegou até aqui é porque ele tem algo de especial nele e ele não vai sobreviver só de bombinhas e algumas engenhocas“"
    
    hide angel
    hide lucca

    "E então, tomando essa decisão, Angel pergunta a Lucca se ele quer ficar junto com ela."

    show luccadir at left
    show angeles at right

    "Você quer ficar com Angel?"

    menu:
        "Ficar com Angel":
            "Lucca aceita ficar."
            jump stay_with_angel
        
        "Não Ficar com Angel":
            "Angel entende e segue seu caminho, deixando o menino sozinho no bar."
            jump end_game_transition

label stay_with_angel:
    scene apocalipse2
    with fade
    
    show angel
    show luccadir
    "Já saindo do bar levando os enlatados, Lucca diz que precisa passar numa loja de eletrônicos para pegar algumas peças para suas futuras invenções."
    "Angel concorda, já que acha útil ter alguma de suas invenções para ajudar a combater os infectados."

    scene lojafora
    with fade

    "Depois de andarem para se afastar um pouco dos lugares mais infestados eles acabam vendo um galpão de longe e decidem descansar lá."

    scene loja
    with fade

    show angel
    show luccadir at left 
    "La tinha algumas coisas como veículos e muitas caixas que provavelmente tinha alguns mantimentos, cansados decidem sentar um pouco e preparar algo para comer"
    "Mas eles escutam um barulho nos fundos e decidem verificar, chegando là, colocando a cabeça entre as caixas não encontram nada"
    
    scene galpao
    with fade

    show angel at left
    "Mas Angel é surpreendida por um homem que estava sangrando muito porem o homem que estava fraco e desmaiado."

    "Ajudar o Rapaz?"

    menu:
        "Ajudar":
                "Eles Decidem Ajuda-lo"
                jump help_guy

        "Irem Embora":
                "Eles Decidem Abandona-lo"
                jump end_game_transition

    
    label help_guy:

        show luccadir
        "Angel e Lucca ficam assustados, mas fazem os primeiros socorros no rapaz ferido"

        "Logo após eles discutem sobre o que devem fazer com o rapaz"

        hide luccadir
        show lucca

        l "Bom, terminamos mas…O que fazemos?"

        a "Eu não sei ainda…ele me atacou mas acho que foi pra se defender talvez"

        l "Pode ser ele tava com algumas marcas de cortes no corpo fora a bala que retiramos dele, o que será que pode ter acontecido? uma batalha com outro humano?"

        a "Muito provavelmente já vi alguns lutando por mantimentos, território e alguns exércitos de diferentes pessoas querendo lutar contra os infectados por conta própria"

        l "Agora parando pra pensar não é muito difícil isso acontecer mesmo é lamentável, de qualquer forma o melhor a se fazer é esperar ele acordar para perguntar"

        a "Vamos fazer isso então."
        
    return


