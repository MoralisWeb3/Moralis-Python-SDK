import subprocess
import sys
from pathlib import Path
from .paths import temp_generated_api_path, temp_swaggers_path


def execute(cmd: str):
    print(f"🤖 Executing {cmd}")

    out = subprocess.check_call(
        cmd, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)

    print(out)
    print(f"✅ Execution successful")


def run_openapi_generator(input_path: Path, output_path: Path, package_name: str, project_name: str):
    command_call = 'npx @openapitools/openapi-generator-cli generate'

    command_env = [
        # Fix for https://github.com/OpenAPITools/openapi-generator/issues/11763#issuecomment-1098337960
        '_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED"',
        # Make sure to select 'yes' on the npm question "do you want to install @openapitools/openapi-generator-cli"
        'npm_config_yes=true'
    ]

    command_arguments = {
        '--input-spec': input_path.as_posix(),
        '--generator-name': 'python',
        '--skip-validate-spec': '',
        '--output': output_path.as_posix(),
        '--additional-properties': f'packageName={package_name},projectName={project_name},generateSourceCodeOnly=true'
    }

    command_env_string = ' '.join(command_env)
    command_arguments_string = ' '.join(
        [f"{argument} {value}" for argument, value in command_arguments.items()])

    commmand = f'{command_env_string} {command_call} {command_arguments_string}'
    execute(commmand)


root_path = Path(__file__).parent.parent.parent


def generate_openapi(api_name: str):
    print(f"⏳ Generating openapi client for {api_name}...")
    input_path = temp_swaggers_path / f'{api_name}.json'
    output_path = temp_generated_api_path
    package_name = f'openapi_{api_name}'
    project_name = api_name

    run_openapi_generator(
        input_path=input_path,
        output_path=output_path,
        package_name=package_name,
        project_name=project_name
    )
    print(f"✅ Generatedopenapi client for {api_name}...")

    return package_name
