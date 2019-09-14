from diary import User

private_key = 'Kzr6GbF9RpiuczdwJV9CS2STu9FvDfa7QPHRvx7zui51gxNxnTS3'
user = User(private_key)

diary1 = '''
I have a super big secret and I want to write it on-chain.
'''
user.send_diary(diary1)

diary2 = '''
But I won't write it under this address because you already know the private key!
'''
user.send_diary(diary2)

user.print_diaries()
