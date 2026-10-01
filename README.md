# Habit Pix

Appli perso pour créer des habitudes, style pixel / rétro. Tout est dans `index.html` (un seul fichier). Les données restent dans le navigateur.

## Onglets
- **Habitudes** : cartes avec grille sur 22 semaines, série 🔥, filtres par catégorie, filtre « Restant » (Matin / Midi / Soir), recherche, tri.
  - Bouton **+** : catalogue de 36 suivis prêts à ajouter (santé, sport, nutrition, esprit, productivité, maison, social, finances) ou suivi personnalisé.
  - 3 types de suivi : **oui / non**, **compteur** (ex. 8 verres d'eau, 50 pompes) et **auto** (protéines, calories, séance de sport, remplis depuis les autres onglets).
  - Touche l'icône d'une carte pour la modifier ou la supprimer.
- **Sport** :
  - séance du jour avec cases à cocher par exercice et charge (kg) notée ;
  - calendrier mensuel : séances prévues, faites, manquées ; touche un jour pour changer la séance ; « Planifier 4 semaines » ; export `.ics` vers ton agenda (dans Claude) ;
  - **Coach IA** : génère un programme selon objectif, niveau, jours, durée, matériel et tes infos (blessures…), et le modifie sur demande (« remplace le squat, j'ai mal au genou »). Bouton Annuler.
  - programme entièrement modifiable : jours d'entraînement, séances, exercices, séries, reps, kg.
- **Nutrition** : calories, protéines, glucides, lipides par rapport à tes objectifs ; ajout par aliment (base de 33 aliments, valeurs recalculées selon la quantité) ou à la main ; « Décris ton repas » estimé par l'IA ; calcul des objectifs (Mifflin-St Jeor) ; poids du matin et notes du jour.
- **Journal** : humeur, note du jour, revue de la semaine.
- **Analyses** : séances sur 30 jours, calories moyennes, poids, graphiques 7 jours (habitudes, calories, protéines), statistiques par suivi, remise à zéro.
- **Méthodes** (ampoule en haut) : les techniques utilisées par l'appli.

## IA
Ouverte dans Claude (lien d'artefact), l'appli utilise Claude pour écrire et modifier le programme et estimer les repas. Ouverte ailleurs, elle se rabat sur un générateur de programme intégré et sur la base d'aliments intégrée.

## Méthodes intégrées
Empilement d'habitudes, règle des 2 minutes, ne jamais rater deux fois, suivi automatique, identité d'abord, quand et où, surcharge progressive, récompense immédiate (Pixou), revue hebdomadaire, peu à la fois.

Les données de départ sont des exemples (bouton « Tout effacer » dans Analyses).
