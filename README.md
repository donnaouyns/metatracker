# MetaTracker

MetaTracker is a Python program designed to schedule sleep and wake times for your Windows system to conserve energy and enhance system longevity. By monitoring system idle time and predefined sleep/wake schedules, MetaTracker ensures that your device is only awake when needed.

## Features

- **Automated Sleep Schedule**: Automatically puts the system to sleep during specified hours if the system is idle.
- **Energy Conservation**: Helps in reducing energy consumption by minimizing unnecessary system uptime.
- **System Longevity**: Reduces wear and tear by ensuring the system is not running when not in use.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository or download the `metatracker.py` file.

## Usage

1. Open the `metatracker.py` file in a text editor.
2. Customize the `sleep_hour`, `sleep_minute`, `wake_hour`, and `wake_minute` variables if needed. The default schedule is set to sleep at 23:00 and wake up at 07:00.
3. Run the script using the command: `python metatracker.py`.

## Important Notes

- This program uses the Windows command `shutdown /h` to hibernate the system. Ensure that hibernation is enabled on your Windows machine.
- The program checks for system idleness every 60 seconds. You can adjust this interval if needed.
- Make sure to run this script with appropriate permissions to execute system commands.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.