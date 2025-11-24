MAIN = Latex_2020-Template
Temp_Dir = Latex_2020-Template_MultiTex
RM = rm -f

FIGURES = Figures/
CUR_PWD = $(shell pwd)

find:
	@echo $(CUR_PWD)

# PATHFIG=`pwd`

evince:
	evince $(MAIN).pdf
main:
	xelatex -shell-escape $(MAIN)
	-@bibtex $(MAIN)
	xelatex -shell-escape $(MAIN)
	xelatex -shell-escape $(MAIN)

all: main evince # clean

clean:
	-@$(RM) *.tex~ *.aux *.bbl *.dvi *.blg *.bcf *.out *.log *.nav *.thm *.snm *.toc *.vrb *.*.xml *.*~ *~ .*.swp
	-cd ..
	-@$(RM) *.tex~ *.aux *.bbl *.dvi *.blg *.bcf *.out *.log *.nav *.thm *.snm *.toc *.vrb *.*.xml *.*~ *~ .*.swp

cleanall: clean
	-@$(RM) $(MAIN).pdf
