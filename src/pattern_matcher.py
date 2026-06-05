import re

class PatternMatcher:
    """Extract patterns dari decoded text"""
    
    @staticmethod
    def extract_flags(text: str) -> list:
        """Extract flag{...} patterns"""
        pattern = r'flag\{[^}]*\}'
        matches = re.findall(pattern, text, re.IGNORECASE)
        return matches
    
    @staticmethod
    def extract_hex_strings(text: str, min_length: int = 4) -> list:
        """Extract hex strings"""
        pattern = r'[0-9a-fA-F]{' + str(min_length) + ',}'
        matches = re.findall(pattern, text)
        return matches
    
    @staticmethod
    def extract_base64(text: str) -> list:
        """Extract base64 patterns"""
        pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
        matches = re.findall(pattern, text)
        return matches
    
    @staticmethod
    def is_readable(text: str) -> bool:
        """Check if text is human-readable"""
        if not text:
            return False
        
        try:
            text.encode('utf-8')
        except:
            return False
        
        # Check if mostly printable characters
        printable_count = sum(1 for c in text if c.isprintable())
        return printable_count / len(text) > 0.8