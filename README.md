# Password-Generator

This simple program generates a password and save it in the archive called password.txt at the same directory that is your Password Generator.exe.

You can download it from this link of my Dropbox: https://www.dropbox.com/s/voxy7fgts7a0ey2/Password%20Generator.exe?dl=0

Password Generator has a simple interface. All you do in this program, it is by your keyboard like in the terminal.

<h2>Explaning how it works:</h2>

There are few types of password that you can choose to generate yours. Moreover, I really recommend you choose more than twelve characters for your password to be shure of that the password generated is really strong.<br/>
L   => Only letters<br/>
N   => Only numbers<br/>
C   => Only special characters<br/>
LN  => Letters and numbers<br/>
LC  => Letters and special characters<br/>
NC  => Numbers and special characters<br/>
LNC => Letters, numbers and special characters<br/>

After that, you can name your password and this name will be at the .txt file to separate password of others.

<h2>What I use to create this program:</h2>
How I was leaning python and using it at my college, I choose it to create this program. Besides that, to create an executable of the python file I used the PyInstaller is a normal Python package.

Also, I put a custom icon in the .exe file. I took it from the site flaticon: <a href="https://www.flaticon.com/free-icons/password" title="password icons">Password icons created by Freepik - Flaticon</a>

<h2>Big problem!</h2>
After compiling the main.py into an executable, I faced a big problem. When I download the archive (at my Dropbox), the Windows Defender accused it of being a virus. After that, I use the site VirusTotal to try it in others anti-virus. To my surprise, at the first time, 6 anti-virus thinks that is a trojan or a malicious archive.

Moreover, I wasted a good time searching how to make the pyinstaller creates my .exe without this false positive. Sadly, the best I reached at VirusTotal display 4 of 65 of the tests and the Windows Defender keeps accusing it of being a malicious archive.
