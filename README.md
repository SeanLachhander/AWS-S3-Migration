# NFS to AWS S3 Migration using AWS DataSync

This Python script enables migration of files from an on-premises NFS (Network File System) to AWS S3 using AWS DataSync. It utilizes the `boto3` library for AWS interactions and includes tests using `unittest`.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed
- AWS account credentials with sufficient permissions for DataSync and S3
- `boto3` library installed (`pip install boto3`)

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/SeanLachhander/AWS-S3-Migration.git
    cd AWS-S3-Migration
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Replace placeholder values in the script:

    - Update the `NFSMigrationAWS` class with your AWS resource ARNs and credentials.
    - Update the `test_create_datasync_task` and `test_start_datasync_task` methods in the test script with appropriate test cases.

## Usage

Run the unit tests to verify the functionality:

```bash
python your_test_script.py
