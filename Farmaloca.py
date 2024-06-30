import os 
import time
import csv
listaRemedios = [];

def CadastroRemedio(nomeRemedio,tipoRemedio,statusRemedio):
    os.system("cls")
    remedio = [];
    remedio.append(nomeRemedio);
    remedio.append(tipoRemedio);
    remedio.append(statusRemedio);
    listaRemedios.append(remedio);
    IncluindoCSV();
    time.sleep(1);

def EstoqueRemedios():
    if len(listaRemedios) != 0 :
        for i in range(len(listaRemedios)):
            print("");
            print(f"Nome do Remédio:{listaRemedios[i][0]}");
            print(f"Tipo do Remédio:{listaRemedios[i][1]}");
            print(f"Status do Remédio:{listaRemedios[i][2]}");
            print("");
            
            time.sleep(0.5);
    else:
        print("A LISTA ESTÁ VAZIA!!!");
        time.sleep(0.5);    

def AlterandoStatus():
    os.system("cls")
    mudancaRemedio = str(input("Digite o nome do remédio que deseja mudar o status:"));

    if mudancaRemedio != "":
        for remedio in listaRemedios:
            if mudancaRemedio == remedio[0]:
                statusAtt = str(input('Digite qual status deseja adicionar:'));
                remedio[2]= statusAtt;
                time.sleep(1);
    else:
        print("\nÉ necessario digitar algum remédio para prosseguir com o processo de mudança.");
        time.sleep(1);
           
def RemoveRemedio():
    time.sleep(1);
    remedioSelecionado = str(input("Digite o remédio a ser excluído:"))
    for remedio in listaRemedios:
            if remedioSelecionado == remedio[0]:
                verificaExcluir = str(input("Se tem certeza que quer excluir este remédio digite y/s \nCaso não queria apenas dê Enter\n:"))
                if verificaExcluir.lower() == "y" or verificaExcluir.lower() == "s":
                    listaRemedios.remove(remedio);
                    time.sleep(1);
                else:
                    print("Tente novamente se atentando ao nome dos remédios");
                    time.sleep(1);
    IncluindoCSV();
    
def IncluindoCSV():
    with open('lista_remedios.csv', mode ='w', newline ='') as file:
        escrita = csv.writer(file);
        escrita.writerow(["Nome:", "Tipo:", "Status:"]);
        for remedio in listaRemedios:
            escrita.writerow(remedio);
    print("\n - LISTA SALVA - ");
    time.sleep(1);

def CarregandoArquivoCsv():
    with open('lista_remedios.csv', mode ='r') as file:
        lendoArquivo = csv.reader(file);
        next(lendoArquivo);
        for remedios in lendoArquivo:
            listaRemedios.append(remedios);
    print("\n - lEITURA REALIZADA - ");

def Logo():    
    print("""
    ███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░██╗░░░░░░█████╗░░█████╗░░█████╗░
    ██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗
    █████╗░░███████║██████╔╝██╔████╔██║███████║██║░░░░░██║░░██║██║░░╚═╝███████║
    ██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░░░░██║░░██║██║░░██╗██╔══██║
    ██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝ \n""");

def Topicos():
    print("");
    print("1. Cadastrar");
    print("2. Lista remédios");
    print("3. Alterar estado do remédio");
    print("4. Remover item da lista")
    print("5. Sair");

def Menu():    
    Topicos();


Logo();
CarregandoArquivoCsv()
escolha = 0;
while escolha != 5:
    print("="*80);
    Menu();
    escolha = int(input("\nSELECIONE UMA DAS OPÇÕES: "));
    if escolha == 1:
        print("");
        CadastroRemedio(input("NOME:"),input("TIPO:"), input("STATUS:"));
        print("\n- REMÉDIO CADASTRADO COM SUCESSO -\n");
    elif escolha ==2:
        print("\n -LISTA DOS REMÉDIOS- ");
        EstoqueRemedios();
    elif escolha ==3:
        print("\n -ALTERANDO STATUS- \n");
        AlterandoStatus();
    elif escolha ==4:
        print("\n -REMOVENDO REMÉDIO- \n");
        RemoveRemedio();
    elif escolha ==5:
        print("DESLOGANDO DO SISTEMA!!");
    else:
        print("Opção invalida!!");