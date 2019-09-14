Diary: A permanent and private on-chain diary book, powered by BSV.
=======================================================================

.. code-block:: python

    >>> from diary import User
    >>> private_key = 'Kzr6GbF9RpiuczdwJV9CS2STu9FvDfa7QPHRvx7zui51gxNxnTS3'
    >>> user = User(private_key)
    >>> diary1 = '''
    ... I have a super big secret and I want to write it on-chain.
    ... '''
    >>> user.send_diary(diary1)
    '30d58b9d7d9bbdd6d93d0096fba595054812010d65605c394723f853d4ca8cb7'
    >>> diary2 = '''
    ... But I won't write it under this address because you already know the private key!
    ... '''
    >>> user.send_diary(diary2)
    '39382cddd129a6c359b516fda93f91c4753a13c8db5831f00d3623bc6ff3cbc0'
    >>> user.print_diaries()
    ==============================
    Blocktime: 2019-09-14 07:53:53
    Txid: 30d58b9d7d9bbdd6d93d0096fba595054812010d65605c394723f853d4ca8cb7
    Content:
    I have a super big secret and I want to write it on-chain.


    ==============================
    Blocktime: 2019-09-14 07:54:49
    Txid: 39382cddd129a6c359b516fda93f91c4753a13c8db5831f00d3623bc6ff3cbc0
    Content:
    But I won't write it under this address because you already know the private key!


Here are the transactions. The data is encrypted by Elliptic Curve Integrated Encryption Scheme.
`<https://whatsonchain.com/tx/30d58b9d7d9bbdd6d93d0096fba595054812010d65605c394723f853d4ca8cb7>`_
`<https://whatsonchain.com/tx/39382cddd129a6c359b516fda93f91c4753a13c8db5831f00d3623bc6ff3cbc0>`_


Planned improvements
--------------------

- Support advanced text format.
- Support more encryption schemes.
- Support a permission system. Each diary can be set to be only visible to your self, totally public or visible to certain group of people. For the last one, the key for decryption would be sent to your friends through an encrypted on-chain message, when the diary is sent.
- Function of revealing the encrypted diary at some future time.


Credits
-------

- `AustEcon`_ for bitSV.
- `ecies`_ for eciespy.

.. _AustEcon: https://github.com/AustEcon/bitsv
.. _ecies: https://github.com/ecies/py
