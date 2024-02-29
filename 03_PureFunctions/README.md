# M323
TBZ M323


## Aufgabe 1.1 Bewertung: Pure vs. Impure Funktionen

| Aufgabe | Nur ein Rückgabewert | Resultat nur abhängig von übergebenen Parametern | Verändert keine existierenden Werte | Pure oder Impure |
|---------|:--------------------:|:------------------------------------------------:|:-----------------------------------:|:----------------:|
| 1.1     | Ja                   | Nein                                             | Nein                                | Impure           |

### Erklärung:
- **Nur ein Rückgabewert:** Die Funktion `addToCart` gibt tatsächlich nur einen Wert zurück, den aktualisierten Warenkorb, daher ist dieses Kriterium erfüllt.
- **Resultat nur abhängig von übergebenen Parametern:** Die Funktion `addToCart` hängt von einem externen Zustand (`cartItems`) ab und verletzt damit das Prinzip, dass das Ergebnis nur von den übergebenen Parametern abhängen soll.
- **Verändert keine existierenden Werte:** Die Funktion verändert einen externen Zustand (`cartItems`), indem sie ein neues Element hinzufügt, was das Prinzip verletzt, keine existierenden Werte zu verändern.
