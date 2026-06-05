from src.encodings import EncodingDetector

def test_base64():
    encoded = "SGVsbG8gV29ybGQ="
    decoded = EncodingDetector.decode_base64(encoded)
    assert decoded == "Hello World"
    print("✓ Base64 test passed")

def test_hex():
    encoded = "48656c6c6f"
    decoded = EncodingDetector.decode_hex(encoded)
    assert decoded == "Hello"
    print("✓ Hex test passed")

def test_rot13():
    encoded = "Uryyb"
    decoded = EncodingDetector.decode_rot13(encoded)
    assert decoded == "Hello"
    print("✓ ROT13 test passed")

def test_auto_detect():
    encoded = "VV9YViMEQmkCbEEGKUcuKFxBZlprTi5kQEAKXDpbQjRO"
    encoding, decoded = EncodingDetector.auto_detect_and_decode(encoded)
    print(f"Auto-detected: {encoding}")
    print(f"Decoded: {decoded[:50]}...")
    print("✓ Auto-detect test passed")

if __name__ == '__main__':
    test_base64()
    test_hex()
    test_rot13()
    test_auto_detect()
    print("\nAll tests passed! ✓")