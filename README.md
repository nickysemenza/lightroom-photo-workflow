# photo-workflow
Used to streamline my photo editing workflow.

1. While shooting, I press the protect button on my Nikon camera, which essentially adds a lock to the file at the filesystem level.
2. Because lightroom cannot read these, my script updates the EXIF metadata for every locked file, so that lighroom can now show me which are my selects, without me needing to manually do this via photomechanic.
3. Also, this script copies from the SD card into my lightroom directory, which can be slow for 30Mb RAW photos. Because of this, I prioritize the copying of the 'selects' first.


