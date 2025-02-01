# Registro de Produção

## Visão Geral

O aplicativo Apontamento é um aplicativo desktop projetado para rastrear dados de produção, incluindo defeitos e tipos de refugo, em um ambiente de manufatura. Ele permite que os usuários insiram várias métricas de produção e visualizem os últimos 10 registros para facilitar o monitoramento e análise.

## Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para o desenvolvimento do aplicativo.
- **PyQt5**: Um conjunto de bindings do Python para as bibliotecas Qt, utilizado para criar a interface gráfica do usuário (GUI).
- **SQLite**: Um banco de dados leve utilizado para armazenar os dados de produção localmente.
- **datetime**: Um módulo embutido do Python para manipulação de datas e horários.

## Funcionalidades

- **Entrada de Dados**: Os usuários podem inserir diversas métricas de produção, incluindo:
  - Data da entrada de produção
  - Turno
  - Processo
  - Máquina
  - Referência
  - Quantidade Produzida
  - Refugos
  - Defeitos e seus tipos associados

- **Armazenamento de Dados**: Todos os dados inseridos são armazenados em um banco de dados SQLite local, permitindo a gestão persistente dos dados.

- **Visualização dos Últimos Registros**: Os usuários podem visualizar os últimos 10 registros em uma janela dedicada, proporcionando acesso rápido aos dados recentes de produção.

- **Validação de Entrada**: O aplicativo inclui validação de entrada para garantir que todos os campos obrigatórios sejam preenchidos corretamente antes do envio.

- **Limpar Formulário**: Os usuários podem limpar o formulário de entrada após o envio dos dados, facilitando a inserção de novos registros.

## Possíveis Melhorias Futuras

- **Autenticação de Usuário**: Implementar autenticação de usuário para restringir o acesso ao aplicativo e manter a integridade dos dados.

- **Visualização de Dados**: Adicionar gráficos e tabelas para visualizar as métricas de produção ao longo do tempo, ajudando os usuários a identificar tendências e padrões.

- **Funcionalidade de Exportação**: Implementar a funcionalidade de exportar dados para os formatos CSV ou Excel para relatórios e análise.

- **Melhoria no Tratamento de Erros**: Aprimorar o tratamento de erros para fornecer mensagens mais informativas e evitar falhas no aplicativo.

- **Testes Unitários**: Adicionar testes unitários para garantir a confiabilidade e estabilidade do aplicativo.

- **Suporte Multilíngue**: Implementar suporte a múltiplos idiomas para atender a um público mais amplo.

- **Implantação**: Criar um instalador para facilitar a distribuição e instalação do aplicativo em diferentes sistemas operacionais.

## Instalação

Para executar o aplicativo, certifique-se de ter o Python e as bibliotecas necessárias instaladas. Você pode instalar os pacotes necessários usando o pip:

```bash
pip install PyQt5
```

Em seguida, clone o repositório e execute o aplicativo:

```bash
git clone https://github.com/seuusuario/apontamento.git
cd apontamento
python gui.py
```

