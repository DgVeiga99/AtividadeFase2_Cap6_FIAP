#============================================================================================================
#                    ATIVIDADE FASE 2 - Capítulo 6 - Gestão de Qualidade de Sementes
#============================================================================================================
#                                   GESTÃO DE QUALIDADE DE SEMENTES
#------------------------------------------------------------------------------------------------------------
"""
# Autor.....: Diego Nunes Veiga
# RM........: 560658
# Turma.....: Graduação - 1TIAOR
# Data......: 09/10/2024
# Assunto...: GESTÃO DE QUALIDADE DE SEMENTES
# Função....: Realizar a conexão com o banco de dados possibilitando cadastrar, consultar, atualizar e excluir
              lotes das sementes colocadas para estoque e gerar um relatório aprovando ou não o lote.
"""

#============================================================================================================
#                        INFORMAÇÕES COLETADAS PARA DESENVOLVIMENTO DO SOFTWARE
#============================================================================================================

# Após realizar uma pesquisa, foi escolhido o setor de insumos focado no controle de qualidade das sementes.O sistema de Gestão de Qualidade de
# Sementes tem como objetivo oferecer uma solução tecnológica para o monitoramento e controle da qualidade de sementes utilizadas no setor
# agrícola. Através de uma interface, o software será capaz de gerenciar dados de diversos lotes de sementes, oferecendo insights valiosos
# para o agricultor ou gerente de produção. Com esse sistema, o usuário poderá acompanhar e garantir que os lotes de sementes atendam aos
# padrões de qualidade necessários para uma produção agrícola eficiente e sustentável.

# Guardaremos os seguintes dados
#   * Número do Lote (Código alfanumérico) - Utilizado para rastreabilidade
#   * Data da colheita (dd/mm/aaaa) - Utilizado para controle de tempo estocado
#   * Pureza (%) - porcentagem de sementes puras no lote, excluindo impurezas e outras espécies de sementes.
#   * Taxa de Germinação(%) - sementes que germinaram com sucesso em relação ao número total de sementes testadas.
#   * Viabilidade (%) - sementes que ainda são capazes de germinar após um determinado período
#   * Teor de Umidade (%) - quantidade de água presente nas sementes
#   * Sanidade(%) - Presença/ausência de patógenos específicos ou contagem de colônias por grama de semente
#   * Peso de Mil sementes (g) - referência para o tamanho e a qualidade do lote de sementes.

# Para os valores padrões de qualidade adotaremos:
#   * Pureza - 98.0%
#   * Taxa de Germinação = 90.0%
#   * Viabilidade - 85.0%
#   * Teor de Umidade - 10.0%
#   * Sanidade(%) - até 0.5%
#   * Peso de Mil sementes (g) - 500g com tolerância de +/-5%

# O Software traz alguns benefícios como a interação completa com o banco de dados que contem os dados dos lotes de sementes, assim podemos
# ususfruir de alguns recursos como:
#   * Cadastro de novos lotes de sementes no banco de dados
#   * Atualização de lotes existentes no banco de dados
#   * Exclusão de um lote existente no banco de dados
#   * Geração de relatório do lote num arquivo txt e apresentado ao usuário após solicitação do comando
#   * Consulta completa de todos os lotes registrados no banco de dados
#   * Limpeza completa do banco de dados

#============================================================================================================
#                                       PROCEDIMENTOS E FUNÇÕES
#============================================================================================================

# Importação dos módulos
import os
import oracledb
import pandas as pd


# Apresentação do software
def Apresentação():
    print("=" * 80)
    print(" " * 25 + "GESTÃO DE QUALIDADE DE SEMENTES")
    print("=" * 80)


# Apresentação do menu inicial
def MenuInicial():
    print("\nSelecione a operação que deseja executar:")
    print(f'''
       1 - Inserir lote
       2 - Atualizar lote
       3 - Excluir lote
       4 - Gerar relatório
       5 - Exibir lotes registrados
       6 - Excluir lotes registrados
       7 - SAIR''')


# Validação do comando de menu
def ValidaComando(cmd:int) -> int:
    while cmd not in range(1, 8):
        print("Comando inválido!")
        cmd = int(input("Digite novamente o comando:"))
    return cmd


# Cadastro do novo lote no banco de dados
def NovoLote() -> None:
    try:
        print("Preencha os dados para registro no sistema")
        L = input("Lote: ")
        DC = input("Data de colheita: ")
        Pu = float(input("Pureza(%): "))
        G= float(input("Taxa de Germinação(%): "))
        V = float(input("Viabilidade(%): "))
        U = float(input("Teor de Umidade(%): "))
        S = float(input("Sanidade(%): "))
        Ps = float(input("Peso Mil sementes(g): "))
        bd_comando.execute(f""" INSERT INTO sementes (lote,datacolheita,pureza,germinacao,viabilidade,umidade,sanidade,peso)
                                VALUES ('{L}','{DC}','{Pu}','{G}','{V}','{U}','{S}','{Ps}') """)
        conn.commit()
        print("\nOs dados foram armazenados...\n")

    except ValueError:
        print("\nA variável não é numérica\n")
    except:
        print("\nErro de transferência de dados\n")



