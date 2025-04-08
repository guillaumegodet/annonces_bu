import streamlit as st
from st_audiorec import st_audiorec
import tempfile
import os
import shutil

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

# Message 30 minutes
with st.form(key='form_30'):
    st.subheader("Message 30 minutes")
    st.write("La bibliothèque ferme dans 30 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.")
    wav_audio_data_30 = st_audiorec()
    submit_button_30 = st.form_submit_button(label='Valider et envoyer')

    if submit_button_30 and wav_audio_data_30 is not None:
        st.audio(wav_audio_data_30, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_30)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "Message 30 minutes.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'Message 30 minutes' a été enregistré avec succès dans {output_path}")

# Message 10 minutes
with st.form(key='form_10'):
    st.subheader("Message 10 minutes")
    st.write("La bibliothèque ferme dans 10 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir demain matin à partir de 8h30. Bonne soirée.")
    wav_audio_data_10 = st_audiorec()
    submit_button_10 = st.form_submit_button(label='Valider et envoyer')

    if submit_button_10 and wav_audio_data_10 is not None:
        st.audio(wav_audio_data_10, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_10)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "Message 10 minutes.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'Message 10 minutes' a été enregistré avec succès dans {output_path}")

# Message samedi 10 minutes et vendredi quand samedi fermé
with st.form(key='form_samedi'):
    st.subheader("Message samedi 10 minutes et vendredi quand samedi fermé")
    st.write("La bibliothèque ferme dans 10 minutes. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Nous serons heureux de vous accueillir lundi matin à partir de 8h30. Bonne soirée.")
    wav_audio_data_samedi = st_audiorec()
    submit_button_samedi = st.form_submit_button(label='Valider et envoyer')

    if submit_button_samedi and wav_audio_data_samedi is not None:
        st.audio(wav_audio_data_samedi, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_samedi)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "Message samedi 10 minutes et vendredi quand samedi fermé.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'Message samedi 10 minutes et vendredi quand samedi fermé' a été enregistré avec succès dans {output_path}")

# NoctamBU 18h30
with st.form(key='form_noctambu_18h30'):
    st.subheader("NoctamBU 18h30")
    st.write("Le service NoctamBU débute dans 30 minutes. Si vous ne souhaitez pas rester et que vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.")
    wav_audio_data_noctambu_18h30 = st_audiorec()
    submit_button_noctambu_18h30 = st.form_submit_button(label='Valider et envoyer')

    if submit_button_noctambu_18h30 and wav_audio_data_noctambu_18h30 is not None:
        st.audio(wav_audio_data_noctambu_18h30, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_noctambu_18h30)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "NoctamBU 18h30.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'NoctamBU 18h30' a été enregistré avec succès dans {output_path}")

# NoctamBU 19h05
with st.form(key='form_noctambu_19h05'):
    st.subheader("NoctamBU 19h05")
    st.write("La bibliothèque fonctionne désormais en horaires NoctamBU. Les prêts et les retours restent possibles pendant la soirée.")
    wav_audio_data_noctambu_19h05 = st_audiorec()
    submit_button_noctambu_19h05 = st.form_submit_button(label='Valider et envoyer')

    if submit_button_noctambu_19h05 and wav_audio_data_noctambu_19h05 is not None:
        st.audio(wav_audio_data_noctambu_19h05, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_noctambu_19h05)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "NoctamBU 19h05.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'NoctamBU 19h05' a été enregistré avec succès dans {output_path}")

# NoctamBU 21h30
with st.form(key='form_noctambu_21h30'):
    st.subheader("NoctamBU 21h30")
    st.write("La fermeture de la bibliothèque débutera dans 15 minutes. Merci de commencer à rassembler vos affaires afin de vous préparer à partir. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.")
    wav_audio_data_noctambu_21h30 = st_audiorec()
    submit_button_noctambu_21h30 = st.form_submit_button(label='Valider et envoyer')

    if submit_button_noctambu_21h30 and wav_audio_data_noctambu_21h30 is not None:
        st.audio(wav_audio_data_noctambu_21h30, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_noctambu_21h30)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "NoctamBU 21h30.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'NoctamBU 21h30' a été enregistré avec succès dans {output_path}")

# NoctamBU 21h45
with st.form(key='form_noctambu_21h45'):
    st.subheader("NoctamBU 21h45")
    st.write("La bibliothèque est en cours de fermeture. Merci de rassembler vos affaires et de vous diriger vers la sortie. Quand vous quittez la BU, merci de repousser votre chaise et de laisser votre place propre. Bonne soirée.")
    wav_audio_data_noctambu_21h45 = st_audiorec()
    submit_button_noctambu_21h45 = st.form_submit_button(label='Valider et envoyer')

    if submit_button_noctambu_21h45 and wav_audio_data_noctambu_21h45 is not None:
        st.audio(wav_audio_data_noctambu_21h45, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_noctambu_21h45)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "NoctamBU 21h45.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'NoctamBU 21h45' a été enregistré avec succès dans {output_path}")

# Vendredi de NoctamBU, à 21h45
with st.form(key='form_vendredi'):
    st.subheader("Vendredi de NoctamBU, à 21h45")
    st.write("La bibliothèque est en cours de fermeture. Merci de rassembler vos affaires et de vous diriger vers la sortie. Nous vous retrouverons demain, de 9h à 13h. Bonne fin de soirée.")
    wav_audio_data_vendredi = st_audiorec()
    submit_button_vendredi = st.form_submit_button(label='Valider et envoyer')

    if submit_button_vendredi and wav_audio_data_vendredi is not None:
        st.audio(wav_audio_data_vendredi, format='audio/wav')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(wav_audio_data_vendredi)
            temp_file_path = temp_file.name

        # Fermer le fichier avant de le déplacer
        temp_file.close()

        output_dir = "annonces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "Vendredi de NoctamBU, à 21h45.wav")
        shutil.move(temp_file_path, output_path)
        st.success(f"Votre message 'Vendredi de NoctamBU, à 21h45' a été enregistré avec succès dans {output_path}")
