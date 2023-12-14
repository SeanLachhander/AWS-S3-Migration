# NFS to AWS S3 Migration using AWS DataSync

This Python script automates the migration of files from an on-premises NFS (Network File System) to AWS S3 utilizing AWS DataSync. The script employs the `boto3` library for AWS interactions and includes comprehensive unit tests using `unittest`.

## Purpose

The purpose of this script is to simplify and automate the process of migrating files stored on an on-premises NFS to an AWS S3 bucket. By leveraging AWS DataSync, the migration ensures reliable, efficient, and secure transfer of data to the cloud.

## Prerequisites

Before using this script, ensure you have the following:

- **Python 3.x**: Installed on your system.
- **AWS Account**: Access with sufficient permissions for DataSync and S3.
- **boto3 Library**: Installed (`pip install boto3`).

## Setup

1. **Clone the Repository**:

    ```bash
    git clone git clone https://github.com/SeanLachhander/AWS-S3-Migration.git
    cd your-repo
    ```

2. **Install Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configuration**:

    - **AWS Credentials**: Update the `NFSMigrationAWS` class with your AWS resource ARNs and credentials.
    - **Tests**: Update the `test_create_datasync_task` and `test_start_datasync_task` methods in the test script with appropriate test cases.

## Usage

1. **Run Unit Tests**:

    ```bash
    python migration.py
    ```

2. **Run Unit Tests then Start DataSync Migration**:

    - After successful tests, DataSync migration will automatically commence. Ensure your AWS credentials are properly configured.

## Project Structure

- `migration.py`: Contains the main code for NFS to S3 migration, also includes unit tests for the code.
- `README.md`: Documentation providing instructions and information.
- `requirements.txt`: File listing required Python packages.

## Contributions

Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or additional features.

## License

This project is licensed under the [MIT License](LICENSE).
