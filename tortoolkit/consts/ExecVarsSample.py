try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "8743fcb30d909f1ece760ebbd03c1bdd"
        API_ID = "2234188"
        BOT_TOKEN = "1734765687:AAHpz0y_lPs8OJ47gWxJfiM2j7_m6CmJAow"
        BASE_URL_OF_BOT = "https://gautamleecherbot.herokuapp.com/"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [820569976,-1001428771862]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 40

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1700000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DB_URI = "postgres://abdzbgwltfziwy:016aea57b883362ef1305b5d340f2ea83dcdf4e958e71f5cedbb020a72b5d81f@ec2-54-157-234-29.compute-1.amazonaws.com:5432/d8j8aptt91frmi"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/Bot Uploads/Leech Bot"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = True

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = True
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = "leech"

        # Max size of the videos in playlist allowed
        MAX_YTPLAYLIST_SIZE = 200
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 30

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





