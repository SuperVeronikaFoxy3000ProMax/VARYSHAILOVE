from pathlib import Path
import secrets
words = Path('words').read_text().splitlines()
passphrase = ' '.join(secrets.choice(words) for i in range(4))
print(passphrase)
