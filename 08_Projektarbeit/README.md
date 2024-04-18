# M323
## 1

PROJEKT REPO HIER: https://github.com/KevinZingg/todo_m323

Bei der Funktion getFirstCharacter(String s) haben wir keine Garantie, dass wir immer einen Wert zurückerhalten. Der Grund dafür ist, dass die Methode charAt(0) eine StringIndexOutOfBoundsException auslösen kann, wenn der übergebene String s leer ist (""). Bei einem leeren String hat s keine Zeichen, auf die zugegriffen werden kann, und somit kann kein Zeichen zurückgegeben werden.

Im Gegensatz dazu wird die Funktion add(int a, int b) immer einen Wert zurückgeben, da die Addition zweier Ganzzahlen in Java immer ein wohldefiniertes Ergebnis hat und keine Ausnahmesituationen wie bei der charAt-Methode auftreten.
