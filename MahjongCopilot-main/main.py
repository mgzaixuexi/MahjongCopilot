

from gui.main_gui import MainGUI
from common import utils
from common.log_helper import LogHelper
from common.settings import Settings
from bot_manager import BotManager


def main():
    """ Main entry point """
    LogHelper.config_logging()
    setting = Settings()
    # utils.set_dpi_awareness()
    utils.prevent_sleep()
    bot_manager = BotManager(setting)
    gui = MainGUI(setting, bot_manager)
    gui.mainloop()

if __name__ == "__main__":
    main()
