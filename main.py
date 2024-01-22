import datetime
import pytz
import logging

logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)

logging.info(f"Lancement du traitement")

# Set the Réunion timezone
reunion_tz = pytz.timezone('Indian/Reunion')

timezone = reunion_tz
logging.debug(f"Demande d'heure sur le timezone : {timezone}")

if timezone is None:
    logging.error("aucune timezone n'a été renseignée")
    raise ValueError("aucune timezone n'a été renseignée")

# Get the current date and time in UTC
utc_now = datetime.datetime.utcnow()

# Convert the UTC datetime to the Réunion timezone
reunion_dt = utc_now.astimezone(reunion_tz)

# Print out the current date and time in the Réunion timezone
print("The current date and time in Réunion is:")
print(reunion_dt.strftime("%Y-%m-%d %H:%M:%S"))

