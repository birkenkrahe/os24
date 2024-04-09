#!/usr/bin/bash
for file in *.xlsx; do
  libreoffice --headless --convert-to pdf "$file"
done

for file in *.docx; do
  pandoc "$file" -o "${file%.docx}.pdf"
done
