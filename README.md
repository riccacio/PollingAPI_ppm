# Polling APP 

Questo è progetto universitario per il corso di Progettazione e Produzione Multimediale. 
È una RESTful API per la creazione e la gestione di sondaggi.

## Funzionalità

- Registrazione di un utente
- Autenticazione dell'utente tramite token
- Creazione di sondaggi
- Votazione nei sondaggi
- Visualizzazione dei risultati dei sondaggi
- Eliminazione dei sondaggi

## Come si usa in Locale

1. Clona il repository sul tuo computer locale.
2. Naviga fino alla directory del progetto.
3. Installa le dipendenze con `pip install -r requirements.txt`.
4. Esegui le migrazioni con `python manage.py migrate`.
5. Avvia il server con `python manage.py runserver`.
6. Apri il tuo browser e vai all'indirizzo `http://127.0.0.1:8000`.

## Come si usa con httpie da terminale
1. Clona il repository sul tuo computer locale.
2. Naviga fino alla directory del progetto.
3. Installa le dipendenze con `pip install -r requirements.txt`.
4. Esegui le migrazioni con `python manage.py migrate`.
5. Avvia il server con `python manage.py runserver`.
6. Apri un altro terminale.
7. Ora puoi scrivere tutti i comandi per testare l'applicazione.

### Comandi
```
REGISTER user
http POST http://127.0.0.1:8000/api/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"

GET token
http http://127.0.0.1:8000/api/auth/token/ username="username" password="password"

GET all polls
http GET http://127.0.0.1:8000/api/polls/ "Authorization: Bearer {YOUR_TOKEN}"

GET a single poll
http GET http://127.0.0.1:8000/api/polls/{poll_id}/ "Authorization: Bearer {YOUR_TOKEN}"

CREATE a new poll
http POST http://127.0.0.1:8000/api/createPoll/ "Authorization: Bearer {YOUR_TOKEN}" question="What is your favorite color?"

DELETE poll
http DELETE http://127.0.0.1:8000/api/polls/{poll_id}/ "Authorization: Bearer {YOUR_TOKEN}"

CREATE new poll choice
http POST http://127.0.0.1:8000/api/polls/{poll_id}/createChoice/ "Authorization: Bearer {YOUR_TOKEN}" text="blue"

GET poll choices
http GET http://127.0.0.1:8000/api/polls/{poll_id}/choices "Authorization: Bearer {YOUR_TOKEN}"

VOTE in a poll
http POST http://127.0.0.1:8000/api/polls/{poll_id}/choices/{choice_id}/vote/ "Authorization: Bearer {YOUR_TOKEN}"
```

### Note su creazione utente e token

Se proviamo ad eseguire questo comando:
```
http GET http://127.0.0.1:8000/api/polls/ 
```
Ci mostrerà questo risulato, visto che per visualizzare, creare, cancellare e votare i sondaggi dobbiamo essere autenticati
```
{
    "detail": "Authentication credentials were not provided."
}
```
Invece, se proviamo ad accedere con le credenziali:
```
http http://127.0.0.1:8000/api/polls/ "Authorization: Bearer {YOUR_TOKEN}"
```
Otterremo la lista di tutti i sondaggi.

Quindi sarà necessario prima effettuare una registrazione e poi ottenere un token per poter fare le richieste, utilizzando i comandi sopra indicati.

Verranno restituiti due token:
```
{
    "access": "token1",
    "refresh": "token2"
}
```
L'access token verrà utilizzato per autenticare tutte le richieste che dobbiamo effettuare e scadrà dopo un po' di tempo. 

Possiamo utilizzare il refresh token per richiedere un nuovo token di accesso.
```
http http://127.0.0.1:8000/api/auth/token/refresh/ refresh="token1"
```
e otterremo un nuovo token di accesso
```
{
    "access": "token3"
}
```





## Online

Il progetto è stato deployato su Railway. Puoi accedere all'applicazione [qui](https://pollingapippm-production.up.railway.app/).
