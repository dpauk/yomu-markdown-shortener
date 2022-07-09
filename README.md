# yomu-markdown-shortener

Takes the output from a [Yomu](https://www.yomu-reader.com/) markdown-formatted set of annotations and removes the dates and links.

## Usage

1. Add the output from Yomu into `yomu_markdown_input.md`
2. Run `python yms.py`
3. The formatted output will appear in `output\output.md`

### Optional

To split the file into individual chapter in the output directory: `python yms.py -s` or `python yms.py --split`