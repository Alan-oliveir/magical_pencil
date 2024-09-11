# Magical Pencil: Transformando Imagens em Desenhos com Python e OpenCV
Este projeto é uma aplicação em Python que transforma imagens em desenhos utilizando bibliotecas como OpenCV e PIL, com uma interface gráfica construída com customTkinter.

## Funcionalidades
- Interface gráfica simples para selecionar imagens.
- Transformação de imagens em desenhos realistas.
- Controle da intensidade do efeito de desenho através de um slider.
- Salvamento automático da imagem transformada na pasta output.

## Inspiração
Este projeto foi inspirado pelos seguintes artigos:

1. Tratamento de Imagens com Python, da Hashtag Treinamentos.

   - O artigo discute como manipular imagens com Python usando as bibliotecas OpenCV e PIL, abordando funções básicas como conversão para tons de cinza, inversão de cores e aplicação de filtros de blur.

2. Transformando Imagens em Desenhos Realistas com Python e OpenCV, do UsandoPy.

   - Este artigo apresenta uma abordagem detalhada para transformar imagens em desenhos realistas, usando técnicas de processamento de imagem como inversão de cores e divisão de imagem com blur gaussiano.

## Diferenças em relação aos artigos originais
Embora os dois artigos tenham fornecido a base para este projeto, algumas diferenças e melhorias foram implementadas na versão final:

- Interface gráfica personalizada: Ao contrário dos exemplos originais, o projeto utiliza customTkinter para criar uma interface amigável, permitindo que o usuário selecione a imagem e ajuste o efeito de desenho em tempo real com um slider.
- Controle de intensidade via Slider: Adicionei um controle de intensidade do efeito (parâmetro scale) usando um slider, permitindo ajustes mais finos diretamente na interface.
- Gerenciamento de arquivos: Implementei uma função para salvar automaticamente as imagens processadas em uma pasta específica (output), criando o diretório se necessário.
- Logging e tratamento de erros: O projeto inclui mensagens de log para facilitar o diagnóstico de problemas, bem como tratamento de exceções mais robusto, com feedback claro para o usuário via messagebox.

## Como executar o projeto
### Pré-requisitos
Certifique-se de ter o Python 3.x instalado e as seguintes bibliotecas:
``` bash
pip install customtkinter pillow opencv-python
```
### Execução
Clone este repositório e execute o script principal:
``` bash
python main.py
```
___
## Licença
Este projeto foi desenvolvido como uma demonstração educacional e é de código aberto. No entanto, certifique-se de respeitar os direitos dos autores dos artigos que inspiraram esta implementação.
