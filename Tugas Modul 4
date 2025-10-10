public class TokoBarang {
    private java.util.ArrayList<String> daftarBarang = new java.util.ArrayList<>();
    private java.util.Scanner scanner = new java.util.Scanner(System.in);

    public void tampilkanHeader() {
        System.out.println("========================================");
        System.out.println("   SELAMAT DATANG DI TOKO KELOMPOK 17   ");
        System.out.println("========================================");
    }

    public void tambahBarang(String namaBarang) {
        daftarBarang.add(namaBarang);
        System.out.println("Barang \"" + namaBarang + "\" berhasil ditambahkan!");
    }

    public void tampilkanDaftarBarang() {
        System.out.println("\nDaftar barang yang terdaftar:");
        if (daftarBarang.isEmpty()) {
            System.out.println("Tidak ada barang di daftar.");
        } else {
            for (String barang : daftarBarang) {
                System.out.println("- " + barang);
            }
        }
    }

    public int getTotalBarang() {
        return daftarBarang.size();
    }

    public boolean isBarangAda(String namaBarang) {
        return daftarBarang.contains(namaBarang);
    }

    public static void main(String[] args) {
        TokoBarang toko = new TokoBarang();

        toko.tampilkanHeader();

        while (true) {
            System.out.print("\nMasukkan nama barang (ketik 'SELESAI' untuk berhenti): ");
            String input = toko.scanner.nextLine();

            if (input.equalsIgnoreCase("SELESAI")) {
                break;
            }

            if (toko.isBarangAda(input)) {
                System.out.println("Barang \"" + input + "\" sudah ada di daftar!");
            } else {
                toko.tambahBarang(input);
            }
        }

        toko.tampilkanDaftarBarang();

        System.out.println("\nTotal barang yang terdaftar: " + toko.getTotalBarang());

        toko.scanner.close();
    }
}
