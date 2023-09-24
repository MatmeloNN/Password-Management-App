passwords = {}

def main():
    while True:
        print("Parola Yönetimi Uygulaması")
        print("1. Parola Ekle")
        print("2. Parolaları Görüntüle")
        print("3. Parola Sil")
        print("4. Çıkış")
        
        choice = input("Lütfen bir seçenek seçin: ")
        
        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

def add_password():
    website = input("Web sitesi adı: ")
    username = input("Kullanıcı adı: ")
    password = input("Parola: ")
    passwords[website] = {"username": username, "password": password}
    print(f"{website} için parola eklendi.")

def view_passwords():
    for website, info in passwords.items():
        print(f"Web sitesi: {website}")
        print(f"Kullanıcı adı: {info['username']}")
        print(f"Parola: {info['password']}")
        print("-" * 20)

def delete_password():
    website = input("Silmek istediğiniz web sitesi adını girin: ")
    if website in passwords:
        del passwords[website]
        print(f"{website} için parola silindi.")
    else:
        print(f"{website} adında bir web sitesi bulunamadı.")

if __name__ == "__main__":
    main()
