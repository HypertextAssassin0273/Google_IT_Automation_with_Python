#!/usr/bin/env python3

from concurrent import futures
from tqdm import tqdm

import argparse, logging, os, sys, PIL.Image


def process_options():
    kwargs = {
        'format': '[%(levelname)s] %(message)s'
    }

    parser = argparse.ArgumentParser(
        description="Thumbnail generator",
        fromfile_prefix_chars='@'
    )
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    # parser.add_argument('-q', '--quiet', action='store_true')

    args = parser.parse_args()
    if args.debug:
        kwargs['level'] = logging.DEBUG
    elif args.verbose:
        kwargs['level'] = logging.INFO
    else:
        kwargs['level'] = logging.WARNING
    
    logging.basicConfig(**kwargs)


def process_file(root, basename):
    logging.info('Processing %s', basename)
    filename = os.path.join(root, basename)
    image = PIL.Image.open(filename)
    image.thumbnail((128, 128))
    thumbnail_name = os.path.join('thumbnails', 't-' + basename)
    image.save(thumbnail_name, 'JPEG')
    return thumbnail_name


def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)


def main():
    process_options() # process the command line options

    os.makedirs('thumbnails', exist_ok=True) # create the thumbnail directory

    executor = futures.ThreadPoolExecutor()
    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if basename.endswith('.jpg'):
                executor.submit(process_file, root, basename)

    print('Waiting for all threads to finish.')
    executor.shutdown()

    print('All threads are done.')
    return 0


if __name__ == "__main__":
    sys.exit(main())
