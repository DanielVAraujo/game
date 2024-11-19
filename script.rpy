define a = Character("Angel")
define l = Character("Lucca")
define t = Character("Thales")
define p = Character("Público")



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

        l "Bom, terminamos mas…o que fazemos?"

        a "Eu não sei ainda…ele me atacou mas acho que foi pra se defender talvez"

        l "Pode ser ele tava com algumas marcas de cortes no corpo fora a bala que retiramos dele, o que será que pode ter acontecido? uma batalha com outro humano?"

        a "Muito provavelmente já vi alguns lutando por mantimentos, território e alguns exércitos de diferentes pessoas querendo lutar contra os infectados por conta própria"

        l "Agora parando pra pensar não é muito difícil isso acontecer mesmo é lamentável, de qualquer forma o melhor a se fazer é esperar ele acordar para perguntar"

        a "Vamos fazer isso então."


        show angel at left with dissolve  
        show lucca at left with dissolve  
          
        show thaleses at right
        t "Onde estou? E quem são vocês?"

        a "Você estava ferido quando nos achamos. Nos atacou, mas perdeu a consciência por conta da grande perda de sangue. Fizemos os primeiros socorros para evitar que morresse."

        t "Ah, sim. Muito obrigado então…"

        l "Mas então, qual é o seu nome? E por que estava tão ferido?"

        hide thaleses
        show thaleses at center with dissolve 

        t "Meu nome é Thales. O motivo de eu estar aqui é que estou com um dos compostos para a cura dessa infestação."

        
        a "O quê? Eu estou à procura de um desses compostos há anos. Como conseguiu?"

       
        t "Bom, a cura vem de um líquido que infectados especiais soltam. Eu os chamei de 'cuspidor'. Esse líquido é semelhante ao ácido sulfúrico. Foi muito difícil manejar esse líquido com minhas ferramentas, porque ele é muito mais corrosivo que ácido, mas finalmente cheguei a um resultado."

        
        a "Então, quer dizer que existem outros tipos de Rottens?"

        
        t "Exatamente. Conforme o tempo foi passando, eles evoluíram e se adaptaram às mudanças. Agora, eles estão absorvendo habilidades de alguns animais. Se eles comerem um peixe ou um pássaro, ganham a habilidade de voar e respirar embaixo d'água."

        
        l "Está muito pior do que pensávamos. Agora temos que lidar com Rottens mais poderosos e com diversas habilidades."

        
        t "De fato. Mas não há mais com o que se preocupar. Eu tenho um dos compostos para a cura."

        
        a "Então, eu não sou a única à procura da cura desse inferno?"

        
        t "Sim. Eu perdi muito e cheguei até aqui, e mesmo que eu morra, quero pelo menos ter achado a cura para tudo isso."

        
        l "Pela lógica, então, temos que procurar a cura nesses tais Rottens especiais?"

        
        t "Só eles têm os compostos necessários para que possamos encontrar a cura."

       
        scene chuva with dissolve

        show  lucca at left with dissolve
        show angeles at center with dissolve 
        a "Já estamos a um mês tentando encontrar a cura… será que estamos perto?"

        show thaleses at right with dissolve
        t "Eu... acho que sim. Só precisamos de mais uma tentativa."

        a "Funciona! A cura... finalmente conseguimos!"

        
        scene cidade with fade

        show angel at center with dissolve
        a "Seis meses depois, 'AntiCarnis' se espalhou por diversas cidades."

        show thales at  right with dissolve
        t "Com a ajuda de sobreviventes, criamos uma base de apoio para disseminar a cura."

        show luccadir at left with dissolve  
        l "E, com o tempo, a cura começou a chegar às últimas cidades restantes."

        
        scene salaciencias with fade

        show angel at left with dissolve
        a "Tudo parecia estar indo bem… até eu descobrir a verdade."

        show luccadir at left with dissolve 
        l "Thales... o que você fez?"

        
        menu:
            "Confrontar Thales diretamente":
                show angel at left with dissolve
                a "O que você está fazendo, Thales? Você sabia o tempo todo, não é?"
                show thales at right with dissolve
                t "Você ainda não entende, Angel? Eu não quero salvar o mundo. Eu quero governá-lo. Eu tenho a cura, e é por isso que estou acima de todos."
            
            "Tentar dialogar com Thales":
                  
                a "Thales, isso não é você... O que aconteceu?"
                
                t "O mundo não merece salvação, Angel. Ele precisa de um novo começo, e eu serei o início. Não há mais lugar para humanos fracos como vocês."

        
        t "A cura... a verdadeira cura... sou eu."

         
        l "Você... Você traiu todos nós, Thales!"
        t "O mundo não merece salvação, Luccas. Ele precisa de um novo começo, e eu serei o início. Não há mais lugar para humanos fracos como vocês."

        
        menu:
            "Lutar contra Thales":
                show angel at center with dissolve
                a "Eu não vou deixar você fazer isso, Thales!"
                hide thales with dissolve
                show thaleses at right with dissolve
                t "Matar? Não. Eu não preciso matar vocês. Não mais. O mundo já está condenado. Eu não preciso de aliados ou inimigos. Preciso apenas de lealdade."
                
                
                menu:
                    "Atacar Thales diretamente":
                        
                        a "Vou acabar com isso agora!"
                        
                        $ defeat = True
                        jump defeated_ending
                    
                    "Tentar negociar":
                        show angeles at center with dissolve  
                        a "Thales, você pode mudar! Podemos reconstruir o mundo!"
                       
                        $ defeat = False
                        jump thales_victory

            "Tentar convencer Thales a mudar de ideia":
                 
                a "Thales, eu sei que você pode mudar... Isso não precisa ser o fim!"
                
                t "Não há mais o que mudar, Angel. O que vocês chamam de 'cura' nunca foi sobre salvar o mundo. Era sobre controle. E agora... eu sou o único com o poder."

                menu:
                    "Atacar Thales diretamente":
                        
                        a "Eu não posso permitir que você continue com isso!"

                       
                        $ defeat = True
                        jump defeated_ending
                    
                    "Tentar negociar":
                        
                        a "Ainda há tempo para mudarmos juntos!"
                       
                        $ defeat = False
                        jump thales_victory

        
        label defeated_ending:
            "Angel dá um soco em Thales e ele cai no chão"
            hide thaleses with dissolve
            "Desesperado, Thales tenta tirar sua arma de seu coldre, mas Angel é mais rápida e dá um tiro na cabeça de Thales"
            a "Thales...volte para o buraco do submundo de onde você saiu...finalmente a cura pode ser distribuída sem mais interferências..."
            scene pordosol with fade
            show luccadir at left with dissolve  
            l "Ainda há muito trabalho a ser feito, mas juntos, podemos reconstruir o mundo."
            show angel at center with dissolve
            a "Com a ajuda dos sobreviventes, a cura será espalhada por todo o planeta, e a esperança renascerá."

            "Fim. O mundo foi salvo, e a humanidade teve uma nova chance."

            return

        label thales_victory:
            hide thales with dissolve
            show thaleses at right with dissolve
            t "Eu sou o novo líder do mundo. E vocês... estão apenas no meu caminho."
            show angel at left with dissolve
            a "Thales, não faça iss-"

            hide angel with dissolve 
            "Thales atira em Angel, a matando"

            l "Thales...SEU MALDITO!!!"

            show luccadir at center with dissolve 

            "Luccas avança para atacar Thales, mas acaba tendo o mesmo destino que Angel, sendo acertado por uma bala"

            hide luccadir with dissolve

            t "Não ousem atrapalhar meu império, vocês apenas serviram de peões para meu plano..."

            scene publico with fade

            "Thales, agora sendo um falso herói, comanda a humanidade em prol de sua vontade"

            p "THALES! THALES! THALES!"



            return


