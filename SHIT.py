import sys

output_file = sys.argv[1]

with open("output_template", "r", encoding="utf-8") as f:
    output_template = f.read()

with open("build_number", "r+", encoding="utf-8") as f:
    build_number = int(f.read()) + 1
    
    f.seek(0)
    f.write(str(build_number))
    f.truncate()

with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write(output_template.format(build_number))