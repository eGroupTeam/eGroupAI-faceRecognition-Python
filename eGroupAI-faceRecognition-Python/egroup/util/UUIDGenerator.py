import uuid, base64, random


class UUIDGenerator:

    def getBase64UUID(self) -> str:
        base64uuid = base64.urlsafe_b64encode(uuid.uuid1().bytes).rstrip(b'=').decode('ascii')
        return base64uuid.replace("-", "").replace("-", "")

    def getUUID(self) -> str:
        r"""Returns UUID

        Params::

            None

        """
        return str(uuid.uuid4()).replace("-", "")

    def getRandomUUID(self, size_: int) -> str:
        char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                     'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                     'Y', 'Z']

        random_uuid = ""
        for x in range(0, size_):
            random_uuid += char_list[random.randint(0, len(char_list))]
        return random_uuid
