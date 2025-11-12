
import pandas as pd
from datetime import datetime
import pyttsx3
import os
import random


CRM_PATH = r"C:\Users\Desktop\sample_30_leads.csv" # csv file path
OUTPUT_LOG = "output_log.csv"
AUDIO_DIR = "voice_calls"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Reading the data
try:
    df = pd.read_csv(CRM_PATH)

    #  matching the data with csv file 
    df.rename(columns={
        "Lead name": "Name",
        "Phone number / WhatsApp": "Phone",
        "Last contact date": "LastContactDate",
        "Last message or call summary": "LastMessage"
    }, inplace=True)

    #  Convert date column
    df["LastContactDate"] = pd.to_datetime(df["LastContactDate"], errors="coerce")

    print(f"\n Successfully loaded and formatted data from: {CRM_PATH}")

except Exception as e:
    print(f" Error loading CRM file: {e}")
    exit()

today = datetime.now().date()
log_data = []

# required functions
def choose_channel(phone):
    # Choose WhatsApp for even last digit, Voice for odd.
    last_digit = int(phone[-1]) if phone[-1].isdigit() else 0
    return "WhatsApp" if last_digit % 2 == 0 else "Voice"

def simulate_whatsapp(name, phone):
    #  Simulate sending a WhatsApp message.
    message = f"Hi {name}, just checking in to see if you'd like to continue our discussion this week."
    print(f"📱 Sending WhatsApp to {name}: {message}")
    success = random.random() > 0.1
    return ("Success", message) if success else ("Failed", "Simulated API error")

def simulate_voice_call(name, text):
    #  Generating audio using pyttsx3.
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    
    filename = os.path.join(AUDIO_DIR, f"{name.replace(' ', '_')}.mp3")
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f" Voice call simulated for {name} → saved to {filename}")
    return "Success", f"Audio saved to {filename}"

# Processing
for _, lead in df.iterrows():
    try:
        name = lead["Name"]
        phone = str(lead["Phone"])
        last_contact = pd.to_datetime(lead["LastContactDate"]).date()
        days_since = (today - last_contact).days

        if days_since > 3:
            decision = "Follow-up"
            channel = choose_channel(phone)

            if channel == "WhatsApp":
                status, details = simulate_whatsapp(name, phone)
            else:
                tts_text = f"Hi {name}, calling from GTM Assist. Following up on our last chat. Can I share a short update?"
                status, details = simulate_voice_call(name, tts_text)
        else:
            decision = "Skip"
            channel = "N/A"
            status = "Skipped"
            details = f"Last contacted {days_since} day(s) ago."

        log_data.append({
            "Name": name,
            "Company": lead["Company"],
            "Phone": phone,
            "DaysSince": days_since,
            "Decision": decision,
            "Channel": channel,
            "Status": status,
            "Details": details,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    except Exception as e:
        print(f" Error processing lead: {e}")
        continue

# Saving Logs
log_df = pd.DataFrame(log_data)
log_df.to_csv(OUTPUT_LOG, index=False)


