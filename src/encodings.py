import base64
import binascii
import codecs
from typing import Tuple, Optional

class EncodingDetector:
    """Detect dan decode berbagai encoding format"""
    
    @staticmethod
    def is_base64(data: str) -> bool:
        """Check if string is base64"""
        try:
            if isinstance(data, str):
                data_bytes = bytes(data, 'utf-8')
            elif isinstance(data, bytes):
                data_bytes = data
            else:
                return False
            
            # Base64 harus divisible by 4
            if len(data_bytes) % 4 != 0:
                return False
                
            return base64.b64encode(base64.b64decode(data_bytes)) == data_bytes
        except:
            return False
    
    @staticmethod
    def is_hex(data: str) -> bool:
        """Check if string is hex"""
        if len(data) % 2 != 0:
            return False
        try:
            bytes.fromhex(data)
            return True
        except:
            return False
    
    @staticmethod
    def decode_base64(data: str) -> str:
        """Decode base64 string"""
        try:
            return base64.b64decode(data).decode('utf-8')
        except:
            return None
    
    @staticmethod
    def decode_hex(data: str) -> str:
        """Decode hex string"""
        try:
            return bytes.fromhex(data).decode('utf-8')
        except:
            return None
    
    @staticmethod
    def decode_rot13(data: str) -> str:
        """Decode ROT13"""
        try:
            return codecs.decode(data, 'rot_13')
        except:
            return None
    
    @staticmethod
    def decode_atbash(data: str) -> str:
        """Decode Atbash cipher (mirror alphabet)"""
        result = []
        for char in data:
            if char.isupper():
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            elif char.islower():
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def decode_url(data: str) -> str:
        """Decode URL encoding"""
        try:
            return binascii.a2b_qp(data).decode('utf-8')
        except:
            try:
                import urllib.parse
                return urllib.parse.unquote(data)
            except:
                return None
    
    @staticmethod
    def auto_detect_and_decode(data: str) -> Tuple[str, str]:
        """Auto-detect encoding dan decode"""
        detectors = [
            ('Base64', EncodingDetector.is_base64, EncodingDetector.decode_base64),
            ('Hex', EncodingDetector.is_hex, EncodingDetector.decode_hex),
        ]
        
        for name, detector, decoder in detectors:
            if detector(data):
                decoded = decoder(data)
                if decoded:
                    return name, decoded
        
        # Try ROT13 dan Atbash (always try)
        rot13_result = EncodingDetector.decode_rot13(data)
        if rot13_result and rot13_result != data:
            return 'ROT13', rot13_result
        
        atbash_result = EncodingDetector.decode_atbash(data)
        if atbash_result and atbash_result != data:
            return 'Atbash', atbash_result
        
        return None, None