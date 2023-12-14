import boto3
from botocore.exceptions import ClientError
import unittest
from unittest.mock import patch

class NFSMigrationAWS:
    """
    A class to migrate files from an on-premises NFS (Network File System) to AWS S3 using AWS DataSync.

    Attributes:
    - nfs_path (str): The local path of the NFS directory.
    - s3_bucket_name (str): The name of the AWS S3 bucket.
    - aws_access_key (str): The AWS access key.
    - aws_secret_key (str): The AWS secret access key.
    """

    def __init__(self, nfs_path, s3_bucket_name, aws_access_key, aws_secret_key):
        """
        Initialize the NFSMigrationAWS instance.

        Args:
        - nfs_path (str): The local path of the NFS directory.
        - s3_bucket_name (str): The name of the AWS S3 bucket.
        - aws_access_key (str): The AWS access key.
        - aws_secret_key (str): The AWS secret access key.
        """
        self.nfs_path = nfs_path
        self.s3_bucket_name = s3_bucket_name
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key

        try:
            self.datasync_client = boto3.client('datasync', aws_access_key_id=self.aws_access_key, aws_secret_access_key=self.aws_secret_key)
        except ClientError as e:
            print(f"Failed to create DataSync client: {str(e)}")
            self.datasync_client = None

    def create_datasync_task(self):
        """
        Create an AWS DataSync task for the NFS to S3 migration.

        Returns:
        - str: The DataSync task ARN (Amazon Resource Name).
        """
        if not self.datasync_client:
            return None

        try:
            response = self.datasync_client.create_task(
                SourceLocationArn='YourNFSLocationArn',
                DestinationLocationArn='YourS3LocationArn',
                CloudWatchLogGroupArn='YourCloudWatchLogGroupArn',
                Name='NFS-to-S3-Migration-Task'
            )
            return response['TaskArn']
        except ClientError as e:
            print(f"Failed to create DataSync task: {str(e)}")
            return None

    def start_datasync_task(self, task_arn):
        """
        Start the AWS DataSync task for migration.

        Args:
        - task_arn (str): The DataSync task ARN (Amazon Resource Name).

        Returns:
        - None
        """
        if not self.datasync_client:
            return

        try:
            self.datasync_client.start_task_execution(
                TaskArn=task_arn
            )
            print(f"DataSync task {task_arn} started.")
        except ClientError as e:
            print(f"Failed to start DataSync task: {str(e)}")

# Unit Tests
class TestNFSMigrationAWS(unittest.TestCase):
    """
    Test suite for NFSMigrationAWS class.
    """

    @patch('boto3.client')
    def test_create_datasync_task(self, mock_boto_client):
        """
        Test create_datasync_task method.
        """
        mock_datasync_client = mock_boto_client.return_value
        mock_datasync_client.create_task.return_value = {'TaskArn': 'mocked-task-arn'}

        migration = NFSMigrationAWS('nfs_path', 's3_bucket_name', 'aws_access_key', 'aws_secret_key')
        task_arn = migration.create_datasync_task()

        self.assertEqual(task_arn, 'mocked-task-arn')

    @patch('boto3.client')
    def test_start_datasync_task(self, mock_boto_client):
        """
        Test start_datasync_task method.
        """
        mock_datasync_client = mock_boto_client.return_value

        migration = NFSMigrationAWS('nfs_path', 's3_bucket_name', 'aws_access_key', 'aws_secret_key')
        migration.start_datasync_task('test-task-arn')

        mock_datasync_client.start_task_execution.assert_called_with(TaskArn='test-task-arn')

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestNFSMigrationAWS))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        # If all tests were successful, proceed with DataSync migration
        nfs_path = "/path/to/nfs/folder"
        s3_bucket_name = "your-s3-bucket-name"
        aws_access_key = "your-aws-access-key"
        aws_secret_key = "your-aws-secret-key"

        migration = NFSMigrationAWS(nfs_path, s3_bucket_name, aws_access_key, aws_secret_key)
        task_arn = migration.create_datasync_task()
        if task_arn:
            migration.start_datasync_task(task_arn)
