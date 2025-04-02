# Vigenère Cipher Variants

This repository contains three different implementations of the Vigenère cipher, each using a distinct method for generating the cipher's "gamma" (key stream) from the secret key.

## Files Overview

### 1. main.py - Standard Vigenère Cipher
- **Method**: Repeating short key
- **Description**:
  - Classic Vigenère implementation
  - The key is repeated to match the length of the plaintext
  - Simple and most common version of the cipher

### 2. vigener_openText.py - Vigenère with Plaintext Self-Key
- **Method**: Plaintext-based self-key
- **Description**:
  - Uses the plaintext itself to extend the key
  - Initial key is a single character
  - Subsequent key values come from previous plaintext characters
  - More secure than standard Vigenère but vulnerable to known-plaintext attacks

### 3. vigener_close.py - Vigenère with Ciphertext Self-Key
- **Method**: Ciphertext-based self-key
- **Description**:
  - Uses the ciphertext itself to extend the key
  - Initial key is a single character
  - Subsequent key values come from previous ciphertext characters
  - More resistant to known-plaintext attacks than plaintext version

## Usage Instructions

For all three scripts:
1. Run the Python file: `python filename.py`
2. Enter your plaintext when prompted
3. Enter the initial key (single character for self-key versions)
4. View the encrypted output
5. For decryption, run again and enter ciphertext when prompted

### Key Requirements:
- **Standard Vigenère**: Any length key (letters only)
- **Self-key variants**: Single character key (a-z)

## Technical Notes
- All implementations work with lowercase English alphabet only
- Non-alphabetic characters are preserved unchanged
- Modular arithmetic ensures wrap-around from z to a
- Self-key versions provide better security than standard repeating key
- Ciphertext self-key version is most resistant to cryptanalysis

These implementations demonstrate how different gamma generation methods affect the security properties of the Vigenère cipher, from the vulnerable standard version to more secure self-keying variants.
