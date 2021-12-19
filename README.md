# Finding the CRC checksum.
**This code is a search for the CRC checksum of any file, where the input data is the path to this file and either a manually entered polynomial or a selected polynomial that is embedded in the program.**

<div align="center">
  
<img alt="GitHub (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/pettyderf/CRC">
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/pettyderf/CRC">

[Without using integrated polynomials](#without-using-integrated-polynomials) •  
[With using integrated polynomials](#with-using-integrated-polynomials) • 
  
</div>

#

For this software implementation to work, 2 libraries are needed: *docopt* and *pprint*.

*Pprint* is a built-in library, so its installation is not required.

*docopt* must be installed with the following console command:

```sh
pip3 install docopt
```

To display a small instruction about the program, type *-h* or *-help*.

```sh
CRC.py -help
```

![](pic/-help.jpg)

# Without using integrated polynomials

To do this, simply enter the command:

```sh
CRC.py <path> <polynom>
```
For example: 

![](pic/wn_int.jpg)

# With using integrated polynomials

To find out which polynomials are embedded in the program, use the *--pol* command:

```sh
CRC.py --pol
```

![](pic/--pol.jpg)

Now you just need to select a polynomial and use it in the next command, where *--choice* is the flag indicating the choice of the polynomial:

```sh
CRC.py --choice <path> <choice_polynom>
```
For example:

![](pic/--choice.jpg)

#

## Authors

* **Oleg Mihalichev** - [GitHub](https://github.com/pettyderf)

## License

This project is licensed under the GNU ver.3 License.
