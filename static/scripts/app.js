// Tangani pengiriman form pembelian
document.getElementById("formPembelian").addEventListener("submit", async (e) => {
    e.preventDefault(); // Mencegah reload halaman
  
    // Ambil data dari form
    const data = {
      game: document.getElementById("gamePembelian").value,
      id: document.getElementById("idPembelian").value,
      jumlah: document.getElementById("jumlahPembelian").value,
      metode: document.getElementById("metodePembelian").value,
      pesan: document.getElementById("pesanPembelian").value,
    };
  
    // Validasi input
    if (!data.game || !data.id || !data.jumlah || !data.metode) {
      alert("Harap lengkapi semua field!");
      return;
    }
  
    // Kirim data ke backend
    try {
      const response = await fetch("/submit-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
  
      const result = await response.json();
      if (result.status === "success") {
        alert("Pesanan berhasil dikirim!");
        document.getElementById("formPembelian").reset(); // Reset form
      } else {
        alert("Gagal mengirim pesanan: " + result.message);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Terjadi kesalahan saat mengirim pesanan.");
    }
  });