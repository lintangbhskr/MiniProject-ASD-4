import math

class PomBensin:
    def __init__(self, jenis, harga, jumlah, metode_pembayaran):
        self.jenis = jenis
        self.harga = harga
        self.jumlah = jumlah
        self.metode_pembayaran = metode_pembayaran

    def total_pembayaran(self):
        return self.harga * self.jumlah


class Node:
    def __init__(self, pom):
        self.pom = pom
        self.next = None


class ListPomBensin:
    def __init__(self):
        self.head = None

    def tambah_data(self, pom, posisi):
        new_node = Node(pom)
        if posisi == "awal":
            new_node.next = self.head
            self.head = new_node
            print("Data berhasil ditambahkan di awal!")
        elif posisi == "tengah":
            index = int(input("Masukkan indeks data yang ingin ditambahkan: "))
            if index == 0:
                self.tambah_data(pom, "awal")
                return
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    print("Indeks tidak valid.")
                    return
                current = current.next
            if current is None:
                print("Indeks tidak valid.")
            else:
                new_node.next = current.next
                current.next = new_node
                print("Data berhasil ditambahkan di tengah!")
        elif posisi == "akhir":
            if self.head is None:
                self.head = new_node
                print("Data berhasil ditambahkan di akhir!")
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print("Data berhasil ditambahkan di akhir!")
        else:
            print("Posisi tidak valid.")

    def lihat_data(self):
        if self.head is None:
            print("Belum ada data pom bensin.")
            return
        current = self.head
        nomor = 1
        while current:
            pom = current.pom
            print("=== No. Transaksi: #{} ===".format(nomor))
            print("Jenis Bahan Bakar:", pom.jenis)
            print("Harga/liter:", pom.harga)
            print("Jumlah liter:", pom.jumlah)
            print("Metode Pembayaran:", pom.metode_pembayaran)
            print("Total Pembayaran:", pom.total_pembayaran())
            print()
            current = current.next
            nomor += 1

    def edit_data(self, index, pom_baru):
        current = self.head
        for _ in range(index):
            if current is None:
                print("Indeks tidak valid.")
                return
            current = current.next
        current.pom = pom_baru
        print("Data berhasil diubah!")

    def hapus_data(self, index):
        current = self.head
        if index == 0:
            self.head = current.next
            print("Data berhasil dihapus!")
            return
        for _ in range(index-1):
            if current is None:
                print("Indeks tidak valid.")
                return
            current = current.next
        if current is None or current.next is None:
            print("Indeks tidak valid.")
            return
        current.next = current.next.next
        print("Data berhasil dihapus!")

    def merge_sort(self, head, attribute, order):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head, attribute, order)
        right = self.merge_sort(next_to_middle, attribute, order)

        sorted_list = self.merge(left, right, attribute, order)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right, attribute, order):
        if left is None:
            return right
        if right is None:
            return left

        if order == "asc":
            if getattr(left.pom, attribute) < getattr(right.pom, attribute):
                result = left
                result.next = self.merge(left.next, right, attribute, order)
            else:
                result = right
                result.next = self.merge(left, right.next, attribute, order)
        elif order == "desc":
            if getattr(left.pom, attribute) > getattr(right.pom, attribute):
                result = left
                result.next = self.merge(left.next, right, attribute, order)
            else:
                result = right
                result.next = self.merge(left, right.next, attribute, order)
        return result

    def sort_data(self):
        if self.head is None or self.head.next is None:
            return

        print("\nPilih Atribut untuk Sorting:")
        print("1. Jenis Bahan Bakar")
        print("2. Harga/liter")
        print("3. Jumlah liter")
        print("4. Metode Pembayaran")
        attribute_choice = input("Masukkan pilihan (1/2/3/4): ")

        attribute_mapping = {
            "1": "jenis",
            "2": "harga",
            "3": "jumlah",
            "4": "metode_pembayaran"
        }

        if attribute_choice in attribute_mapping:
            attribute = attribute_mapping[attribute_choice]
        else:
            print("Pilihan tidak valid.")
            return

        order_choice = input("Pilih urutan Sorting (asc/desc): ")
        if order_choice not in ["asc", "desc"]:
            print("Pilihan tidak valid.")
            return

        self.head = self.merge_sort(self.head, attribute, order_choice)
        print("Data berhasil diurutkan!")

    def jump_search(self, attribute, value):
        if self.head is None:
            print("Tidak ada data yang tersedia untuk pencarian.")
            return None

        length = self.get_length()
        jump = int(math.sqrt(length))
        current = self.head

        while current and getattr(current.pom, attribute) < value:
            prev = current
            for _ in range(jump):
                if current.next:
                    current = current.next
                else:
                    break

        while prev and getattr(prev.pom, attribute) < value:
            prev = prev.next

        if prev and getattr(prev.pom, attribute) == value:
            return prev.pom
        else:
            print(f"Tidak ditemukan data dengan {attribute} '{value}'.")
            return None

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length


