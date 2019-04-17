# Questions

## What's `stdint.h`?

`stdint.h` is a header file which allows us to declare fixed-width integer types which will remain the same
in all system environments.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

If we want to port our software, it is not wise to use primitive data types such as, int, float, double etc as the size of them
vary in each environments. For example, int won't be 4 bytes in all environments, but if we declare int32_t,
it will take 32 bits in all environments.


## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1, 4, 4, 2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be?
## Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

BM

## What's the difference between `bfSize` and `biSize`?

`bfsize` is the size of the bitmap file in bytes and `bisize` is the number of bytes required by the BITMAPINFOHEADER structure.

## What does it mean if `biHeight` is negative?

If `biHeight` is negative then it is a top-down image and it's center of origin is at upper-left.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

1. The file doesn't exist
2. The file is opened in a mode that doesn't allow other accesses
3. The network is down
4. The file exists, but you don't have permissions
5. A file exists with the name you gave, but the current directory of the process is not what you expected so the relative pathname fails to find and open the file.

## Why is the third argument to `fread` always `1` in our code?

`1` is the quantity of variables of BITMAPINFOHEADER data type.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

It moves the file pointer to a specific position.

## What is `SEEK_CUR`?

It provides current file pointer location.

## Whodunit?

It was Professor Plum with the candlestick in the library.
