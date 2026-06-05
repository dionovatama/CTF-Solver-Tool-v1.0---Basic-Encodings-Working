from typing import List, Tuple

class CryptoDecoder:
    """Decode berbagai cipher"""
    
    @staticmethod
    def xor_decrypt(data: bytes, key: bytes) -> bytes:
        """XOR decryption dengan single/multi-byte key"""
        result = bytearray()
        for i, byte in enumerate(data):
            result.append(byte ^ key[i % len(key)])
        return bytes(result)
    
    @staticmethod
    def xor_brute_force(data: bytes, max_key_size: int = 4) -> List[Tuple[bytes, bytes]]:
        """Brute force XOR dengan berbagai key size"""
        results = []
        
        for key_size in range(1, max_key_size + 1):
            if key_size == 1:
                for key_byte in range(256):
                    key = bytes([key_byte])
                    decrypted = CryptoDecoder.xor_decrypt(data, key)
                    try:
                        if decrypted.decode('utf-8'):
                            results.append((key, decrypted))
                    except:
                        pass
        
        return results
    
    @staticmethod
    def caesar_decrypt(text: str, shift: int) -> str:
        """Caesar cipher dengan shift tertentu"""
        result = []
        for char in text:
            if char.isupper():
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            elif char.islower():
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def caesar_brute_force(text: str) -> List[Tuple[int, str]]:
        """Brute force Caesar cipher (all 26 shifts)"""
        results = []
        for shift in range(26):
            decrypted = CryptoDecoder.caesar_decrypt(text, shift)
            results.append((shift, decrypted))
        return results
    
    @staticmethod
    def vigenere_decrypt(ciphertext: str, key: str) -> str:
        """Vigenère cipher decryption"""
        key = key.upper()
        plaintext = []
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                key_index += 1
            else:
                plaintext.append(char)
        
        return ''.join(plaintext)