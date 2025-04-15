# Tutorial de EvoSuite con Maven

## Configuración inicial

### Descargar EvoSuite

```bash
wget https://github.com/EvoSuite/evosuite/releases/download/v1.0.6/evosuite-1.0.6.jar
wget https://github.com/EvoSuite/evosuite/releases/download/v1.0.6/evosuite-standalone-runtime-1.0.6.jar
```

### Descargar dependencias del proyecto

```bash
mvn dependency:copy-dependencies
```

## Compilar y ejecutar tests manuales

```bash
mvn clean compile
mvn test
```

## Generar y ejecutar tests con EvoSuite

### Compilar el proyecto con Maven

```bash
mvn clean compile
```

### Generar tests automáticos con EvoSuite

```bash
java -jar evosuite-1.0.6.jar -class genetics.Calculadora -projectCP target/classes
```

### Descargar dependencias (JUnit y Hamcrest)

```bash
mvn dependency:copy-dependencies
```

### Setear CLASSPATH

```bash
export CLASSPATH=target/classes:evosuite-standalone-runtime-1.0.6.jar:evosuite-tests:target/dependency/junit-4.12.jar:target/dependency/hamcrest-core-1.3.jar
```

### Compilar los tests generados por EvoSuite

```bash
javac evosuite-tests/genetics/*.java
```

### Ejecutar los tests generados

```bash
java org.junit.runner.JUnitCore genetics.Calculadora_ESTest
```