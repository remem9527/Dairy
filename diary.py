from ecies import encrypt, decrypt
from bitsv import PrivateKey
from datetime import datetime

# have to parse transaction data myself because of a bug in bitsv.network.transaction.Transaction
from bitsv.network.services.bitindex3 import BitIndex3MainNet
network_api = BitIndex3MainNet(api_key=None)

OP_PUSHDATA1 = b'\x4c'
OP_PUSHDATA2 = b'\x4d'
OP_PUSHDATA4 = b'\x4e'

class User:
    def __init__(self, private_key=None):
        if private_key is None:
            self.key = PrivateKey()
        else:
            self.key = PrivateKey(private_key)
        self.__prihex = self.key.to_hex()
        self.__pubhex = self.key.public_key.hex()

    def encrypt(self, message):
        if isinstance(message, str):
            message = message.encode()
        return encrypt(self.__pubhex, message)

    def decrypt(self, cipher):
        return decrypt(self.__prihex, cipher)

    def send_diary(self, message):
        if isinstance(message, Diary):
            message = message.content
        cipher = self.encrypt(message)
        return self.key.send_op_return([cipher])

    def get_diaries(self):
        tx_hash_list = self.key.get_transactions()
        diary_list = []

        # have to parse transaction data myself because of a bug in bitsv.network.transaction.Transaction
        for tx_hash in tx_hash_list:
            tx_dict = network_api.raw_get_transaction(tx_hash)
            for out in tx_dict['vout']:
                out_hex = out['scriptPubKey']['hex']
                if out_hex[0:2] == '6a':
                    if int(out_hex[2:4], 16) < 0x4c:
                        data_hex = out_hex[4:]
                    else:
                        data_hex = out_hex[6:]

                    data_bytes = bytes.fromhex(data_hex)
                    try:
                        content = self.decrypt(data_bytes)
                    except:
                        continue

                    content = content.decode()
                    diary = Diary(content)
                    diary.blocktime = tx_dict['time']
                    diary.txhash = tx_hash
                    diary_list.append(diary)

        return diary_list

    def print_diaries(self):
        diary_list = self.get_diaries()
        for diary in diary_list:
            diary.print()

class Diary:
    def __init__(self, content):
        self.content = content
        self.blocktime = None
        self.txhash = None

    def print(self):
        print('='*30)
        blocktime = datetime.utcfromtimestamp(int(self.blocktime))
        print('Blocktime: {}'.format(blocktime))
        print('Txid: {}'.format(self.txhash))
        print('Content:')
        print(self.content)
        print()