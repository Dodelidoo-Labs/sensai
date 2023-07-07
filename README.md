# sensAI
Recursive Self Training Transformer (RSTT)

As opposed to a _generative pre-trained transformer_ like the traditional GPTs, a RSTT recursively trains itself, and recursively improves its response until the best possible result is achieved: perfection, in the form of error-free response, _continuosly improving_

## Features

- Generate code using GPT models
- Deploy generated code to a server using automated Git actions
- Run the implementation with a Selenium instance
- Perform visual inspections using computer vision
- Inspect debug logs for troubleshooting
- Continuously improve code quality by providing feedback to the GPT model for corrections
- Loop until the desired implementation is complete and working

## Requirements

To use this tool, you need to have the following dependencies installed:

- Python 3.6+
- Git
- Selenium
- OpenCV (for computer vision)
- Any necessary web driver for Selenium (e.g., ChromeDriver)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Change into the project directory:

   ```bash
   cd your-repo
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Download and configure the necessary web driver for Selenium. Please refer to the official Selenium documentation for specific instructions on setting up the web driver for your preferred browser.

## Usage

1. Prepare the GPT model:

   - Ensure you have a trained GPT model available or use a pre-trained GPT model.
   - Place the GPT model in the appropriate directory within the project structure.

2. Configure the tool:

   - Open the `config.yaml` file and update the necessary parameters according to your requirements.

3. Run the tool:

   ```bash
   python generate_and_deploy.py
   ```

   This command will initiate the code generation process, deployment to the server, execution, visual inspection, and debugging capabilities.

4. Iterate and improve:

   - Review the generated code, inspect the visual results, and analyze the debug logs.
   - If any issues are found, provide feedback to the GPT model for correction and repeat the execution process.

   Repeat this loop until the desired implementation is complete and working as expected.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL3 License. See the [LICENSE]() file for more details.

## Acknowledgments

- This tool utilizes the power of GPT models, Selenium, and computer vision libraries to simplify and expedite the code generation and deployment process.
- We would like to thank the open-source community for their invaluable contributions.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).