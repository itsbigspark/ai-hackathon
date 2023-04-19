#! /bin/sh
#
# generate_pdf.sh
# Copyright (C) 2023 Konrad <konrad.zdeb@me.com>
#
# Trivial script automatically generating PDFs from the provided drawio file
# uses fswatch to monitor for local file change

# Change to replace drawio binary, on linux usually drawio 
drawio='/Applications/draw.io.app/Contents/MacOS/draw.io'

fswatch -0 ./*.drawio | xargs -t -0 -n1 -I {} $drawio \
	--export --format pdf "{}"

