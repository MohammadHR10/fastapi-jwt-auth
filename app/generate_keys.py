import secrets
print(f"JWT_SECRET_KEY: {secrets.token_hex(32)}")
print(f"JWT_REFRESH_SECRET_KEY: {secrets.token_hex(32)}")
