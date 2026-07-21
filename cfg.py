c = get_config()
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
c.TemplateExporter.extra_template_paths = [current_dir]
c.TemplateExporter.template_file = 'article.tplx'
c.PDFExporter.latex_command = ['xelatex', '{filename}']