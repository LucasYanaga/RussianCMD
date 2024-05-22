import time

import SpeakManager as spk
import os
import SoundPlayerManager as spm

ENIGMA_1 = ["Em um reino de letras e cores vibrantes, eu me escondo.",
            "Sob a sombra da máquina que ecoa melodias mecânicas, eu repouso.",
            "Procure-me onde a criatividade encontra forma, e os suspiros da imaginação fluem."]

ENIGMA_2 = ["Eu sou um esconderijo discreto, onde os objetos perdidos são encontrados.",
            "Minha escuridão oferece abrigo para pequenos tesouros esquecidos.",
            "Procure-me onde as memórias ganham vida, enquanto histórias se desdobram na tela."]

ENIGMA_3 = ["Na ponta de quatro lados há um igual. E ao centro momentos são criados.",
            "Amparado pelo chão, um refúgio discreto.",
            "Procure-me onde as pernas descansam e os pés se movem."]

def run():
    spm.init()
    suspense = spm.set_sound("./music/suspense.mp3")
    suspense.play(loops=-1)

    os.system("cls")
    
    spk.enemy_speak("Parabéns! Você foi selecionada para fazer parte da minha equipe secreta de engenheiros robóticos!")
    spk.enemy_speak("Porém antes, precisamos testar suas habilidades para saber se é digna de trabalhar neste cargo sigiloso e de alto risco...")
    spk.enemy_speak("Me chamo Mstislav (" + spk.get_enemy_name() + ") e estarei acompanhando você neste processo.")
    spk.enemy_speak("Serão 3 enigmas no total.")
    spk.enemy_speak("Caso complete todos, receberá um kit completo com todas ferramentas necessárias para trabalhar conosco.")
    spk.enemy_speak("Ah outra coisa...")
    spk.enemy_speak("Grave vídeos durante todo esse processo.")
    spk.enemy_speak("Ao final você enviará esses vídeos para nossa equipe.")
    spk.enemy_speak("Assim será feito uma análise comportamental para avaliarmos se você é apta para trabalhar em uma equipe sigilosa.")
    spk.enemy_speak("Boa sorte... ")

    play_enigma(ENIGMA_1, "EX6BA4", 1)
    play_enigma(ENIGMA_2, "S4U7HL", 2)
    play_enigma(ENIGMA_3, "P26DW9", 3)

    spk.enemy_speak("Parabéns! Você desvendou todos os enigmas!")
    spk.enemy_speak("Agora junte as peças e escaneie o QRCode para desbloquear sua recompensa.")
    spk.enemy_speak("Entre em contato com nossa equipe pelo número +55 (41) 98880-4347 e envie seus vídeos.")
    spk.enemy_speak("Nossa equipe analisará seus comportamentos durante os testes e avaliará se você está apta para trabalhar conosco!")

    time.sleep(5)

    suspense.stop()
    spinnin = spm.set_sound("./music/spinnin.mp3")
    spinnin.play()

    os.system("cls")

    spk.player_speak("Parabéns pelos seus 32 anos meu amorzinho!! ;p", False)
    spk.player_speak("Espero que tenha gostado dessa experiência.", False)
    spk.player_speak("Também espero que goste do presente kkkkkkk", False)
    spk.player_speak("Te amo muito!! <3 <3", False)
    spk.system_speak("Pressione qualquer tecla para sair.")

    import keyboard
    while(True):
        if keyboard.read_event():
            break

def play_enigma(sentences, answer, number):
    correct = spm.set_sound("./music/correct.mp3")
    wrong = spm.set_sound("./music/wrong.mp3")

    for sentence in sentences:
        spk.enigma_speak(sentence, number)

    while(True):
        player_answer = spk.player_input()

        if player_answer.upper().strip() == answer:
            os.system("cls")
            correct.play()
            spk.system_speak("Resposta Correta!")

            break
        else:
            wrong.play()
            spk.system_speak("Resposta errada!")

    if number != 3 :
        spk.enemy_speak("Muito bem! Vamos para a próxima...")


