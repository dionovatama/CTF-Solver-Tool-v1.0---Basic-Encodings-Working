import click
from colorama import Fore, Style
from src.encodings import EncodingDetector
from src.cryptography import CryptoDecoder
from src.pattern_matcher import PatternMatcher

@click.group()
def cli():
    """CTF Solver Tool - Encoding & Cryptography"""
    pass

@cli.command()
@click.argument('data')
def auto(data):
    """Auto-detect dan decode encoding"""
    click.echo(f"{Fore.CYAN}[*] Auto-detecting encoding...{Style.RESET_ALL}")
    
    encoding, decoded = EncodingDetector.auto_detect_and_decode(data)
    
    if encoding:
        click.echo(f"{Fore.GREEN}[+] Detected: {encoding}{Style.RESET_ALL}")
        click.echo(f"{Fore.YELLOW}Decoded:{Style.RESET_ALL}")
        click.echo(f"{decoded}\n")
        
        # Extract flags
        flags = PatternMatcher.extract_flags(decoded)
        if flags:
            click.echo(f"{Fore.GREEN}[FLAG]{Style.RESET_ALL} {flags[0]}")
    else:
        click.echo(f"{Fore.RED}[-] Could not detect encoding{Style.RESET_ALL}")

@cli.command()
@click.argument('data')
def base64(data):
    """Decode base64"""
    result = EncodingDetector.decode_base64(data)
    if result:
        click.echo(f"{Fore.GREEN}[+] Decoded:{Style.RESET_ALL}")
        click.echo(result)
    else:
        click.echo(f"{Fore.RED}[-] Failed to decode base64{Style.RESET_ALL}")

@cli.command()
@click.argument('data')
def hex(data):
    """Decode hex"""
    result = EncodingDetector.decode_hex(data)
    if result:
        click.echo(f"{Fore.GREEN}[+] Decoded:{Style.RESET_ALL}")
        click.echo(result)
    else:
        click.echo(f"{Fore.RED}[-] Failed to decode hex{Style.RESET_ALL}")

@cli.command()
@click.argument('data')
def rot13(data):
    """Decode ROT13"""
    result = EncodingDetector.decode_rot13(data)
    click.echo(f"{Fore.GREEN}[+] ROT13 Decoded:{Style.RESET_ALL}")
    click.echo(result)

@cli.command()
@click.argument('data')
def caesar(data):
    """Brute force Caesar cipher (all 26 shifts)"""
    click.echo(f"{Fore.CYAN}[*] Trying all Caesar shifts...{Style.RESET_ALL}\n")
    
    results = CryptoDecoder.caesar_brute_force(data)
    for shift, decrypted in results:
        if PatternMatcher.is_readable(decrypted):
            click.echo(f"{Fore.GREEN}Shift {shift}: {decrypted}{Style.RESET_ALL}")
        else:
            click.echo(f"Shift {shift}: {decrypted[:50]}...")

@cli.command()
@click.argument('data')
@click.argument('key')
def xor(data, key):
    """XOR decryption dengan key"""
    try:
        data_bytes = bytes.fromhex(data)
        key_bytes = key.encode() if isinstance(key, str) else bytes.fromhex(key)
        
        result = CryptoDecoder.xor_decrypt(data_bytes, key_bytes)
        click.echo(f"{Fore.GREEN}[+] XOR Decrypted:{Style.RESET_ALL}")
        click.echo(result.decode('utf-8', errors='replace'))
    except Exception as e:
        click.echo(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

if __name__ == '__main__':
    cli()