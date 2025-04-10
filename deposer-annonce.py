# -*- coding: utf-8 -*-


import streamlit as st
from st_audiorec import st_audiorec
import tempfile
import os
import shutil
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Authentification Google Drive via secrets
SCOPES = ['https://www.googleapis.com/auth/drive.file']
service_account_info = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(
    dict(service_account_info), scopes=SCOPES
)
drive_service = build('drive', 'v3', credentials=credentials)

# Fonction pour créer un sous-dossier si nécessaire
def create_subfolder(folder_name, parent_folder_id):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and '{parent_folder_id}' in parents and trashed=false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])
    if items:
        return items[0]['id']
    else:
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_folder_id]
        }
        file = drive_service.files().create(body=file_metadata, fields='id').execute()
        return file.get('id')

# Fonction pour uploader un fichier sur Google Drive
def upload_to_drive(file_path, folder_id):
    try:
        file_metadata = {'name': os.path.basename(file_path), 'parents': [folder_id]}
        media = MediaFileUpload(file_path, mimetype='audio/wav')
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')
    except Exception as e:
        st.error(f"Erreur lors de l'upload sur Google Drive : {e}")
        return None

# ID du dossier Google Drive principal
FOLDER_ID = '1_2InKzKskt1q-0S9HFWXlap380QF4hi2'

# Titre et description
st.title("Une nouvelle annonce sonore pour la BU Droit !")
st.write("""> La bibliothèque ferme dans 30 minutes. A votre départ, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir demain matin à partir de 9h et jusqu'à 13h. Bonne soirée.

Si vous fréquentez la BU le soir vers 18h30, vous avez l'habitude d'entendre ce type de message. Et si vous faisiez entendre votre voix en renouvellement ces annonces sonores ?  
Enregistrez vos annonces, transmettez-nous les fichiers et vous aurez peut-être la chance d'entendre votre belle voix résonner le soir dans toute la BU !""")

# Fonction générique pour un formulaire d'enregistrement
def enregistrer_annonce(titre_formulaire, nom_fichier, texte_annonce):
    with st.form(key=f'form_{nom_fichier}'):
        st.subheader(titre_formulaire)
        st.write(texte_annonce)
        audio_data = st_audiorec()
        submit_button = st.form_submit_button(label='Valider et envoyer')

        if submit_button and audio_data is not None:
            st.audio(audio_data, format='audio/wav')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                temp_file.write(audio_data)
                temp_file_path = temp_file.name
            temp_file.close()

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = "annonces"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{nom_fichier}_{timestamp}.wav")
            shutil.move(temp_file_path, output_path)

            # Créer ou obtenir le sous-dossier
            subfolder_id = create_subfolder(nom_fichier, FOLDER_ID)

            # Upload Google Drive
            file_id = upload_to_drive(output_path, subfolder_id)
            if file_id:
                # Confirmation visuelle
                st.success(f"Merci pour votre participation ! Votre message '{titre_formulaire}' a bien été envoyé.")
                st.toast("Message envoyé ! ", icon="✅")
                st.balloons()
            else:
                st.error("L'upload du fichier a échoué. Veuillez réessayer.")

# Formulaires
annonces = [
    ("Message 30 minutes", "Message_30_minutes", "La bibliothèque ferme dans 30 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée."),
    ("Message 10 minutes", "Message_10_minutes", "La bibliothèque ferme dans 10 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir demain matin à partir de 8h30. Bonne soirée."),
    ("Message samedi 10 minutes et vendredi quand samedi fermé", "Message_samedi", "La bibliothèque ferme dans 10 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir lundi matin à partir de 8h30. Bonne soirée."),
    ("NoctamBU 18h30", "NoctamBU_18h30", "Le service NoctamBU débute dans 30 minutes. Si vous ne souhaitez pas rester et que vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée."),
    ("NoctamBU 19h05", "NoctamBU_19h05", "La bibliothèque fonctionne désormais en horaires NoctamBU. Les prêts et les retours restent possibles pendant la soirée."),
    ("NoctamBU 21h30", "NoctamBU_21h30", "La fermeture de la bibliothèque débutera dans 15 minutes. Merci de commencer à rassembler vos affaires afin de vous préparer à partir. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée."),
    ("NoctamBU 21h45", "NoctamBU_21h45", "La bibliothèque est en cours de fermeture. Merci de rassembler vos affaires et de vous diriger vers la sortie. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée."),
    ("Vendredi de NoctamBU", "Vendredi_NoctamBU", "La bibliothèque est en cours de fermeture. Merci de rassembler vos affaires et de vous diriger vers la sortie. Nous vous retrouverons demain, de 9h à 13h. Bonne fin de soirée.")
]

for titre, fichier, texte in annonces:
    enregistrer_annonce(titre, fichier, texte)
