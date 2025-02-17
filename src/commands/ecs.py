import click
import subprocess


@click.command()
@click.option("--option", help="ECS CLI configuration")
def ecs(option):
    """AWS ECS commands for Zenoo processes"""
    match option:
        case "configure":
            subprocess.run(
                "source ./config.sh && ecs-cli configure --cluster $CLUSTER --default-launch-type $LAUNCH_TYPE --config-name $CONFIG_NAME --region $REGION",
                shell=True, executable="/bin/bash")
            subprocess.run(
                "source ./config.sh && ecs-cli configure profile --access-key $ACCESS_KEY --secret-key $SECRET_KEY --profile-name $PROFILE_NAME",
                shell=True, executable="/bin/bash")
        case "enable-execute-command":
            subprocess.run(
                "source ./config.sh && aws ecs update-service --cluster $CLUSTER --service $PROJECT_NAME --region $REGION --enable-execute-command --force-new-deployment",
                shell=True, executable="/bin/bash")
