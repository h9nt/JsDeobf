import requests

# Api wrapper for https://jsdeobfuscator.com/api/deobfuscate

# Modes:
# - "auto": Automatically detect the obfuscation method.
# - "deobfuscate": Deobfuscate standard obfuscated code.
# - "beautify": Deobfuscate code that uses beautify-based obfuscation.
# - "unminify": Deobfuscate code that uses unminify-based obfuscation.

# Note: The API is not officially documented, so the implementation may change in the future.


class JsDeobf:
    def __init__(self, code: str | None = None, mode: str | None = None):
        """Initialize the JsDeobf class with optional code and mode parameters.

        Args:
            code (str, optional): The code to deobfuscate. Defaults to None.
            mode (str, optional): The deobfuscation mode. Defaults to None.

        Modes:
            - "auto": Automatically detect the obfuscation method.
            - "deobfuscate": Deobfuscate standard obfuscated code.
            - "beautify": Deobfuscate code that uses beautify-based obfuscation.
            - "unminify": Deobfuscate code that uses unminify-based obfuscation.
        """

        self.code: str | None = code
        self.mode: str | None = mode
        self.request = requests.Session()
        self.api_url = "https://jsdeobfuscator.com/api/deobfuscate"
        self.headers: dict[str, str] = {
            "Host": "jsdeobfuscator.com",
            "Connection": "keep-alive",
            "sec-ch-ua-platform": '"Windows"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
            "Content-Type": "application/json",
            "sec-ch-ua-mobile": "?0",
            "Accept": "*/*",
            "Origin": "https://jsdeobfuscator.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://jsdeobfuscator.com/",
            "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "_ga=GA1.1.2066508683.1789961914; _ga_ZRDYQJ09X7=GS2.1.s1789961913$o1$g1$t1789962303$j60$l0$h0",
        }

        if self.code is None:
            raise ValueError("Code is required")

        if self.mode is None:
            raise ValueError("Mode is required")

        if self.mode not in ["auto", "deobfuscate", "beautify", "unminify"]:
            raise ValueError("Invalid mode")

    def read_code_from_file(self, file_path: str):
        """Read code from a file and set it as the code to deobfuscate.

        Args:
            file_path (str): The path to the file containing the code.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            self.code = file.read()

    def deobfuscate(self):
        return self.request.post(
            self.api_url,
            headers=self.headers,
            json={"code": self.code, "mode": self.mode},
        ).json()["code"]

    def write_code_to_file(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.code)


if __name__ == "__main__":
    js_code = input("Enter the JavaScript file to deobfuscate: ")
    with open("./" + js_code, "r", encoding="utf-8") as file:
        code = file.read()
        try:
            deobf = JsDeobf(code=code, mode="auto").deobfuscate()
            print(deobf)
        except ValueError as e:
            print(f"Error: {e}")
