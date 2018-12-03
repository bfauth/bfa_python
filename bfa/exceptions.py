class JavaScriptError(Exception):
    def __str__(self):
        return "Failed to load JS"


class FingerprintError(Exception):
    def __str__(self):
        return "SHA256 fingerprint must be 64 symbols"
