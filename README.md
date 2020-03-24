# clipatron

**This is a script for creating clips from a video file.**
You create a spreadsheet that describes the clips you want to create, and then the script calls [`ffmpeg`](https://ffmpeg.org/) to create the clips.

This is an example spreadsheet:

<table>
  <tr><th>filename</th><th>start_time</th><th>duration</th><th>notes</th></tr>
  <tr><td>intro.mp4</td><td>00:00</td><td>00:03</td><td>animated "DLR 30"</td></tr>
  <tr><td>social_media.mp4</td><td>00:35.5</td><td>00:11</td><td>social media information</td></tr>
</table>

Combined with a video file, this would create two clips (`intro.mp4` and `social_media.mp4`).

This is deliberately a simple script.
If you need more complex options, you might be better off invoking ffmpeg directly, or looking at script like <https://github.com/c0decracker/video-splitter>

Original design and idea are from [@bessyboo](https://twitter.com/bessyboo)



## Installation

You need two programs installed and in your PATH:

-   ffmpeg; see the [ffmpeg installation guide](https://www.ffmpeg.org/download.html).
-   Python; which you can download [from python.org](https://www.python.org/downloads/).
    Any recent version of Python should be fine (2.7 or 3.x).

Then download this repository (click *"Clone or download"* > *"Download ZIP"*).
Unzip the repository.



## Usage

1.  Create a spreadsheet that describes the clips you want to create; one row per clip.
    This needs to have at least three named columns:

    *   `filename` -- the name of the file you want to create for this clip
    *   `start_time` -- where in the file the clip starts
    *   `duration` -- how long the clip lasts

    You can add other columns if it's helpful (e.g. a `notes` column describing what's in the clip), but the script will ignore them.

    Save this spreadsheet as a CSV.

2.  Open a terminal window, and navigate to the repository.

    ```console
    $ cd /path/to/repository
    ```

3.  Run the script, passing (1) the path to the video file you want to clip and (2) the path to the CSV you created in step 1.

    The repository includes an example:

    ```console
    $ python clipatron.py --manifest manifest.csv --input dlr_turns_30.mp4
    ✨ Clipping done! ✨
    ```



## Example

So you can see what the script expects, this repository includes an example [`manifest.csv`](manifest.csv) and video file.

(This is a video from the [Transport for London YouTube channel](https://www.youtube.com/watch?v=6BoDePDGBHs).)



## Getting help

If you get stuck, you can ask me for help [on Twitter](https://twitter.com/alexwlchan).




## License

MIT.
