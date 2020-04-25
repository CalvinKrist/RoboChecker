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

:: Generate spiral path
python spiral_model_generator.py %1 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm -simpath %2 spiral/m%1paths/%3

:: Generate random path
python random_model_generator.py %1 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm -simpath %2 random/m%1paths/%3

:: Generate snake path
python snake_model_generator.py %1 > model.pm
java -Xmx4g -Xss8M -Djava.library.path="%PRISM_DIR%\lib" -classpath "%CP%" prism.PrismCL model.pm -simpath %2 snake/m%1paths/%3
