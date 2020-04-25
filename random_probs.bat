@echo off

:: Set prism directory (no quotes)
set PRISM_DIR=D:\Program Files\prism-4.5

:: Add PRISM to path
path=%PRISM_DIR%\lib;%path%

:: Set up CLASSPATH:
::  - PRISM jar file (for binary versions) (gets priority)
::  - classes directory (most PRISM classes)
::  - top-level directory (for images, dtds)
::  - lib/pepa.zip (PEPA stuff)
::  - lib/*.jar (all other jars)
set CP=%PRISM_DIR%\lib\prism.jar;%PRISM_DIR%\classes;%PRISM_DIR%;%PRISM_DIR%\lib\pepa.zip;%PRISM_DIR%\lib\*


python random_model_generator.py 1 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm calvin.csl -prop 19 -sim -simmethod ci -simsamples	100
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm calvin.csl -prop 20 -sim -simmethod ci -simsamples	100
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm calvin.csl -prop 21 -sim -simmethod ci -simsamples	100
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm calvin.csl -prop 22 -sim -simmethod ci -simsamples	100
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm calvin.csl -prop 23 -sim -simmethod ci -simsamples	100
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm calvin.csl -prop 24 -sim -simmethod ci -simsamples	100