# virtual-sheet-magic

## Features


## Installation

Set up **virtual-sheet-magic** in a `virtualenv` - this way, you will not pollute your system-wide install.  
*(If you know how to package Python projects, feel free to fork & submit a pull request.)*

```sh
$ python -m virtualenv .venv && source .venv/bin/activate && pip install -r requirements.txt

# install development packages (preferably in virtualenv as well)
$ pip install -r requirements-dev.txt
```

### `keyboard` versus `pynput`

At the time of writing, `pynput` on Windows sends simulated keypresses which may not work with all applications.  
However, on Linux, `keyboard` requires root access, which is rather inconvenient and a potential security risk.

By default, the program uses `pynput` as it should work for most scenarios. If you're on Windows and an application
is not receiving keystrokes, try using `--input-wrapper keyboard` when you play a sheet.

## Usage

```
positional arguments:
  {play,p,parse}
    play (p)      Plays a virtual sheet from `stdin`. Outputs seeker value on exit to `stdout`

options:
  -h, --help      show this help message and exit
```

### play

```
play [-h] [--input-wrapper INPUT_WRAPPER] [--seek SEEK] [--tempo TEMPO] [--newline-pauses]

options:
  -h, --help            show this help message and exit
  --input-wrapper INPUT_WRAPPER, -w INPUT_WRAPPER

                        Use an input wrapper preferable to your system configuration
                        	pynput - preferable on X11, macOS
                        	keyboard - preferable on Microsoft Windows
  --seek SEEK, -s SEEK  Start the player at the provided number (measured in notes)
  --tempo TEMPO, -t TEMPO

                        Overrides the tempo of the sheet being played.
                        If not provided, uses the sheet's tempo or default (120)
  --newline-pauses, -N  Toggle whether a newline should count as a `|` (pause) note
```

## Example usage

Browse around [Virtual Piano's collection of sheets](https://virtualpiano.net/music-sheets/) and copy/save into a file to try it out.

```
$ python main.py play -t 110 < my-vp-sheet.txt
$ sleep 1; python main.py play -t 110 < my-vp-sheet.txt
$ xclip -i -sel c | python main.py play -t 160
$ sleep 1; xclip -i -sel c | python main.py play -s echo $([ -f asf ] && cat /tmp/seeker-stopped-at || echo 0) -t 160 > /tmp/seeker-stopped-at
```
