from infra.repository.user_repository import User_repository

if __name__ == "__main__":
    repository = User_repository()

    repository.create_user("Data base with hash salt","@giithub@","github@example.com")
    repository.login("git_hub@example.com", "@giithub@")
    repository.delete(1)

