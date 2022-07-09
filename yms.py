output = open('output.md', 'w')

passed_intro = False

with open('input.md', 'r') as input:
    for line in input:
        if line == '## Annotations\n':
            passed_intro = True
            output.write(f'{line}\n')
            continue
        
        if not passed_intro:
            output.write(line)
            continue
        
        if line.startswith('###'):
            output.write(f'{line}\n')
            continue

        if line.startswith('>'):
            output.write(f'{line}\n')
        
output.close()