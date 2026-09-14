from database.mongodb import client


def test_mongodb_connection():
    client.admin.command("ping")

    print("MongoDB Atlas berhasil terhubung! ✅")


if __name__ == "__main__":
    try:
        client.admin.command("ping")
        print("MongoDB Atlas berhasil terhubung! ✅")
    except Exception as e:
        print("Gagal terhubung ke MongoDB Atlas ❌")
        print(e)