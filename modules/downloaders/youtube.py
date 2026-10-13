from os import path, makedirs

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from modules.config import DURATION_LIMIT
from modules.helpers.errors import DurationLimitError


DOWNLOAD_DIR = "downloads"
makedirs(DOWNLOAD_DIR, exist_ok=True)

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
    "noplaylist": True,
    "retries": 2,
    "fragment_retries": 2,
    "quiet": False,
    "no_warnings": False,
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    try:
        # ആദ്യം video വിവരങ്ങൾ പരിശോധിക്കുന്നു
        info = ydl.extract_info(url, download=False)

        if not info:
            raise DownloadError("YouTube returned no video information.")

        duration_seconds = info.get("duration")

        if duration_seconds is not None:
            duration = round(duration_seconds / 60)

            if duration > DURATION_LIMIT:
                raise DurationLimitError(
                    f"🛑 Videos longer than {DURATION_LIMIT} "
                    f"minute(s) aren't allowed. "
                    f"This video is {duration} minute(s)."
                )

        # Audio download ചെയ്യുന്നു
        ydl.download([url])

        file_path = path.join(
            DOWNLOAD_DIR,
            f"{info['id']}.{info['ext']}",
        )

        if not path.exists(file_path):
            raise DownloadError(
                f"Downloaded file not found: {file_path}"
            )

        return file_path

    except DurationLimitError:
        raise

    except Exception as e:
        print(f"YouTube download failed: {type(e).__name__}: {e}")
        raise
