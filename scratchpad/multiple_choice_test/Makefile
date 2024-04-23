MAIN_NAME=mct

$(MAIN_NAME).pdf: $(MAIN_NAME).tex
	pdflatex -interaction nonstopmode $(MAIN_NAME).tex

.PHONY: live
live:
	while fswatch -1 $(MAIN_NAME).tex; do \
		$(MAKE) ; \
	done

.PHONY: clean
clean:
	-rm -rf $(MAIN_NAME).aux $(MAIN_NAME).log

.PHONY: superclean
superclean: clean
	-rm -rf $(MAIN_NAME).pdf
