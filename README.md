# API SMS Free Mobile

[![Build Status](https://travis-ci.org/ericgaspar/Free_SMS_Sender.svg?branch=master)](https://travis-ci.org/ericgaspar/Free_SMS_Sender)

Activer la Notification par SMS 
[mobile.free.fr](https://www.mobile.free.fr)

L'envoi du SMS se fait en appelant le lien suivant : `https://smsapi.free-mobile.fr/sendmsg`
avec les paramètres suivants :
* user :  votre login
* pass :  votre clé d'identification générée automatiquement par notre service
* msg :  le contenu du SMS encodé sous forme d'url (Percent-encoding)
* Exemple : Envoyer le message "Hello World !" sur votre mobile :
`https://smsapi.free-mobile.fr/sendmsg?user=USER&pass=PASS&msg=Hello%20World%20!`
Vous pouvez également, si vous le préférez, envoyer les paramètres en POST.
Dans ce cas, le contenu du message n'a pas besoin d'être encodé.

Le code de retour HTTP indique le succès ou non de l'opération :

* 200 : Le SMS a été envoyé sur votre mobile.
* 400 : Un des paramètres obligatoires est manquant.
* 402 : Trop de SMS ont été envoyés en trop peu de temps.
* 403 : Le service n'est pas activé sur l'espace abonné, ou login / clé incorrect.
* 500 : Erreur côté serveur. Veuillez réessayer ultérieurement.
