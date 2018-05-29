# sf30ac-extractor
Extract assets from Street Fighter 30th Anniversary Collection (music, roms, artwork, fonts...)

## Requirements
You need to have a python 3 available somewhere

## Usage
Download the project.

Open a command line and execute the following command.

```
python extract.py "C:\.....\Street Fighter 30th Anniversary Collection\Bundle" "C:\...your extraction folder..."
```

The arguments are 1) the original bundle folder (in your steam directory) 2) the folder where you want stuff to be extracted to.

## Dependency
`bplist.py` was stolen by the project [bplist-python](https://github.com/farcaller/bplist-python) with a few alterations to make this work.
