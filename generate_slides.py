import os
import re
import glob

def parse_markdown(text):
    lines = text.split('\n')
    html_lines = []
    list_stack = [] # Stores indentation levels
    
    for line in lines:
        # Check for list items
        list_match = re.match(r'^(\s*)\*\s+(.*)', line)
        
        if list_match:
            indent = len(list_match.group(1))
            content = list_match.group(2)
            
            # Manage nesting
            if not list_stack:
                html_lines.append('<ul>')
                list_stack.append(indent)
            else:
                if indent > list_stack[-1]:
                    html_lines.append('<ul>')
                    list_stack.append(indent)
                elif indent < list_stack[-1]:
                    while list_stack and indent < list_stack[-1]:
                        html_lines.append('</ul>')
                        list_stack.pop()
                    if not list_stack or indent > list_stack[-1]:
                        # Should technically not happen in well-formed MD, but handle graceful
                        html_lines.append('<ul>')
                        list_stack.append(indent)
            
            # Format content
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html_lines.append(f'<li>{content}</li>')
            continue
        
        # Not a list item, close all lists
        while list_stack:
            html_lines.append('</ul>')
            list_stack.pop()
            
        stripped = line.strip()
        if not stripped:
            html_lines.append('<br>')
            continue
            
        # Headers
        if line.startswith('# '):
            content = line[2:]
            html_lines.append(f'<h1>{content}</h1>')
        elif line.startswith('## '):
            content = line[3:]
            html_lines.append(f'<h2>{content}</h2>')
        elif line.startswith('### '):
             content = line[4:]
             html_lines.append(f'<h3>{content}</h3>')
        # Normal text
        else:
            content = line
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html_lines.append(f'<p>{content}</p>')
            
    # Close any remaining lists
    while list_stack:
        html_lines.append('</ul>')
        list_stack.pop()
        
    return '\n'.join(html_lines)

files = glob.glob('script_for_diapositiva_*.md')

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        html_body = parse_markdown(content)
        
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{file_path}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #121212; color: #e0e0e0; padding: 40px; line-height: 1.6; max-width: 800px; margin: 0 auto; }}
        h1 {{ color: #90caf9; border-bottom: 2px solid #333; padding-bottom: 10px; }}
        h2 {{ color: #ce93d8; margin-top: 30px; }}
        strong {{ color: #ffab40; }}
        ul {{ background: #1e1e1e; padding: 20px 40px; border-radius: 8px; border: 1px solid #333; }}
        li {{ margin-bottom: 8px; }}
        p {{ margin-bottom: 15px; }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""

        # Extract number
        match = re.search(r'script_for_diapositiva_(\d+)\.md', file_path)
        if match:
            num = match.group(1)
            out_name = f'diapositiva_{num}.html'
            with open(out_name, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"Generated {out_name}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
