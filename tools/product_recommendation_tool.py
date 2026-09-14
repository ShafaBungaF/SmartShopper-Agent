import json
import os
import re


def load_products():
    """
    Membaca data produk dari products.json.
    """

    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    file_path = os.path.join(
        base_dir,
        "data",
        "products.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def extract_budget(query: str):
    """
    Mengambil budget dari pertanyaan pengguna.
    """

    query_lower = query.lower()

    # Format: 5 juta / 5.5 juta / 5,5 juta
    match = re.search(
        r'(?:budget|maksimal|max|dibawah|di bawah|sekitar)?\s*'
        r'(\d+(?:[.,]\d+)?)\s*(juta|jt)',
        query_lower
    )

    if match:
        number = match.group(1).replace(",", ".")
        value = float(number) * 1_000_000
        return int(value)

    # Format angka langsung, misalnya 5000000
    match = re.search(
        r'(?:budget|maksimal|max|dibawah|di bawah)?\s*'
        r'(?:rp\.?\s*)?(\d{6,})',
        query_lower
    )

    if match:
        return int(match.group(1))

    return None

def extract_category(query: str):
    """
    Mengambil kategori produk dari pertanyaan pengguna.
    """

    query_lower = query.lower()

    categories = {
        "smartphone": ["smartphone", "hp", "handphone"],
        "laptop": ["laptop", "notebook"],
        "audio": ["headphone", "earbuds", "earphone"]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", query_lower):
                return category

    return None


def product_recommendation(
    query: str,
    max_price: int = None,
    category: str = None
) -> str:
    """
    Memberikan rekomendasi produk berdasarkan kebutuhan pengguna.

    Gunakan tool ini untuk:
    - rekomendasi produk
    - mencari produk berdasarkan kebutuhan
    - mencari produk berdasarkan budget
    - membandingkan pilihan produk

    Jangan gunakan tool ini untuk:
    - pengiriman
    - pembayaran
    - refund
    - retur
    - pembatalan pesanan
    - tracking pesanan

    Args:
        query: Kebutuhan atau preferensi pengguna.
        max_price: Batas harga maksimum jika disebutkan.
        category: Kategori produk jika diketahui.

    Returns:
        Daftar produk yang paling relevan.
    """

    products = load_products()

    query_lower = query.lower()

    # Ambil budget otomatis dari pertanyaan pengguna
    detected_budget = extract_budget(query)

    if detected_budget:
        max_price = detected_budget

    # Ambil kategori otomatis dari pertanyaan pengguna
    detected_category = extract_category(query)

    if detected_category:
        category = detected_category    

    # Filter berdasarkan kategori
    filtered_products = products

    if category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"].lower() == category.lower()
        ]

    # Filter berdasarkan budget
    if max_price:
        filtered_products = [
            product
            for product in filtered_products
            if product["price"] <= max_price
        ]

    if not filtered_products:
        return "Maaf, tidak ditemukan produk yang sesuai dengan kriteria Anda."

    # Hitung skor sederhana berdasarkan kecocokan fitur
    scored_products = []

    for product in filtered_products:

        score = 0

        text = (
            product["name"]
            + " "
            + product["description"]
            + " "
            + " ".join(product["features"])
        ).lower()

        query_words = query_lower.split()

        for word in query_words:
            if len(word) > 2 and word in text:
                score += 1

        scored_products.append(
            (score, product)
        )

    # Urutkan berdasarkan skor, kemudian rating
    scored_products.sort(
        key=lambda x: (x[0], x[1]["rating"]),
        reverse=True
    )

    top_products = [
        product
        for score, product in scored_products[:3]
    ]

    result = "Rekomendasi produk:\n\n"

    for product in top_products:
        result += (
            f"- {product['name']}\n"
            f"  Harga: Rp{product['price']:,}\n"
            f"  Rating: {product['rating']}\n"
            f"  Deskripsi: {product['description']}\n\n"
        )

    return result


if __name__ == "__main__":

    query = input("Kebutuhan produk: ")

    result = product_recommendation(query)

    print("\nHasil Rekomendasi:")
    print(result)