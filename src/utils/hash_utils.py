import bcrypt

class Hasher:
    """
    Password hashing with Bcrypt.
    """
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        This method verify the plain password and hashed password.
        :param plain_password: plain password
        :param hashed_password: hashed password
        :return: True if verify else False
        """
        return bcrypt.checkpw(plain_password.strip().encode("utf-8"), hashed_password.encode("utf-8"))

    @staticmethod
    def hash_password(password):
        """
        This method is used to create the hashed password.
        :param password: password
        :return: hashed password
        """
        return bcrypt.hashpw(password.strip().encode("utf-8"), bcrypt.gensalt(rounds=4))