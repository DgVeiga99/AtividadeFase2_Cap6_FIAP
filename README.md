# AtividadeFase2_Cap6_FIAP

# Cenário de Utilização
Este código propõe um modelo de solução para uma aplicação em Python voltada para a **Gestão de Qualidade de Sementes**. O sistema é projetado para gerenciar lotes de sementes utilizados no setor agrícola, oferecendo monitoramento de qualidade e rastreabilidade. A aplicação inclui:

- Registro de lotes de sementes, com dados como número do lote, data da colheita, pureza, e umidade.
- Atualização de dados dos lotes.
- Exclusão de lotes que não atendem aos critérios de qualidade.
- Geração de relatórios para acompanhamento da qualidade dos lotes.
- Exibição de lotes registrados no sistema.
- Uso de uma interface interativa que possibilita navegar pelas opções e processar dados de maneira eficiente.

A aplicação tem como objetivo auxiliar o setor agrícola a garantir que os lotes de sementes atendam aos padrões de qualidade exigidos, contribuindo para uma produção agrícola mais eficiente e sustentável.

# Funcionamento do Código
* O código está separado em menus interativos que permitem ao usuário realizar o cadastro, consulta, atualização e exclusão de lotes de sementes, além de gerar relatórios e exibir dados.
* A navegação no menu é feita por meio da entrada de um número inteiro, que representa a escolha da opção desejada pelo usuário.
* O gerenciamento dos dados de sementes é realizado por funções que lidam com listas e dicionários, facilitando a manipulação e atualização dos lotes.
* Os dados inseridos no sistema são armazenados e geridos para garantir a rastreabilidade dos lotes e fornecer relatórios que auxiliam no controle de qualidade.
* O sistema está modularizado e comentado, facilitando a manutenção e a compreensão por outros programadores.

# Fluxograma do funcionamento
Início – O programa inicia com uma mensagem de saudação e introdução.

Menu Inicial – O usuário escolhe uma das seguintes opções:

- Inserir novo lote;
- Atualizar lote existente;
- Excluir lote;
- Gerar relatório de qualidade;
- Exibir lotes registrados;
- Excluir todos os lotes;
- Sair do programa.

Verificar opção escolhida – O software valida a escolha. Se a entrada for inválida, solicita uma nova.

Inserir novo lote (Opção 1)
- Solicita informações do lote (número, data, pureza, umidade).
- Armazena o lote no sistema.
- Permite ao usuário continuar ou voltar ao menu principal.

Atualizar lote (Opção 2)
- Solicita o número do lote para atualizar.
- Permite a atualização dos dados do lote selecionado.
- Permite continuar ou voltar ao menu principal.

Excluir lote (Opção 3)
- Solicita o número do lote a ser excluído.
- Remove o lote do sistema.
- Permite continuar ou voltar ao menu principal.

Gerar relatório (Opção 4)
- Gera um relatório de qualidade do lote selecionado.
- Exibe o relatório no terminal.
- Permite continuar ou voltar ao menu principal.

Exibir lotes registrados (Opção 5)
- Exibe todos os lotes registrados no sistema.
- Permite continuar ou voltar ao menu principal.

Excluir todos os lotes (Opção 6)
- Remove todos os lotes registrados no sistema.
- Permite continuar ou voltar ao menu principal.

Sair do programa (Opção 7)
- Encerra o programa com uma mensagem de despedida.
