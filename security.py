from cryptography.fernet import Fernet

# --------------------
# 3. Güvenlik ve Gizlilik
# --------------------
class Security:
    @staticmethod
    def encrypt_data(data, key):
        """Veriyi şifreler."""
        cipher = Fernet(key)
        return cipher.encrypt(data.encode())

    @staticmethod
    def decrypt_data(data, key):
        """Veriyi çözer."""
        cipher = Fernet(key)
        return cipher.decrypt(data).decode()

    @staticmethod
    def generate_key():
        """Şifreleme anahtarını oluşturur."""
        return Fernet.generate_key()
