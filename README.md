## Automação de Publicações no LinkedIn

### Visão Geral
Este software desenvolvido em Python com a biblioteca CustomTkinter, e pyautogui automatiza a publicação de posts no LinkedIn. Ele oferece uma interface gráfica intuitiva para o usuário selecionar imagens, inserir textos e programar a publicação.

### Características Principais
* **Interface Gráfica Amigável:** Design moderno, escuro e responsivo.
* **Seleção de Arquivos:** Permite escolher imagens diretamente do computador.
* **Automação de Publicação:** Integração com o PyAutoGUI para interagir com o LinkedIn.

### Funcionamento
* **Início:** A interface é carregada com as opções básicas.
* **Inserção de Conteúdo:** O usuário digita o texto e escolhe a imagem.
* **Publicação:** Ao clicar em "Publicar", o software realiza as ações de publibar no LinkedIn.

### Detalhes Técnicos
* **Tecnologias:** Python, CustomTkinter, PyAutoGUI, Tkinter.
* **Funcionalidades:**
    * **Interface:** Criação e gerenciamento da interface gráfica.
    * **Automação:** Interação com o navegador para publicar posts.
* **Requisitos:** Python 3.8+, bibliotecas especificadas, computador com acesso à internet.

### Limitações e Melhorias Futuras
* **Limitações:**
    * Utiliza o Position.py para marcar os pontos de click do mouse em resoluções diferentes da recomendada. 
    * Dependência de coordenadas fixas no LinkedIn a aplicação pode falhar dependendo da resolução atual da tela(recomendavel. 1920x1080).
    
* **Melhorias que podem ser implementadas:**
    * Detecção dinâmica de elementos no LinkedIn.
    * Suporte a mais formatos de arquivo.
    
### Arquitetura do Sistema
Aplicação com estrutura modular.


* Implementar [melhoria 1]
* Adicionar [nova funcionalidade]