# Procura lote para realizar a atualização
def ProcuraLote() -> str:
    try:
        lista = []
        cmd = str(input("Qual lote deseja buscar?:"))
        bd_comando.execute("SELECT * FROM sementes WHERE lote = {}".format(cmd))
        data = bd_comando.fetchall()

        for dt in data:
            lista.append(dt)

        if len(lista) == 0: # se não há o id
            print("\nNenhum registro encontrado!\n")
            cmd = "1"
        else:
            print("\nArquivo de Lote...: {} existente\n".format(cmd))

    except:
        print("\nErro de transferência de dados\n")
        cmd = "1"
    return cmd


# Atualiza lote existente
def AtualizaLote(lote: str) -> None:
    try:
        print("Preencha os dados para atualizar no sistema")
        DC = input("Data de colheita: ")
        Pu = float(input("Pureza(%): "))
        G = float(input("Taxa de Germinação(%): "))
        V = float(input("Viabilidade(%): "))
        U = float(input("Teor de Umidade(%): "))
        S = float(input("Sanidade(%): "))
        Ps = float(input("Peso Mil sementes(g): "))

        bd_comando.execute(f"UPDATE sementes SET datacolheita='{DC}', pureza='{Pu}', germinacao='{G}', viabilidade='{V}', umidade='{U}', sanidade='{S}', peso='{Ps}' WHERE lote = '{lote}'")
        conn.commit()
        print("\nOs dados foram atualizados...\n")

    except ValueError:
        print("A variável não é numérica\n")


# Comando para excluir lote
def ExcluiLote(lote: str) -> None:
    try:
        bd_comando.execute(f"DELETE FROM sementes WHERE lote='{lote}'")
        conn.commit()
        print("\nO lote foi apagado\n")

    except:
        print("\nErro de transferência de dados\n")


# Cálculo de aprovação e reprovação do lote
def CalculoAprova(lista: list,ref: tuple) -> None:
    resultado = []

    # Realiza comparação dos valores no banco com os padrões
    for i in range(3, len(lista)):
        index = i - 3
        aprova = False

        match i:
            case 3|4|5:
                aprova = lista[i] >= ref[index]

            case 6|7:
                aprova = lista[i] <= ref[index]

            case 8:
                zonamax = ref[index] * 1.05
                zonamin = ref[index] * 0.95
                aprova = zonamin <= lista[i] <= zonamax

        resultado.append("Aprovado" if aprova else "Reprovado")

    return resultado


# Cria o relatório em TXT
def RelatorioTXT(dados: list, result: list, ref: tuple) -> None:

    arq = open(f"RelatorioLote{dados[1]}.txt", "w")
    arq.seek(0)
    arq.write("="*20 + "RELATÓRIO DE QUALIDADE" + "="*20 )
    arq.write("\nRelatório de qualidade das sementes obtemos os valores que estão aprovado e reprovados conforme padrão\n")
    arq.write("VALORES PADRÕES:\n")
    arq.write("\t1.Pureza: acima de {} %\n".format(ref[0]))
    arq.write("\t2.Taxa de Germinação: acima de {} %\n".format(ref[1]))
    arq.write("\t3.Viabilidade: acima de {} %\n".format(ref[2]))
    arq.write("\t4.Teor de Umidade: menor ou igual a {} %\n".format(ref[3]))
    arq.write("\t5.Sanidade: menor ou igual a {} %\n".format(ref[4]))
    arq.write("\t6.Peso Mil sementes: padrão {}(g) com tolerância de +/-5%\n".format(ref[5]))
    arq.write("-"*60 + "\n\n")
    arq.write("ID...............:{} (Número banco de dados)\n".format(dados[0]))
    arq.write("LOTE.............:{}\n".format(dados[1]))
    arq.write("DATA COLHEITA....:{}\n".format(dados[2]))
    arq.write("\t1.Pureza:{} %                  -> {} conforme padrão\n".format(dados[3],result[0]))
    arq.write("\t2.Taxa de Germinação:{} %      -> {} conforme padrão\n".format(dados[4],result[1]))
    arq.write("\t3.Viabilidade:{} %             -> {} conforme padrão\n".format(dados[5],result[2]))
    arq.write("\t4.Teor de Umidade:{} %         -> {} conforme padrão\n".format(dados[6],result[3]))
    arq.write("\t5.Sanidade:{} %                -> {} conforme padrão\n".format(dados[7],result[4]))
    arq.write("\t6.Peso Mil sementes:{}g        -> {} conforme padrão\n".format(dados[8],result[5]))
    arq.close()
    # Apresenta para o usuário o relatório
    arq = open(f"RelatorioLote{busca3}.txt", "r")
    print(arq.read())
    arq.close()


