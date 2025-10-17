# Simple script to convert notebooks to markdown preserving frontmatter
# Usage: python scripts/export_notebooks.py notebooks/first.ipynb --output-dir=site_src

import argparse
import os
import nbformat
from nbconvert import MarkdownExporter


def convert_notebook(nb_path, output_dir):
    nb = nbformat.read(nb_path, as_version=4)

    # Ensure the first cell contains YAML frontmatter with permalink; adjust trailing slash
    if nb.cells and nb.cells[0].cell_type == 'markdown':
        src = nb.cells[0].source
        if 'permalink:' in src and '---' in src:
            # Add trailing slash to permalink if missing
            lines = src.splitlines()
            new_lines = []
            for line in lines:
                if line.strip().startswith('permalink:'):
                    key, val = line.split(':', 1)
                    val = val.strip()
                    # if value not quoted, it might be like /foo
                    if not val.endswith('/') and not val.endswith('.html'):
                        val = val + '/'
                    new_lines.append(f"{key}: {val}")
                else:
                    new_lines.append(line)
            nb.cells[0].source = '\n'.join(new_lines)

    exporter = MarkdownExporter()
    body, resources = exporter.from_notebook_node(nb)

    base = os.path.splitext(os.path.basename(nb_path))[0]
    out_path = os.path.join(output_dir, base + '.md')
    os.makedirs(output_dir, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(body)
    print(f'Converted {nb_path} -> {out_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('notebooks', nargs='+')
    parser.add_argument('--output-dir', default='site_src')
    args = parser.parse_args()
    for nb in args.notebooks:
        convert_notebook(nb, args.output_dir)
