import streamlit as st
from audiorecorder import audiorecorder
import os


# Titre de l'application
st.title("Une nouvelle annonce sonore pour la BU Droit !")

# Descriptif
st.write("""
"La bibliothèque ferme dans 30 minutes. A votre départ, merci de repousser votre chaise et de laisser votre place propre.
Nous serons heureux de vous accueillir demain matin à partir de 9h et jusqu'à 13h. Bonne soirée."
Si vous fréquentez la BU le soir avant la fermeture, vous avez l'habitude d'être interrompus dans votre travail par ce type de message.
Et si vous faisiez entendre votre voix en participant au renouvellement de ces annonces ?
Enregistrez ces annonces sonores sur votre téléphone, transmettez-nous les fichiers ici et vous aurez la chance d'entendre votre annonce résonner dans toute la BU !
""")

# Liste des messages avec leur contenu
messages = {
    "Message 30 minutes": "La bibliothèque ferme dans 30 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.",
    "Message 10 minutes": "La bibliothèque ferme dans 10 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir demain matin à partir de 8h30. Bonne soirée.",
    "Message samedi 10 minutes et vendredi quand samedi fermé": "La bibliothèque ferme dans 10 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir lundi matin à partir de 8h30. Bonne soirée.",
    "NoctamBU 18h30": "Le service NoctamBU débute dans 30 minutes. Si vous ne souhaitez pas rester et que vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.",
    "NoctamBU 19h05": "La bibliothèque fonctionne désormais en horaires NoctamBU. Les prêts et les retours restent possibles pendant la soirée.",
    "NoctamBU 21h30": "La fermeture de la bibliothèque débutera dans 15 minutes. Merci de commencer à rassembler vos affaires afin de vous préparer à partir. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.",
    "NoctamBU 21h45": "La bibliothèque est en cours de fermeture. Merci de rassembler vos affaires et de vous diriger vers la sortie. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.",
    "Vendredi de NoctamBU, à 21h45": "La bibliothèque est en cours de fermeture. Merci de rassembler vos affaires et de vous diriger vers la sortie. Nous vous retrouverons demain, de 9h à 13h. Bonne fin de soirée."
}

# Afficher chaque message avec un enregistreur
for title, content in messages.items():
    st.subheader(title)
    st.write(content)

    # Enregistreur audio
    audio = audiorecorder("Cliquez pour enregistrer", "Cliquez pour arrêter l'enregistrement", key=title)

    if audio.duration_seconds > 0:  # Vérifie si un enregistrement a été fait
        # Lire l'audio
        st.audio(audio.export().read())

        # Bouton de validation
        if st.button(f"Valider et envoyer - {title}"):
            # Chemin du dossier où les fichiers seront enregistrés
            output_dir = "annonces"
            os.makedirs(output_dir, exist_ok=True)

            # Enregistrer le fichier au format WAV
            output_path = os.path.join(output_dir, f"{title}.wav")
            audio.export(output_path, format="wav")

            st.success(f"Votre message '{title}' a été enregistré avec succès dans {output_path}")
