import click
from src.commands import ecr, ecs, service

@click.group()
def cli():
    pass

cli.add_command(ecr.ecr)
cli.add_command(ecs.ecs)
cli.add_command(service.service)

if __name__ == "__main__":
    cli()


# @click.command()
# @click.option("--option", default="login", help="Logging into ECR")
# def ecr(option):
#     """AWS ECR commands for Zenoo processes"""
#     if option == "login":
#         subprocess.run(
#             "source ./config.sh && echo $(aws ecr get-login-password --region $REGION --profile $PROFILE_NAME) | docker login --username AWS --password-stdin $DOCKER_REPO", shell=True, executable="/bin/bash")


# @click.command()
# @click.option("--option", help="ECS CLI configuration")
# def ecs(option):
#     """AWS ECS commands for Zenoo processes"""
#     match option:
#         case "configure":
#             subprocess.run("source ./config.sh && ecs-cli configure --cluster $CLUSTER --default-launch-type $LAUNCH_TYPE --config-name $CONFIG_NAME --region $REGION", shell=True, executable="/bin/bash")
#             subprocess.run("source ./config.sh && ecs-cli configure profile --access-key $ACCESS_KEY --secret-key $SECRET_KEY --profile-name $PROFILE_NAME", shell=True, executable="/bin/bash")
#         case "enable-execute-command":
#             subprocess.run("source ./config.sh && aws ecs update-service --cluster $CLUSTER --service $PROJECT_NAME --region $REGION --enable-execute-command --force-new-deployment", shell=True, executable="/bin/bash")


# @click.command()
# @click.option("--option", help="ECS CLI configuration")
# def service(option):
#     """AWS ECS-CLI commands for Zenoo processes"""
#     main_command = "source ./config.sh && ecs-cli compose --project-name $PROJECT_NAME service %s --cluster-config $CONFIG_NAME --ecs-profile $PROFILE_NAME"
#     subprocess.run(main_command % option, shell=True, executable="/bin/bash")


# cli.add_command(ecr)
# cli.add_command(ecs)
# cli.add_command(service)

# if __name__ == "__main__":
#     cli()
