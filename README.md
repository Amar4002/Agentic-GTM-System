# Agentic GTM Automation (Gemini + Twilio)

This project is an end-to-end **Agentic GTM Automation System** that:
- Reads CRM data
- Decides who requires follow-up
- Generates personalized messages using **Gemini LLM**
- Sends real WhatsApp messages via **Twilio API**
- Logs provider responses (SID, status, timestamp)
- Saves voice call audio for alternate channel tests
- Supports inbound reply handling (webhook-ready)

---

## 🚀 Features

### 1. Automated Lead Follow-ups
Decides whether a lead needs follow-up based on:
- Last contact date
- Days since last interaction
- Lead context (last message)

### 2. AI-Powered Personalization (Gemini)
The message is generated dynamically using:
- Lead name
- Last message
- Days since last contact

### 3. Real WhatsApp Delivery via Twilio
Sends:
- WhatsApp messages
- Receives Twilio SID + Status
- Logs complete provider response

### 4. Logging System
Everything is stored in `output_log.csv`:
- Lead info
- Channel used
- LLM prompt
- LLM output
- Provider-side message SID
- Timestamp

### 5. Inbound Reply Demo
A mock webhook example is included to show how replies could be processed.

---

## 📁 Project Structure

