import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from rag.retriever import retrieve_information


def common_information(query: str) -> str:
    """
    Mencari informasi umum terkait proses belanja.

    Gunakan tool ini untuk pertanyaan tentang:
    - pengiriman
    - pelacakan pesanan
    - cara membeli produk
    - checkout
    - pembayaran
    - refund
    - retur
    - pembatalan pesanan
    - komplain
    - voucher
    - akun dan alamat pengiriman

    Jangan gunakan tool ini untuk mencari rekomendasi,
    spesifikasi, harga, atau perbandingan produk.

    Args:
        query: Pertanyaan pengguna.

    Returns:
        Informasi yang paling relevan dari knowledge base.
    """

    results = retrieve_information(query, top_k=3)

    if not results:
        return "Maaf, informasi yang relevan tidak ditemukan."

    best_result = results[0]

    # Threshold sederhana agar sistem tidak asal menjawab
    if best_result["score"] < 0.15:
        return (
            "Maaf, informasi yang relevan belum tersedia "
            "di knowledge base."
        )

    return (
        f"Kategori: {best_result['category']}\n"
        f"Pertanyaan: {best_result['question']}\n"
        f"Jawaban: {best_result['answer']}"
    )

if __name__ == "__main__":
    query = input("Pertanyaan: ")

    result = common_information(query)

    print("\nJawaban:")
    print(result)