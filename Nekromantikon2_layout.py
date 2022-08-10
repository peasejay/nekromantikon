from jinja2 import Environment, FileSystemLoader
import json

# load serialized text blocks
text_block_path = "Nekromantikon2_textblocks.mbn.json"
with open(text_block_path) as f:
	text_blocks = json.load(f)

# initalize jinja
env = Environment(
    loader=FileSystemLoader('./templates'),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template("Nekromantikon2.html.jinja")


# export template to html
export_path = "Nekromantikon2.html"
with open(export_path, 'w') as f:
	print("Writing %s" % export_path)
	f.write(template.render(text_blocks=text_blocks))

