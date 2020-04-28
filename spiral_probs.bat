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


python spiral_model_generator.py 2 > model_spiral.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 1 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 2 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 3 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 4 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 5 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 6 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 7 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 8 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 9 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 10 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 11 -sim -simmethod ci -simsamples 50
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model_spiral.pm properties.csl -prop 12 -sim -simmethod ci -simsamples 50