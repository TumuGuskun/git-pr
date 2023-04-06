from __future__ import annotations
from dataclasses import dataclass, field
from subprocess import run, PIPE
import sys
from typing import Dict, List


@dataclass
class CommandResult:
    return_code: int
    text: str

    @property
    def passed(self) -> bool:
        return self.return_code == 0


@dataclass
class ShellCommand:
    shell_command: List[str]
    flags: List[str] = field(default_factory=list)
    kv_args: Dict[str, str] = field(default_factory=dict)
    command_args: List[str] = field(default_factory=list)
    env: Dict[str, str] = field(default_factory=dict)
    input_command: ShellCommand | None = None

    def add_flag(self, flag: str) -> None:
        self.flags.append(flag)

    def add_flags(self, flags: list[str]) -> None:
        self.flags.extend(flags)

    def add_key_value_arg(self, key: str, value: str) -> None:
        self.kv_args[key] = value

    def add_key_value_args(self, kv_args: dict) -> None:
        self.kv_args.update(kv_args)

    def add_command_args(self, *args: str) -> None:
        self.command_args.extend(args)

    def add_env(self, key: str, value: str) -> None:
        self.env[key] = value

    def add_input(self, input_command: ShellCommand) -> None:
        self.input_command = input_command

    @property
    def command(self) -> List[str]:
        command = []
        if self.env:
            command.append("env")
            command.extend([f"{key}={value}" for key, value in self.env.items()])
        command.extend(self.shell_command)
        command.extend(self.flags)
        command.extend([f"{key}={value}" for key, value in self.kv_args.items()])
        command.extend(self.command_args)
        return command

    def run(self, check: bool = True) -> CommandResult:
        command_input = None
        if self.input_command:
            command_input = self.input_command.run(check=check).text

        subprocess_result = run(
            self.command, stdout=PIPE, text=True, input=command_input
        )
        if check and subprocess_result.returncode != 0:
            sys.exit(subprocess_result.returncode)

        return CommandResult(
            return_code=subprocess_result.returncode,
            text=subprocess_result.stdout.strip(),
        )
