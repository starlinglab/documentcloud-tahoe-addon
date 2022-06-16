import os

import requests
from documentcloud.addon import AddOn

SERVER = "https://example.com"  # No ending slash
PASSWORD = os.environ["TAHOE_PASSWORD"]  # For server basicauth


class Tahoe(AddOn):
    def main(self):
        for doc_id in self.documents:
            pass


if __name__ == "__main__":
    Tahoe().main()
