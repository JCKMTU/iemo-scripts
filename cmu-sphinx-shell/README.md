# Phoneme recognition using Speech recognition toolkit, pocketsphinx

### Prerequisite:
 - get neccessities
 	- [sphinxbase][sphinxbase]
 	- [pocketsphinx][pocketsphinx]
 	- [language-model][cmumodel]
 	- [cmu-dict][cmudict]

 - If you downloaded repository from git...
    ```sh
    $ ./autogen.sh
    ```
 - install sphinxbase before pocketsphinx
 	```sh
 	$ ./configure
 	$ make
 	$ sudo make install
 	```

 - install pocketsphinx
 	```sh
 	$ ./configure
 	$ make
 	$ sudo make install
 	```

 - link libraries
 	```sh
 	$ export LD_LIBRARY_PATH=/usr/local/lib
 	$ export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
 	```

 - If make fails...
 	```sh
 	# Try this!!!
 	$ autoreconf -vfi
 	```

 - Prepare sound files
 	It should be 16kHz and single channel sound track. 
 
 - Run script
 	```sh
 	$ ./sphinx.sh [SOUND-FILE] [POCKETSPHINX-HOME-DIR]
 	```

### About phoneme recognition
See this [link](https://cmusphinx.github.io/wiki/phonemerecognition/)


[sphinxbase]: <https://github.com/cmusphinx/sphinxbase>
[pocketsphinx]: <https://github.com/cmusphinx/pocketsphinx>
[cmudict]: <https://github.com/cmusphinx/cmudict>
[cmumodel]: <https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/US%20English/>
