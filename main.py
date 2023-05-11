from funcoes import *

if __name__ == "__main__":
    
    while True:
        saudacao = escuta()
        if 'ok sexta-feira' in saudacao:
            abertura()
            while True:
                comando = escuta().lower()
                if "horas" in comando:
                    hora()
                    break

                elif "clima" in comando or "previsão do tempo" in comando:
                    clima()
                    break

                elif "data" in comando:
                    data()
                    break

                elif "toque" in comando:
                    musica = comando.replace("toque", "")
                    tocar(musica)
                    break

                elif "procure por" in comando:
                    comando = comando.replace("procure por", "")
                    buscar(comando)
                    break

                elif "quanto é" in comando:
                    conta(comando)                  
                    break

                elif "o que é" in comando:
                    comando = comando.replace("o que é", "")
                    wiki(comando)
                    break

                elif "bom dia" in comando:
                    bom_dia()
                    break

                elif "boa tarde" in comando:
                    boa_tarde()
                    break

                elif "boa noite" in comando:
                    boa_noite()
                    break

                elif "recomendar filmes" in comando or "recomendar filme" in comando or "fale um filme" in comando or "filme" in comando:
                    buscar_filme()
                    break
                
                elif "jogar" in comando:
                    jogar()
                    break

                elif "tipo de corno" in comando:
                    corno()
                    break

                elif "meu pai morreu hoje" in comando:
                    piada()
                    resposta = escuta()
                    if resposta == "quem é":
                        Speaker("Seu pai que não é")
                        break

                elif "anotar tarefa" in comando or "anotar" in comando:
                    while True:
                        escreva()
                        Speaker('deseja continuar anotando?')
                        resposta = escuta()
                        if continuar(resposta) is not True:
                            Speaker('Tarefas anotadas')
                            break
                    break   

                elif "tirar foto" in comando:
                    tirar_foto()
                    break

                elif "fotos" in comando or "abrir fotos" in comando:
                    abrir_fotos("img")
                    break
                
                elif "listar tarefas" in comando or "mostrar tarefas" in comando:
                    listar_tarefas()
                    break
        elif "tchau" in saudacao or "adeus" in saudacao:
            Speaker("Adeus meu mestre")
            break
        else:
            Speaker('Diga ok sexta feira para iniciar!')