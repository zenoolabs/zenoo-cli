import click
import subprocess


@click.command()
@click.option("--option", default="login", help="Logging into ECR")
def ecr(option):
    """AWS ECR commands for Zenoo processes"""
    if option == "login":
        subprocess.run(
            "source ./config.sh && echo $(aws ecr get-login-password --region $REGION --profile $PROFILE_NAME) | docker login --username AWS --password-stdin $DOCKER_REPO",
            shell=True, executable="/bin/bash")
