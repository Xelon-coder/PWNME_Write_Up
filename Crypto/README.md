En séparant la chaine encrypté en 2 sous chaines : 219516015989366871732728605936755197601 et 2130689570892075754234400430874403925069147738764347075321
Nous avons les composante first et second

Pour reverse l'algo il faut commencer par inverser les chaines puis d'appliquer un xor avec 13 pour la first et 37 pour la seconde
On convertit le long en bytes et voilà le flag:

PWNME{84ec5fec3e2ec91291bb74648d35dcbc4}
