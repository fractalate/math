csfpc.pdf: csfpc.tex
	pdflatex -interaction nonstopmode csfpc.tex

.PHONY: live
live:
	while inotifywait -e close_write csfpc.tex; do \
		$(MAKE) ; \
	done

.PHONY: clean
clean:
	-rm -rf csfpc.aux csfpc.log

.PHONY: superclean
superclean: clean
	-rm -rf csfpc.pdf
