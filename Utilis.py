
from pathlib import Path
import csv
from datetime import datetime

class CSVLogger:
    def __init__(self, path: Path):
        self.path = Path(path)
        header = ["Name","Phone","Channel","Decision","ProviderMessageSid","ProviderStatus","LLMPrompt","LLMOutput","Timestamp"]
        if not self.path.exists():
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(header)

    def log(self, record: dict):
        with open(self.path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                record.get("Name",""),
                record.get("Phone",""),
                record.get("Channel",""),
                record.get("Decision",""),
                record.get("ProviderMessageSid",""),
                record.get("ProviderStatus",""),
                record.get("LLMPrompt",""),
                record.get("LLMOutput",""),
                record.get("Timestamp", datetime.utcnow().isoformat())
            ])