def buat_pom_bensin(jenis, harga):
    jumlah = int(input(f"Masukkan jumlah liter {jenis}: "))
    print("Pilih Metode Pembayaran:")
    print("1. Cash")
    print("2. Debit")
    metode_pilihan = input("Masukkan pilihan (1/2): ")
    metode_pembayaran = "Cash" if metode_pilihan == "1" else "Debit"
    return PomBensin(jenis, harga, jumlah, metode_pembayaran)


# Main program
if __name__ == "__main__":
    list_pom = ListPomBensin()
    jenis_bbm = {
        "1": ("Pertalite", 10000),
        "2": ("Pertamax", 13500),
        "3": ("Pertamax Turbo", 14750)
    }

    while True:
        print("\n=== Aplikasi CRUD Pom Bensin ===")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Sorting Data")
        print("6. Cari Data")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

        if pilihan == "1":
            print("\n=== Tambah data Pom Bensin ===")
            print("1. Tambah Data di Awal")
            print("2. Tambah Data di Tengah")
            print("3. Tambah Data di Akhir")
            tambah_pilihan = input("Masukkan pilihan (1/2/3): ")
            if tambah_pilihan in ["1", "2", "3"]:
                print("Pilih Jenis Bahan Bakar:")
                for key, value in jenis_bbm.items():
                    print(f"{key}. {value[0]} - Harga/liter: {value[1]}")
                jenis_pilihan = input("Masukkan pilihan (1/2/3): ")
                if jenis_pilihan in jenis_bbm:
                    jenis, harga = jenis_bbm[jenis_pilihan]
                    pom_baru = buat_pom_bensin(jenis, harga)

                    print("\nBerikut data yang anda input:")
                    print("Jenis Bahan Bakar:", pom_baru.jenis)
                    print("Harga/liter:", pom_baru.harga)
                    print("Jumlah liter:", pom_baru.jumlah)
                    print("Metode Pembayaran:", pom_baru.metode_pembayaran)
                    print("Total Pembayaran:", pom_baru.total_pembayaran())

                    konfirmasi = input("\nApakah data di atas sudah benar? (y/n): ")
                    if konfirmasi.lower() == "y":
                        if tambah_pilihan == "1":
                            list_pom.tambah_data(pom_baru, "awal")
                        elif tambah_pilihan == "2":
                            list_pom.tambah_data(pom_baru, "tengah")
                        elif tambah_pilihan == "3":
                            list_pom.tambah_data(pom_baru, "akhir")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Pilihan tidak valid.")
        elif pilihan == "2":
            list_pom.lihat_data()
        elif pilihan == "3":
            index = int(input("Masukkan indeks data yang ingin diubah: "))
            if index > 0 and index <= len(list_pom):
                jenis, harga = list_pom[index - 1].pom.jenis, list_pom[index - 1].pom.harga
                pom_baru = buat_pom_bensin(jenis, harga)

                print("\nBerikut data yang akan diubah:")
                print("Jenis Bahan Bakar:", pom_baru.jenis)
                print("Harga/liter:", pom_baru.harga)
                print("Jumlah liter:", pom_baru.jumlah)
                print("Metode Pembayaran:", pom_baru.metode_pembayaran)
                print("Total Pembayaran:", pom_baru.total_pembayaran())

                konfirmasi = input("\nApakah data di atas sudah benar? (y/n): ")
                if konfirmasi.lower() == "y":
                    list_pom.edit_data(index - 1, pom_baru)
            else:
                print("Indeks tidak valid.")
        elif pilihan == "4":
            index = int(input("Masukkan indeks data yang ingin dihapus: "))
            if index > 0 and index <= len(list_pom):
                list_pom.hapus_data(index - 1)
            else:
                print("Indeks tidak valid.")
        elif pilihan == "5":
            list_pom.sort_data()
        elif pilihan == "6":
            print("\n=== Pencarian Data ===")
            print("1. Berdasarkan Jenis Bahan Bakar")
            print("2. Berdasarkan Harga/liter")
            search_choice = input("Masukkan pilihan (1/2): ")

            if search_choice == "1":
                jenis = input("Masukkan jenis bahan bakar yang ingin dicari: ")
                result = list_pom.jump_search("jenis", jenis)
                if result:
                    print("Data ditemukan:")
                    print("Jenis Bahan Bakar:", result.jenis)
                    print("Harga/liter:", result.harga)
                    print("Jumlah liter:", result.jumlah)
                    print("Metode Pembayaran:", result.metode_pembayaran)
                    print("Total Pembayaran:", result.total_pembayaran())
            elif search_choice == "2":
                harga = float(input("Masukkan harga per liter yang ingin dicari: "))
                result = list_pom.jump_search("harga", harga)
                if result:
                    print("Data ditemukan:")
                    print("Jenis Bahan Bakar:", result.jenis)
                    print("Harga/liter:", result.harga)
                    print("Jumlah liter:", result.jumlah)
                    print("Metode Pembayaran:", result.metode_pembayaran)
                    print("Total Pembayaran:", result.total_pembayaran())
        elif pilihan == "7":
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
