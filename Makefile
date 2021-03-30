# Makefile for Test_Fortran

MAKE = make
AR = ar

#CPP_OPTIONS= -DMPI -DHOST=\"IFC91_ompi\" -DIFC \
             -DCACHE_SIZE=4000 -DPGF90 -Davoidalloc \
             -DMPI_BLOCK=8000 -DscaLAPACK -Duse_collective \
             -DnoAugXCmeta -Duse_bse_te \
             -Duse_shmem -Dtbdyn

#CPP        = fpp -f_com=no -free -w0  $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

FC         = ifort

MKL_PATH   = $(MKLROOT)/lib/intel64
BLAS       = -lmkl_intel_lp64 -lmkl_core -lmkl_sequential
LAPACK     =
LLIBS      = $(MKL_PATH) $(LAPACK) $(BLAS)
FFLAGS     = -L$(LLIBS)
# include ../make.inc

#-------------------------------------------------------------------------------------------------
# Src and Libs
#-------------------------------------------------------------------------------------------------
SRC = Matrix_deal.f90 # Matrix_check.f90

OBJ = $(SRC:.f90=.o)
EXE = Generate_Matrix

#-------------------------------------------------------------------------------------------------
# Suffix rules
#-------------------------------------------------------------------------------------------------
.SUFFIXES: .o .f90
.f90.o:
	$(FC) $(FFLAGS) -c $<

#-------------------------------------------------------------------------------------------------
# Targets
#-------------------------------------------------------------------------------------------------
Generate_Matrix: $(OBJ)
	$(FC) $(FFLAGS) -o $(EXE) $(OBJ)
	rm *.o

clean:
	rm -f *.mod *.a
	rm -f $(OBJ) $(EXE)
