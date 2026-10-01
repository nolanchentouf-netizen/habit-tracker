# Habit Pix

Appli perso pour créer des habitudes, style pixel / rétro. Tout est dans `index.html` (un seul fichier). Les données restent dans le navigateur.

## Navigation (pensée pour le téléphone)
- En bas : **Suivis · Agenda · Sport · Repas · Études · Plus** (Journal, Temps restant, Analyses, Méthodes, Aide, Réglages sont dans Plus).
- En haut : **sablier** = temps restant, **+** = ajouter un suivi.
- Chaque page a un titre, une phrase qui explique quoi faire et des flèches pour changer de jour.
- **Plus** : Temps restant, Analyses, Méthodes, Aide (à quoi sert chaque bouton), Réglages.

## Installer sur le téléphone
L'appli installable est dans `app/` (générée par `python3 tools/build.py` à partir de `index.html`) :
icône sur l'écran d'accueil, plein écran, fonctionne hors ligne, raccourcis par appui long sur l'icône
(Temps restant, Repas, Sport, Journal).

1. **La mettre en ligne** (une seule fois), au choix :
   - **GitHub Pages** : le dépôt doit être public (ou compte GitHub Pro). Settings → Pages → Source : « GitHub Actions ».
     Le workflow `.github/workflows/pages.yml` publie `app/` à chaque push sur `main`.
   - **Netlify Drop** : sur https://app.netlify.com/drop, glisser le dossier `app/` (compte gratuit pour garder le site).
2. **L'installer** : ouvrir l'adresse sur le téléphone.
   - Android (Chrome) : menu ⋮ → « Installer l'application ».
   - iPhone (Safari) : Partager → « Sur l'écran d'accueil ».
3. **Récupérer ses données** : Plus → Réglages → « Sauvegarder mes données » dans l'ancienne version, puis « Restaurer une sauvegarde » dans l'appli installée.

Hors de Claude, l'IA n'est pas disponible : le coach et l'estimation des repas utilisent le modèle et la base intégrés.

## Onglets
- **Habitudes** : cartes avec grille sur 22 semaines, série 🔥, filtres par catégorie, filtre « Restant » (Matin / Midi / Soir), recherche, tri.
  - Bouton **+** : catalogue de 47 suivis prêts à ajouter (santé, sport, nutrition, esprit, productivité, maison, social, finances) ou suivi personnalisé.
  - 3 types de suivi : **oui / non**, **compteur** (ex. 8 verres d'eau, 50 pompes) et **auto** (protéines, calories, séance de sport, remplis depuis les autres onglets).
  - Touche l'icône d'une carte pour la modifier ou la supprimer.
- **Sport** :
  - séance du jour avec cases à cocher par exercice et charge (kg) notée ;
  - calendrier mensuel : séances prévues, faites, manquées ; touche un jour pour changer la séance ; « Planifier 4 semaines » ; export `.ics` vers ton agenda (dans Claude) ;
  - **Coach IA** : génère un programme selon objectif, niveau, jours, durée, matériel et tes infos (blessures…), et le modifie sur demande (« remplace le squat, j'ai mal au genou »). Bouton Annuler.
  - programme entièrement modifiable : jours d'entraînement, séances, exercices, séries, reps, kg.
- **Agenda** : emploi du temps centralisé, vue jour et semaine. Cours, travail, rendez-vous (une fois ou chaque semaine), séances de sport, séances de révision, examens et habitudes du jour.
- **Études** : fiches de révision avec répétition espacée (boîtes de Leitner : 1, 2, 4, 8, 16 jours), minuteur Pomodoro, fiches créées par l'IA depuis un cours (ou une par ligne « question : réponse »), planning de révision jusqu'à l'examen (apprendre puis revoir à J+1, J+3, J+7, test blanc la veille) ajouté à l'Agenda, technique de Feynman vérifiée par l'IA, matières et dates d'examen, conseils de révision.
- **Matériel** (Sport → Coach) : haltères, chaise romaine, poutre d'escalade, rétracteur et extenseur pour doigts cochés par défaut. Le programme les utilise toujours, avec un bloc doigts / avant-bras en fin de séance.
- **Nutrition** : calories, protéines, glucides, lipides par rapport à tes objectifs ; ajout par aliment (base de 33 aliments, valeurs recalculées selon la quantité) ou à la main ; « Décris ton repas » estimé par l'IA ; calcul des objectifs (Mifflin-St Jeor) ; poids du matin et notes du jour.
- **Journal** : humeur et note du jour, **une note + un ressenti par activité** (habitudes, séance, nutrition), historique des notes par activité, revue de la semaine. Le crayon sur chaque carte écrit directement la note.
- **Temps restant** : heures avant minuit, jours avant la fin de la semaine / du mois / de l'année, années, semaines et jours de vie estimés (date de naissance + espérance de vie), grille de ta vie en semaines.
- **Phrase de motivation** du jour sur l'écran Habitudes, et un encouragement à chaque case cochée.
- **Analyses** : séances sur 30 jours, calories moyennes, poids, graphiques 7 jours (habitudes, calories, protéines), statistiques par suivi, remise à zéro.
- **Méthodes** (ampoule en haut) : les techniques utilisées par l'appli.

## IA
Ouverte dans Claude (lien d'artefact), l'appli utilise Claude pour écrire et modifier le programme et estimer les repas. Ouverte ailleurs, elle se rabat sur un générateur de programme intégré et sur la base d'aliments intégrée.

## Méthodes intégrées
Empilement d'habitudes, règle des 2 minutes, ne jamais rater deux fois, suivi automatique, identité d'abord, quand et où, surcharge progressive, récompense immédiate (Pixou), revue hebdomadaire, peu à la fois.

Les données de départ sont des exemples (bouton « Tout effacer » dans Analyses).
