Les échecs renferment de nombreux secrets

Cette image est tirée d'une partie de 2 grands maîtres internationaux et renferme un immense secret que vous devez retrouver !

![chall](https://user-images.githubusercontent.com/77735908/177059313-3935cccf-d5c9-4165-8e99-3bf8d627a57b.jpg)

En allant voir dans la description de l'image située dans le code source nous avons une message encodée en base 64 : MS4gaDMgZDYgMi4gTmMzIGc1IDMuIE5kNSBjNiA0LiBiNCBjeGQ1IDUuIFJoMiBmNiA2LiBlMyBCZjUgNy4gUWc0IEJkMyA4LiBOZjMgUWM4IDkuIGM0IFFjNSAxMC4gUWU0IHsgQmxhY2sgcmVzaWducy4gfSAxLTA=
Une décodé cela nous donne : 1. h3 d6 2. Nc3 g5 3. Nd5 c6 4. b4 cxd5 5. Rh2 f6 6. e3 Bf5 7. Qg4 Bd3 8. Nf3 Qc8 9. c4 Qc5 10. Qe4 { Black resigns. } 1-0

Cette combinaison de coup d'échec n'est en fait qu'un message encodé, car en faisant des recherches on tombe sur le github https://github.com/jes/chess-steg qui explique bien le principe. Une fois décodé nous obtenons ce message : NGxcj5Ft0GA

Ce drôle de message est assez court pour être le flag encodé. En faisant un tour sur https://www.dcode.fr/identification-chiffrement on trouve que c'est une vidéo youtube.

Dans la description de la vidéo on trouve le flag:

PWNME{1_L0v3_Ch3sSsss}