# Rotina para geração do relatório de lote
def GeraRelatorio(lote: str,ref: tuple) -> None:
    lista = []
    bd_comando.execute(f"SELECT * FROM sementes WHERE lote = '{lote}'")
    tabela = bd_comando.fetchall()

    for dt in tabela:
        lista.append(dt)

    # Converte os dados obtidos de lista + tupla para lista
    lista = sorted(lista)
    dados = list(lista[0])

    # Chamada do cálculo para comparar os itens aprovados
    result = CalculoAprova(dados,ref)

    #Chamada para realizar o relatorio txt
    RelatorioTXT(dados,result,padrão)


# Apresenta lista de todos os lotes registrados
def ListaCompleta() -> None:
    lista = []
    bd_comando.execute('SELECT * FROM sementes')
    tabela = bd_comando.fetchall()

    for dt in tabela:
        lista.append(dt)

    # ordena a lista
    lista = sorted(lista)

    # Formatação para apresentar todas a tabela sem exceção
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', None)

    # Gera um DataFrame com os dados da lista utilizando o Pandas
    DadosFormatados = pd.DataFrame.from_records(lista, columns=["ID","Lote","Data de colheita","Pureza(%)","Germinação(%)","Viabilidade(%)","Umidade(%)","Sanidade(%)","Pesos(g)"], index='ID')

    if DadosFormatados.empty:
        print("Nenhum registro encontrado!\n")
    else:
        print(DadosFormatados)


# Exclui todos os registros existentes no banco de dados
def ExcluiCompleto() -> None:
    print("!!!!! O COMANDO IRA EXCLUIR SEU BANCO DE DAODOS POR COMPLETO !!!!!")
    cmd = input("Confirma a exclusão? [S]im ou [N]ÃO?")

    if cmd.upper() == "S":
        bd_comando.execute("DELETE FROM sementes")
        conn.commit()
        bd_comando.execute(" ALTER TABLE sementes MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) ")
        conn.commit()
        print("\nTodos os registros foram excluídos!\n")

    else:
        print("\nOperação cancelada!\n")


#============================================================================================================
#                                          PROGRAMA PRINCIPAL
#============================================================================================================

#Usuário para acessar o banco de dados
user = "RM560658"
password = "010199"
server = 'oracle.fiap.com.br:1521/ORCL'


# Variáveis do processo
padrão = (98.0, 90.0, 85.0, 10.0, 0.5, 500)

#----------------------------------------------------------------------------------------------------------


# Realiza conexão com o servidor do banco de dados
try:
    conn = oracledb.connect(user=user, password=password, dsn=server)
    bd_comando = conn.cursor()

except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
     conexao = True

# Execução do Menu enquanto não for solicitado encerramento
while conexao:

    # Limpa terminal operacional
    os.system('cls')

    # Apresentação do menu de interação
    Apresentação()
    MenuInicial()

    # Entrada do comando de navegação e validação
    try:
        comando = int(input("\nDigite o comando:"))
        menu = ValidaComando(comando)
    except ValueError:
        print("A variável digitada não é numérica")
    else:

        #Limpa terminal operacional
        os.system('cls')

        # Escolha do menu conforme comando
        match menu:

            # ================================ Inserir lote ========================================
            case 1:
                print("----- INSERE NOVO LOTE -----\n")
                NovoLote()

            # =============================== Atualizar lote =======================================
            case 2:
                print("----- ATUALIZA LOTE -----\n")
                busca1 = ProcuraLote()
                if busca1 != "1":
                    AtualizaLote(busca1)

            # ================================= Excluir lote =======================================
            case 3:
                print("----- EXCLUIR LOTE -----\n")
                busca2 = ProcuraLote()
                if busca2 != "1":
                    ExcluiLote(busca2)

            # ============================== Gerar relatório =======================================
            case 4:
                print("----- GERAR RELATÓRIO -----\n")
                busca3 = ProcuraLote()
                if busca3 != "1":
                    GeraRelatorio(busca3,padrão)
                    print("O Relatório do Lote:{} foi gerado e está disponível para consulta\n".format(busca3))

            # =========================== Exibir lotes registrados =================================
            case 5:
                print("----- EXIBIR LOTES REGISTRADOS -----\n")
                ListaCompleta()

            # ========================== Excluir lotes registrados =================================
            case 6:
                print("----- EXCLUIR LOTES REGISTRADOS -----\n")
                ExcluiCompleto()

            # ============================== Sair do programa ======================================
            case 7:
                print("\nEncerrando a interface de usuário...até a proxima!")
                conexao = False

    if conexao:
        #Pausa para verificação dos comandos
        input("Pressione ENTER")