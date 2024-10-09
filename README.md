# AtividadeFase2_Cap6_FIAP

### Cenário de Utilização
Este código propõe um modelo de solução para uma aplicação em Python voltada para a **Gestão de Qualidade de Sementes** no setor agrícola. O sistema foi desenvolvido para monitorar e controlar a qualidade dos lotes de sementes, oferecendo uma interface interativa para gerenciar os dados e gerar relatórios detalhados.
Através deste sistema, o agricultor ou gerente de produção poderá monitorar, cadastrar, atualizar e excluir lotes de sementes, além de gerar relatórios que garantem que os lotes atendam aos padrões de qualidade necessários para uma produção eficiente e sustentável.

### Funcionalidades do Sistema:
O software oferece uma interação completa com um banco de dados, onde os dados dos lotes de sementes são armazenados e geridos. As funcionalidades incluem:

- **Cadastro de novos lotes**: Adiciona novos lotes de sementes ao banco de dados.
- **Atualização de lotes**: Permite modificar as informações de lotes já existentes.
- **Exclusão de lotes**: Remove lotes do banco de dados.
- **Geração de relatórios**: Cria relatórios detalhados dos lotes em formato .txt, que são apresentados ao usuário.
- **Consulta de lotes**: Exibe todos os lotes registrados no banco de dados.
- **Limpeza do banco de dados**: Exclui todos os lotes de sementes registrados.
- 
O sistema armazena e processa as seguintes informações de cada lote de sementes:

- **Número do Lote (Código alfanumérico)**: Usado para rastreabilidade.
- **Data da Colheita (dd/mm/aaaa)**: Para controle de tempo de estocagem.
- **Pureza (%)**: Porcentagem de sementes puras, excluindo impurezas e outras espécies.
- **Taxa de Germinação (%)**: Sementes que germinaram com sucesso em relação ao número total de sementes testadas.
- **Viabilidade (%)**: Percentual de sementes ainda capazes de germinar após um determinado período.
- **Teor de Umidade (%)**: Quantidade de água presente nas sementes.
- **Sanidade (%)**: Presença ou ausência de patógenos, ou contagem de colônias por grama de semente.
- **Peso de Mil Sementes (g)**: Referência para o tamanho e qualidade do lote.

### Padrões de Qualidade Adotados:
- **Pureza**: 98.0%
- **Taxa de Germinação**: 90.0%
- **Viabilidade**: 85.0%
- **Teor de Umidade**: 10.0%
- **Sanidade**: Máximo de 0.5%
- **Peso de Mil Sementes**: 500g, com tolerância de ±5%

# Funcionamento do Código
* O código está separado em menus interativos que permitem ao usuário realizar o cadastro, consulta, atualização e exclusão de lotes de sementes, além de gerar relatórios e exibir dados.
* A navegação no menu é feita por meio da entrada de um número inteiro, que representa a escolha da opção desejada pelo usuário.
* O gerenciamento dos dados de sementes é realizado por funções que lidam com listas e dicionários provenientes do banco de dados, facilitando a manipulação e atualização dos lotes.
* O sistema está modularizado e comentado.

### Bibliotecas para instalação
* oracledb -> utilizado para realizar os comandos com o bando de dados
* pandas -> utilizado para melhorar a apresentação dos dados no terminal 
* os -> responsável por realizar as limpezas no terminal do promp de comando

### Fluxograma do funcionamento

Inicializa o processo de conexão com o banco de dados. Se a conexão for bem sucedida, procede com o fluxo do software, caso contrario informa a mensagem de erro e finaliza o programa

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
- Solicita informações do lote (número, data, pureza, umidade, etc.).
- Armazena o lote no sistema.

Atualizar lote (Opção 2)
- Solicita o número do lote para atualizar.
- Realiza a procura do lote selecionado informando sua existencia ou não
- Permite a atualização dos dados do lote selecionado.

Excluir lote (Opção 3)
- Solicita o número do lote a ser excluído.
- Realiza a procura do lote selecionado informando sua existencia ou não
- Remove o lote do sistema.

Gerar relatório (Opção 4)
- Gera um relatório de qualidade do lote selecionado.
- Realiza a procura do lote selecionado informando sua existencia ou não
- Exibe o relatório no terminal e gera um arquivo txt para o usuário com as informações.

Exibir lotes registrados (Opção 5)
- Exibe todos os lotes registrados no sistema.

Excluir todos os lotes (Opção 6)
- Remove todos os lotes registrados no sistema.

Sair do programa (Opção 7)
- Encerra o programa com uma mensagem de despedida.
