------------------
![maxresdefault](https://user-images.githubusercontent.com/49293816/188544424-4b56d278-b797-42bc-87e1-60c4adfdd1b9.jpg)

------------------
# Xorcry

Xorcry is an open-source ransomware written in python3 to explain how actually a ransomware or a crypter with a given cryptography algorithm do works.

# Why?

as a curious person, I really love to understand how things get to work deeply, and one of the questions that I've been asking for a long time was how does the ransomware work? after a lot of disappointing research to give my question a clear answer, I started diving into cryptography algorithms and malware understanding, so without any further ado let's leave this boring introduction aside a bit and go with the cool part.

## How Does Xorcry Work?

first of all, you must make sure that I did this tool only for educational purposes, secondly, if you are a cryptographer you will find this writeup boring you.

there are a lot of cryptography algorithms you can use to make ransomware but I'm not going to explain them for the reason that I didn't use any known crypto algorithm, in fact, what I  did is reading files as binary and xor them with a given key and this is what called **xor cipher**, but wait, I said **xor cipher** hmmm what is this? well, this will be our next topic.

## Xor Cipher

I'll assume that you have a background about Logic gates and what are they, but if you don't I  want you to take a deep look at this
article from Wikipedia :

https://en.wikipedia.org/wiki/Logic_gate

well as you noticed  In **xor** operation, the output is true when the inputs differ. In other words, **xor** operation means either one but not both or none.

Below you can find the principles of **xor** (^ denotes the **xor** operation):

```
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

**xor** cipher employs the **xor** logical operation in order to encrypt data. First, a random key is generated or is chosen by you. Then, **xor** operation is performed using the key so that an encrypted data is created. In order to decrypt, the same key should be used and **xor** operation should be run again.

**xor** operation uses the same key for both encryption and decryption operations. That is why it is known as a symmetric encryption.

## Code Explaining

before covering the code explaining, I'll assume again that you have the basics of the programming language Python in order to understand The rest of the code because I will cover only the most important function which is :

```python
def encrypt(self , f) :

		''' If the file's extension is one of the list declared above then start XoRing '''

		if self.check_ex(f) :

			try :
				with open(f , mode = "rb") as _file :
					rd = bytearray(_file.read())
				for n , v in enumerate(rd) :
					rd[n] = v ^ self.key
				with open(f , mode = "wb") as _nf :
					_nf.write(rd)

				''' This exception is especially for file permissions '''

			except :
				pass
```

the first line I will talk about is the operation of reading the file we want to encrypt in binary mode and declare a variable where we will put the binary data as a list using the built-in function _bytearray()_, I found this article useful for those who want to understand how does the *bytearray()* work :

https://www.geeksforgeeks.org/python-bytearray-function/

after that, there is a for loop to edit the list by performing **xor** operation for each element in the list with the given key and finally rewrite the file we have opened previously with the new encrypted data.

## Contact Me

For Any Questions You Can Find Me on This Platforms :

* [Twitter][_1]
* [Instagram][_2]

[_1]: https://twitter.com/amait0u
[_2]: https://www.instagram.com/amait0u

# Disclaimer
This program must be used for legal purposes! I am not responsible for anything you do with it.
