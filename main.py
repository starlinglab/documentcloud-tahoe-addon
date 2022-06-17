import os

import requests
from documentcloud.addon import AddOn

SERVER = "https://tahoe.starlinglab.org"  # No ending slash
PASSWORD = os.environ["TAHOE_PASSWORD"]  # For server basicauth
TAHOE_DIR = os.environ["TAHOE_DIR"].replace(":", "%3A")  # Root dircap, URL encoded


class Tahoe(AddOn):
    def main(self):
        for doc_id in self.documents:
            document = self.client.documents.get(doc_id)
            r = requests.put(
                f"{SERVER}/uri/{TAHOE_DIR}/{str(document.id)}-{document.slug}.pdf",
                auth=("user", PASSWORD),
                timeout=10,
                data=document.pdf,
            )
            if r.status_code not in [200, 201]:
                self.set_message(f"Uploading failed with status code {r.status_code}")
                return
            filecap = r.text.strip()
            document.data["tahoe-filecap"] = filecap
            document.save()
            self.set_message(f"Upload complete: {filecap}")


if __name__ == "__main__":
    Tahoe().main()
