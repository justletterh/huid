from utils import from_digits,dupe

blocklen=8

b26alpha="abcdefghijklmnopqrstuvwxyz".upper()
b32alpha="abcdefghijklmnopqrstuvwxyz234567".upper()
b64alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
b84alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=[]()&*^%$#@!<>;:\"\'."

binmax=eval(f"0b{'1'*blocklen}")
octmax=eval(f"0o{'7'*blocklen}")
decmax=eval("9"*blocklen)
hexmax=eval(f"0x{'F'*blocklen}")
b26max=from_digits(dupe(25,blocklen),26)
b32max=from_digits(dupe(31,blocklen),32)
b64max=from_digits(dupe(63,blocklen),64)
b84max=from_digits(dupe(83,blocklen),84)


default=0

bl=blocklen

del from_digits,dupe