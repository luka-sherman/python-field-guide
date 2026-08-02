import os


def on_files(files, config):
    file = files.get_file_from_path("thanks.md")
    if file is not None:
        file.dest_path = "thanks.html"
        file.abs_dest_path = os.path.join(config["site_dir"], "thanks.html")
        file.url = "thanks.html"
    return files
