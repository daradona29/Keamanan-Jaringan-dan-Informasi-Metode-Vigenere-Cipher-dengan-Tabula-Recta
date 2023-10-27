def generate_tabula_recta():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tabula_recta = [[(i + j) % 26 for j in range(26)] for i in range(26)]
    return tabula_recta


def vigenere_encrypt(plaintext, key):
    tabula_recta = generate_tabula_recta()
    ciphertext = ""

    print("\nEncrypting:")
    print("  PT  | Key |  Row  |  Col  |  Ord  | CT")
    print("-" * 40)

    i = 0  # Indeks untuk key
    for char in plaintext:
        if char.isalpha():  # Periksa apakah karakter adalah huruf
            row = ord(key[i % len(key)].upper()) - ord("A")
            col = ord(char.upper()) - ord("A")

            # Menampilkan nilai ord, row, col saat enkripsi
            print(
                f"  {char}   |  {key[i % len(key)].upper()}  |   {row:2}   |   {col:2}   |   {ord(char):3}   |  {chr(ord('A') + tabula_recta[row][col])}"
            )

            # Sesuaikan dengan huruf kecil atau kapital pada plaintext
            ciphertext += (
                chr(ord("a") + tabula_recta[row][col])
                if char.islower()
                else chr(ord("A") + tabula_recta[row][col])
            )
            i += 1

        else:
            ciphertext += char

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    tabula_recta = generate_tabula_recta()
    plaintext = ""

    print("\nDecrypting:")
    print("  CT  | Key |  Row  |  Col  |  Ord  | PT")
    print("-" * 40)

    i = 0  # Indeks untuk key
    for char in ciphertext:
        if char.isalpha():  # Periksa apakah karakter adalah huruf
            row = ord(key[i % len(key)].upper()) - ord("A")
            col = (ord(char.upper()) - ord("A") - row + 26) % 26

            # Menampilkan nilai ord, row, col saat dekripsi
            print(
                f"  {char}   |  {key[i % len(key)].upper()}  |   {row:2}   |   {col:2}   |   {ord(char):3}   |  {chr(ord('A') + col)}"
            )

            # Sesuaikan dengan huruf kecil atau kapital pada ciphertext
            plaintext += chr(ord("a") + col) if char.islower() else chr(ord("A") + col)
            i += 1

        else:
            plaintext += char

    return plaintext


def display_tabula_recta():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tabula_recta = generate_tabula_recta()

    print("Tabula Recta:")
    print("   " + " ".join(alphabet))
    for i in range(26):
        row = tabula_recta[i % 26]
        row_chars = [alphabet[x] if x < 26 else alphabet[x - 26] for x in row]
        print(alphabet[i % 26] + " " + " ".join(row_chars))


def main():
    display_tabula_recta()

    choice = input("\nMenu: \n1. Enkripsi \n2. Dekripsi \nPilih 1 atau 2: ")

    if choice == "1":
        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan key: ")
        ciphertext = vigenere_encrypt(plaintext, key)
        print("Ciphertext:", ciphertext)
    elif choice == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan key: ")
        decrypted_text = vigenere_decrypt(ciphertext, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
