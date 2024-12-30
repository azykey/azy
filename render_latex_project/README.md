
# Projeto de Renderização LaTeX
Este repositório inclui um script para renderizar equações LaTeX em imagens, e um GitHub Action que processa automaticamente arquivos Markdown que contêm LaTeX.

## Como funciona
1. O GitHub Action será acionado sempre que você fizer alterações em arquivos Markdown.
2. Ele rodará o script Python, que converterá as equações LaTeX em imagens e as substituirá no Markdown.

## Arquivos
- `render_latex_markdown.py`: O script Python que renderiza o LaTeX em imagens.
- `.github/workflows/render-latex.yml`: O GitHub Action que automatiza o processo.
