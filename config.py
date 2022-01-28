"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", None) or "7055975"
        self.API_HASH: str = os.environ.get("API_HASH", None) or "b5a46009c73889abf90fdcff928e4532"
        self.SESSION: str = os.environ.get("PYROGRAM_SESSION", None) or "BQB2Imr63SjPpo4o1B1DravxYUQk6bnLhu0aCfUmUwKfd-A5AfCZ4lBXcfPfo5PltmKp9JyiKjuhwhuuEKqdIcGGxtCcdk6wRChAD1PeSaCS8I6PPrFoZRmSqLS2sL6L_Lm6EXbyNLGdXbAYNiyUTPYijtLY6JsGFEXCgPLG4PbVI87whqg1W8KLHwvDl45W5qtBosfAzR4T5TKjUStFTUppL4Tg58L6j1G5bnmfxDSrwLdZXTxVWksZJySGSfubW0bo3eHzGMEMhRHlR4x5gIuurLzyZVxVx2fAIRmFI-Wc9qxZtQ_kFEFRbLUrzOHtLem4zCVSoBe4KfdPT0UtiM2jfCT8RgA"
        self.SUDO_USERS: list = [
            int(id) for id in os.environ.get("SUDO_USERS", "5122474448").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
