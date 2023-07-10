# sensAI
Recursive Self Training Transformer (RSTT)

As opposed to a _generative pre-trained transformer_ like the traditional GPTs, an RSTT recursively trains itself, and recursively improves its response until the best possible result is achieved: perfection, in the form of error-free response, _continuosly improving_.

In this POC, a chained solution is presented between GPT, GitHub, and Selenium.

## Features

[*] Generate code using GPT models based on a prompt
[*] Create necessary files with correct names and write generated code to them
[*] Deploy generated code to a server using automatically, using Git actions
[ ] Run the implementation with a Selenium instance
[ ] Perform visual inspections using computer vision
[ ] Inspect debug logs for troubleshooting
[ ] Loop until the desired implementation is complete and working
[ ] Finetune GPT Model with eventual optimizations extracted from the previous processes, to be used in the next loop

## Requirements

To use this tool, you need to have the following dependencies installed:

- Python 3.6+
- Git
- Selenium
- OpenCV (for computer vision)
- Any necessary web driver for Selenium (e.g., ChromeDriver)

You also need your own GitHub Repository with an action defined to deploy to your remote server. This involves as well creating the appropriate SSH keys, GitHub Action Secrets, and other repository variables.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dodelidoo-Labs/sensai.git
   ```

2. Change into the app directory:

   ```bash
   cd sensai
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Download and configure the necessary web driver for Selenium. Please refer to the official Selenium documentation for specific instructions on setting up the web driver for your preferred browser.

## Usage

0. Edit the variables in the `sensai/app/.env` file adequately

1. Run the app:

   ```bash
   python sensai/app/main.py
   ```

2. Provide a description of your goal when prompted, hit enter.
   

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL3 License. See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) file for more details.

## Acknowledgments

- This tool utilizes the power of GPT models, Selenium, and computer vision libraries to simplify and expedite the code generation and deployment process.
- We would like to thank the open-source community for their invaluable contributions.

## Contact

For any questions or inquiries, please contact [beda@tukutoi.com](mailto:beda@tukutoi.com).