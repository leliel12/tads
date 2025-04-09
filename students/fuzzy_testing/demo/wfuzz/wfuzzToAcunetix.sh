# Descubrimiento de Rutas
wfuzz -c -w SecLists/Discovery/Web-Content/common.txt -u http://testphp.vulnweb.com/FUZZ --sc 200,403

# Fuzzing de Archivos Comunes
wfuzz -c -w SecLists/Discovery/Web-Content/raft-large-files.txt -u http://testphp.vulnweb.com/FUZZ --sc 200

# Fuzzing de Parámetros GET ocultos
wfuzz -c -z file,SecLists/Discovery/Web-Content/burp-parameter-names.txt -u "http://testphp.vulnweb.com/search.php?FUZZ=test" --sc 200

# Fuzzing de Cookies
wfuzz -c -w SecLists/Discovery/Web-Content/common.txt -H "Cookie: session=FUZZ" -u http://testphp.vulnweb.com/cart.php --sc 200

# Login Brute Force (simulado)
wfuzz -c -z file,SecLists/Usernames/top-usernames-shortlist.txt -z file,SecLists/Passwords/Common-Credentials/10k-most-common.txt -d "username=FUZZ&password=FUZ2Z" -u http://testphp.vulnweb.com/login.php --hh 1046

# --filter 'response.text.find("Welcome") != -1'
# --hh oculta palabras de longitud x
# -d simula un envio post
# -u url objetivo
