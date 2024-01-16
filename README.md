# Tailwind CSS Color Palette

This repository contains an Adobe Swatch Exchange (`.ase`) color palette for [Tailwind CSS](https://tailwindcss.com/) colors
to be used in Adobe and Affinity applications.
Other programs might also support `.ase` files.
This can be particularly useful for designers and developers who are creating mockups and need to use Tailwind's color palette.

You can find the generator script in the `src` folder.
It will generate a new `.ase` file based on the colors defined in `src/colors.json`.

## Usage
[Download](https://github.com/probstal/tailwindcss-colors-ase/releases/download/v3.4.1/Tailwindcss.ase) the `.ase` file
and import it into your application of choice.

You can find all versions on the [releases page](https://github.com/probstal/tailwindcss-colors-ase/releases).

### Generate a new file
You might want to generate a new `.ase` file after updating `src/colors.json`.

```bash
python src/main.py
```

## Background Information
The colors are taken from the [Taildwind CSS Repository](https://github.com/tailwindlabs/tailwindcss/blob/v3.4.1/src/public/colors.js).

You can find a documentation for the `.ase` file format [here](http://www.selapa.net/swatches/colors/fileformats.php#adobe_ase).
