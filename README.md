<div align="center">
  <img src="https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Sourcecode/static/images/logo_ubi_branca.png" alt="Logo UBI" width="300">
</div>

# EWMN Trabalho Prático Final

Aplicação web desenvolvida como Trabalho Prático Final da disciplina de Ecossistemas Web, Móvel e na Nuvem da Universidade da Beira Interior (UBI).

## Descrição

Este projeto consiste na transformação da aplicação de terminal desenvolvida no Trabalho Prático Intermédio em uma aplicação web completa utilizando Flask para o backend e HTML, CSS e JavaScript para o frontend. A aplicação permite realizar conversões entre diferentes sistemas numéricos, gerar tabelas de códigos Gray e realizar operações aritméticas em diferentes bases numéricas.

## Autores

- Afonso Esteves - 55047
- Duarte Azenhas - 55281
- Felipe Dourado - 53394

## Funcionalidades

### Funcionalidades Mínimas
- **FM01 - Tabelas de Códigos Gray**: Geração de tabelas de códigos Gray para n bits, exibindo os equivalentes em decimal e binário.
- **FM02 - Conversão entre Sistemas Numéricos**: Conversões entre binário, decimal e hexadecimal.

### Funcionalidades Adicionais
- **FA01 - Operações Aritméticas**: Adição e subtração em binário e hexadecimal.
- **FA02 - Menu Interativo**: Interface gráfica com navegação intuitiva entre as diferentes funcionalidades.

## Tecnologias Utilizadas

- **Backend**: Python com Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilo**: CSS personalizado com design responsivo

## Estrutura do Projeto

```
sourcecode/
│
├── app.py                        # Aplicação Flask principal
│
├── templates/                    # Arquivos HTML
│   ├── index.html                # Página inicial
│   ├── gray.html                 # Página de geração de tabelas Gray
│   ├── conversao.html            # Página de conversão entre sistemas
│   └── operacoes.html            # Página de operações aritméticas
│
└── static/                       # Arquivos estáticos
    └── images/
        ├── logo_ubi_branca.png   # Logo da UBI
        └── fundo_ubi.png         # Fundo Imagem UBI
```

## Como Executar

1. Certifique-se de ter Python 3.6+ instalado na sua maquina.
2. Crie um ambiente virtual Python desta forma:
    ```
    python -m venv .venv
    ```
3. Instale as dependências:
    ```
    pip3 install flask
    ```
4. Defina as variáveis de ambientes para o Flask:
    ```
    export FLASK_APP=app
    ```
    ```
    export FLASK_ENV=development
    ```
5. Execute a aplicação:
    ```
    flask run
    ```
6. Acesse a aplicação no navegador em `http://localhost:5000`
    

## Funcionalidades em Detalhes

### Tabela de Gray
Permite gerar tabelas de códigos Gray com o número de bits especificado pelo usuário. A tabela exibe os valores em decimal, binário padrão e código Gray correspondente.

### Conversão entre Sistemas Numéricos
Disponibiliza os seguintes tipos de conversão:
- Binário para Decimal
- Decimal para Binário
- Decimal para Hexadecimal
- Hexadecimal para Decimal
- Binário para Hexadecimal
- Hexadecimal para Binário

### Operações Aritméticas
Permite realizar operações de:
- Adição em binário
- Subtração em binário
- Adição em hexadecimal
- Subtração em hexadecimal

## Screenshots

### Landing Page
<div align="center">
  <img src="https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Screenshots/Landing-Page.png" alt="Landing-Page.png" width="800">
</div>

### Página Tabela Gray
<img src="https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Screenshots/Pagina-TabelaGray.png" alt="Pagina-TabelaGray.png" width="800">

### Página Operações Aritmeticas
<img src="https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Screenshots/Pagina-Operacoes.png" alt="Pagina-Operacoes.png" width="800">

### Página Conversor
<img src="https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Screenshots/Pagina-Conversor.png" alt="Pagina-Conversor.png" width="800">

## Relatório Técnico

Para mais detalhes técnicos do projeto, consulte o [Relatório Técnico](https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Relatorio/relatorio.pdf).

## Enunciado do Projeto

Para maiores detalhes sobre o desenvolvimento do projeto, consulte o [Enunciado do Projeto](https://github.com/fefogaca/EWMN-Trabalho-Pratico-Final/blob/main/Enunciado%20do%20Projeto.pdf).

## Licença

Todos os direitos reservados à [Universidade da Beira Interior](https://ubi.pt) e aos autores do projeto.
