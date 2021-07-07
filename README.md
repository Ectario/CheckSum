# CheckSum
A quick and easy way to do the checksum for files.

## Description
CheckSum is a small piece of software that allows you to quickly recover the hash of a file.

So it is very useful when we are downloading from the internet, as it allows us to compare the key that the developer on the download site mentions to us and the key that we actually have on our computer after uploading to his site.

We can therefore observe whether the file was corrupted during the download or not. This is the principle of the checksum.

## Installation
You just need Python3 on your computer -> https://www.python.org/downloads/

## Usage

(For Unix system you need to begin the command with `python3` like `python3 CheckSum.py [file] [algorithm]`)

- Open a terminal 
- Go to the CheckSum folder
- To getHash/Compare file :

  * **getHash** for the file "exampleFile.extension" with using absolute or relative path : `CheckSum.py [path]/exampleFile.extension [hash algorithm]`  

    _Hint : You can just write `CheckSum.py exampleFile.extension [hash algorithm]`  if the file is in the same directory than CheckSum.py_
    
   * **Compare** the hash of "exampleFile.extension" with using absolute or relative path : `CheckSum.py [path]/exampleFile.extension [hash algorithm] compare=[Hash wanted]`  

      _Hint : You can just write `CheckSum.py exampleFile.extension [hash algorithm]`  if the file is in the same directory than CheckSum.py_
    
**For the moment, just 3 algorithm are managed : SHA256, SHA1, MD5**

## Example of use case

### I want to get the hash SHA-256 of the file "mySample.exa" which is in the path "C:\Users\example\Downloads\mySample.exa"

So in my command line it gives us : 

C:\Users\example\Documents\Python\CheckSum> `CheckSum.py C:\Users\example\Downloads\mySample.exa SHA256`

Then we get something like :

![image](https://user-images.githubusercontent.com/61197119/124780778-29adf000-df43-11eb-856f-451df67fac9e.png)

### I just downloaded an installer for a program that came from the internet, and the site provides me with the original MD5 hash which is the following: ac13dbe4fdcd4ca0a4816df8cfe259c6

So I want to compare the hash MD5 of the file "installer.exe" (which is in the path "C:\Users\example\Downloads\installer.exe") with the one we were given :

C:\Users\example\Documents\Python\CheckSum> 

`CheckSum.py C:\Users\example\Downloads\installer.exe MD5 compare=ac13dbe4fdcd4ca0a4816df8cfe259c6`

Then we get something like :

![image](https://user-images.githubusercontent.com/61197119/124782439-85c54400-df44-11eb-916d-1c686635e00d.png)

    
