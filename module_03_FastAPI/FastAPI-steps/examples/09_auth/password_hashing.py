from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(raw: str) -> str:
    return pwd_context.hash(raw)

def verify_password(raw: str, hashed: str) -> bool:
    return pwd_context.verify(raw, hashed)

if __name__ == "__main__":
    password = "my-secret-pass"
    hashed = hash_password(password)

    print(f"Password: {password}")
    print(f"Hashed Password: {hashed}")
    print(f"Verify OK: {verify_password(password, hashed)}")
    print(f"Verify OK: {verify_password('123456', hashed)}")