from database.mongodb import client


try:
    client.admin.command("ping")
    print("MongoDB Atlas berhasil terhubung! ✅")

except Exception as e:
    print("Gagal terhubung ke MongoDB Atlas ❌")
    print(e)

finally:
    client.close()