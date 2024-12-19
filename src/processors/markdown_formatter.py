import os
import re

class MarkdownFormatter:
    def convert_to_markdown(self, input_file, output_folder, custom_filename=None):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 決定輸出文件名
        if custom_filename:
            if not custom_filename.endswith('.md'):
                custom_filename += '.md'
            output_filename = custom_filename
        else:
            output_filename = os.path.basename(input_file).replace('.vtt', '.md')

        output_path = os.path.join(output_folder, output_filename)

        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        # 處理文本
        text_lines = self._process_lines(lines)
        
        # 寫入文件
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write("\n\n".join(text_lines))

    def _process_lines(self, lines):
        # 跳過 WEBVTT 行
        start_index = 0
        for i, line in enumerate(lines):
            if line.strip() == "WEBVTT":
                start_index = i + 1
                break

        text_lines = []
        current_sentence = ""
        
        for line in lines[start_index:]:
            if self._is_timestamp(line) or not line.strip():
                continue
                
            if self._is_sentence_end(line):
                current_sentence += " " + line.strip()
                if current_sentence.strip():
                    text_lines.append("### " + current_sentence.strip())
                current_sentence = ""
            else:
                current_sentence += " " + line.strip()

        if current_sentence:
            text_lines.append("### " + current_sentence.strip())

        return text_lines

    def _is_timestamp(self, line):
        return bool(re.match(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}", line))

    def _is_sentence_end(self, line):
        return line.strip().endswith(('.', '!', '?'))