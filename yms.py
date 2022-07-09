import argparse
import os

INPUT_FILE = 'yomu_markdown_input.md'
OUTPUT_DIR = os.path.join(os.getcwd(), 'output')

def split():
    passed_intro = False
    output = open(os.path.join(OUTPUT_DIR, 'title.md'), 'w')
    chapter_counter = 0

    with open(INPUT_FILE, 'r') as input:
        for line in input:

            ## Find the end of the intros
            if line == '## Annotations\n':
                passed_intro = True
                chapter_counter += 1
                continue
            
            # Output into title
            if not passed_intro:
                output.write(line)
                continue
            
            # New chapter
            if line.startswith('###'):
                output.close()
                output = open(os.path.join(OUTPUT_DIR, f'{chapter_counter} - {line[3:]}.md'), 'w')
                output.write(f'{line}\n')
                continue

            # A quote line to output
            if line.startswith('>'):
                output.write(f'{line}\n')
    
    output.close()

def parse():
    output = open(os.path.join(OUTPUT_DIR, 'output.md'), 'w')

    passed_intro = False

    with open(INPUT_FILE, 'r') as input:
        for line in input:
            ## Find the end of the intros
            if line == '## Annotations\n':
                passed_intro = True
                output.write(f'{line}\n')
                continue
            
            # Output into title
            if not passed_intro:
                output.write(line)
                continue
            
            # New chapter
            if line.startswith('###'):
                output.write(f'{line}\n')
                continue

            # A quote line to output
            if line.startswith('>'):
                output.write(f'{line}\n')
    
    output.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Yomu reader markdown files')
    parser.add_argument('-s', '--split', help='Split file based on chapter titles', action='store_true')
    args = parser.parse_args()

    if args.split:
        split()
    else:
        parse()
