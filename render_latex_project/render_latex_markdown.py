import os
import re
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def render_latex_to_image(latex_code, output_path):
    """
    Renderiza o código LaTeX em uma imagem e salva no caminho especificado.

    Args:
        latex_code (str): Código LaTeX a ser renderizado.
        output_path (str): Caminho para salvar a imagem gerada.
    """
    fig = plt.figure()
    plt.text(0.5, 0.5, f"${latex_code}$", fontsize=30, ha='center', va='center')
    plt.axis('off')  # Desativa os eixos para não aparecerem na imagem
    canvas = agg.FigureCanvasAgg(fig)
    canvas.print_figure(output_path)

def process_markdown(input_file, output_file, image_dir="images"):
    """
    Processa um arquivo Markdown, renderizando as equações LaTeX inline e em bloco como imagens.

    Args:
        input_file (str): Caminho do arquivo Markdown original.
        output_file (str): Caminho do novo arquivo Markdown com as equações renderizadas.
        image_dir (str): Diretório onde as imagens serão salvas (padrão: "images").
    """
    # Verifica se o diretório de imagens existe, caso contrário, cria-o
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Lê o conteúdo do arquivo Markdown
    with open(input_file, 'r') as f:
        content = f.read()

    # Encontrar equações inline: $equação$
    inline_latex_pattern = r"\$(.*?)\$"
    inline_matches = re.findall(inline_latex_pattern, content)

    # Encontrar equações em bloco: $$equação$$
    block_latex_pattern = r"\$\$(.*?)\$\$"
    block_matches = re.findall(block_latex_pattern, content)

    # Substitui as equações inline por imagens
    for idx, match in enumerate(inline_matches):
        image_path = os.path.join(image_dir, f"inline_{idx}.png")
        render_latex_to_image(match, image_path)
        content = content.replace(f"\${match}\$", f"![inline equation]({image_path})")

    # Substitui as equações em bloco por imagens
    for idx, match in enumerate(block_matches):
        image_path = os.path.join(image_dir, f"block_{idx}.png")
        render_latex_to_image(match, image_path)
        content = content.replace(f"\$\$ {match} \$\$", f"![block equation]({image_path})")

    # Escreve o conteúdo processado no novo arquivo Markdown
    with open(output_file, 'w') as f:
        f.write(content)

# Exemplo de uso
input_markdown_file = "seu_arquivo.md"  # Substitua pelo nome do seu arquivo Markdown
output_markdown_file = "seu_arquivo_processado.md"  # Nome do arquivo de saída
process_markdown(input_markdown_file, output_markdown_file)
