# 🛍️ SmartShopper Agent

SmartShopper Agent adalah AI-powered shopping assistant yang membantu pengguna dalam aktivitas belanja online.

Sistem ini menggunakan Google Agent Development Kit (ADK) dan memiliki kemampuan untuk memahami intent pengguna serta memilih tool yang sesuai secara otomatis.

## 🎯 Tujuan Sistem

SmartShopper Agent dikembangkan untuk:

- Membantu pengguna mendapatkan informasi umum terkait proses belanja.
- Memberikan rekomendasi produk berdasarkan kebutuhan dan budget.
- Menggunakan knowledge base untuk menjawab pertanyaan umum.
- Melakukan automatic routing berdasarkan intent pengguna.
- Mengintegrasikan RAG dengan MongoDB Atlas sebagai penyimpanan knowledge base.
- Memberikan respons yang relevan berdasarkan data yang tersedia.

---

## ✨ Fitur Utama

### 1. Common Information

Digunakan untuk pertanyaan terkait proses dan informasi umum dalam berbelanja, seperti:

- Pengiriman
- Tracking pesanan
- Cara membeli produk
- Checkout
- Pembayaran
- Refund
- Retur
- Pembatalan pesanan
- Komplain
- Voucher
- Akun
- Alamat pengiriman

Informasi diperoleh dari knowledge base yang disimpan di MongoDB Atlas dan dicari menggunakan metode retrieval berbasis TF-IDF dan cosine similarity.

### 2. Product Recommendation

Digunakan untuk memberikan rekomendasi produk berdasarkan:

- Kebutuhan pengguna
- Kategori produk
- Budget
- Fitur produk
- Rating produk

Sistem melakukan filtering berdasarkan kategori dan budget, kemudian melakukan ranking berdasarkan relevansi dan rating.

### 3. Automatic Routing

Agent menentukan tool yang digunakan berdasarkan intent pengguna.

Contoh:

```text
"Bagaimana cara melakukan refund?"
            ↓
   common_information