cuts.pdf: cuts.tex cut1.png cut2.png
	pdflatex -interaction nonstopmode cuts.tex

.PHONY: clean
clean:
	-rm -rf cuts.aux cuts.log

.PHONY: superclean
superclean: clean
	-rm -rf cuts.pdf
