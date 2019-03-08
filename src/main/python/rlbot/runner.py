from rlbot.setup_manager import SetupManager
from rlbot.utils.python_version_check import check_python_version

import multiprocessing as mp


def main(gym=False):
    print(f"Starting Custom runner with gym:{gym}")
    check_python_version()
    manager = SetupManager(gym)
    manager.connect_to_game()
    manager.load_config()
    manager.launch_ball_prediction()
    manager.launch_quick_chat_manager()
    manager.launch_bot_processes()
    manager.start_match()
    return manager

if __name__ == '__main__':
    main()
