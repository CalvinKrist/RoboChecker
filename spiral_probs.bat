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


python spiral_model_generator.py 1 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 1 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 2 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 3 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 4 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 5 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 6 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 7 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 8 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 9 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 10 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 11 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 12 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 13 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 14 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 15 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 16 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 17 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 18 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 19 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 20 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 21 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 22 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 23 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 24 -sim -simmethod ci -simsamples 300

python spiral_model_generator.py 2 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 25 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 26 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 27 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 28 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 29 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 30 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 31 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 32 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 33 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 34 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 35 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 36 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 37 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 38 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 39 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 40 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 41 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 42 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 43 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 44 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 45 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 46 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 47 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 48 -sim -simmethod ci -simsamples 300

python spiral_model_generator.py 3 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 49 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 50 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 51 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 52 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 53 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 54 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 55 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 56 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 57 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 58 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 59 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 60 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 61 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 62 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 63 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 64 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 65 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 66 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 67 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 68 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 69 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 70 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 71 -sim -simmethod ci -simsamples 300
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm properties.csl -prop 72 -sim -simmethod ci -simsamples 300