probs.pdf: probs.tex
	pdflatex probs.tex

.PHONY: live
live:
	while fswatch -1 probs.tex; do \
		$(MAKE) ; \
	done

# Alternatively, with inotify instead:
#
#.PHONY: live
#live:
#	while inotifywait -e close_write probs.tex; do \
#		$(MAKE) ; \
#	done

.PHONY: clean
clean:
	-rm -rf probs.aux probs.log

.PHONY: superclean
superclean: clean
	-rm -rf probs.pdf
