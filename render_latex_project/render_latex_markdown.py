
import os
import re
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def render_latex_to_image(latex_code, output_path):
    # Renderiza o código LaTeX em uma imagem e salva no caminho especificado
    fig = plt.figure()
    plt.text(0.5, 0.5, f"${latex_code}$", fontsize=30, ha='center', va='center')
    plt.axis('off')  # Desativa os eixos
    canvas = agg.FigureCanvasAgg(fig)
    canvas.print_figure(output_path)

def process_markdown(input_file, output_file, image_dir="images"):
    # Processa um arquivo Markdown, renderizando o LaTeX em imagens
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    with open(input_file, 'r') as f:
        content = f.read()

    # Encontrar equações inline: $equação$
    inline_latex_pattern = r"\$(.*?)\$"
    inline_matches = re.findall(inline_latex_pattern, content)

    # Encontrar equações em bloco: $$equação$$
    block_latex_pattern = r"\$\$(.*?)\$\$"
    block_matches = re.findall(block_latex_pattern, content)

    # Substituir as equações inline por imagens
    for idx, match in enumerate(inline_matches):
        image_path = os.path.join(image_dir, f"inline_{idx}.png")
        render_latex_to_image(match, image_path)
        content = content.replace(f"\${match}\$", f"![inline equation]({image_path})")

    # Substituir as equações em bloco por imagens
    for idx, match in enumerate(block_matches):
        image_path = os.path.join(image_dir, f"block_{idx}.png")
        render_latex_to_image(match, image_path)
        content = content.replace(f"\$\$ {match} \$\$", f"![block equation]({image_path})")

    # Escrever o conteúdo processado no novo arquivo Markdown
    with open(output_file, 'w') as f:
        f.write(content)

# Exemplo de uso
input_markdown_file = "seu_arquivo.md"
output_markdown_file = "seu_arquivo_processado.md"
process_markdown(input_markdown_file, output_markdown_file)
