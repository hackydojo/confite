from abc import abstractmethod, ABCMeta


# ---------------------------------------------------------
# CLASS DECRYPTION KEY NOT FOUND ERROR
# ---------------------------------------------------------
class DecryptionKeyNotFoundError(Exception):
    """
    Raised when the encryption key provider fails to
    retrieve a valid encryption/decryption key
    """
    pass


# ---------------------------------------------------------
# CLASS DECRYPTION KEY ERROR
# ---------------------------------------------------------
class DecryptionKeyError(Exception):
    """
    Raised when the decryption key is invalid and fails to
    properly decrypt the encrypted properties.
    """
    pass


# ---------------------------------------------------------
# CLASS DECRYPTION KEY PROVIDER
# ---------------------------------------------------------
class DecryptionKeyProvider:

    """
    Base class for implementations of concrete providers
    that \"know\" how to read the proper decryption key to
    be used
    """

    __metaclass__ = ABCMeta

    # -----------------------------------------------------
    # PROPERTY ENCRYPTION KEY
    # -----------------------------------------------------
    @property
    @abstractmethod
    def encryption_key(self) -> str:
        pass



