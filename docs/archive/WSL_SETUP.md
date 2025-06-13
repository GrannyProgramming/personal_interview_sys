# WSL Remote + Conda Auto-Activation

Simple setup for WSL2 with VS Code Remote that automatically activates conda environments.

## Install

### 1. WSL2 + Ubuntu
```powershell
wsl --install -d Ubuntu-22.04
```

### 2. Miniforge
```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh -b -p $HOME/miniforge3
$HOME/miniforge3/bin/conda init bash
source ~/.bashrc
```

### 3. Create Environment
```bash
conda create -n my_project python=3.11 -y
conda activate my_project
```

## Configure VS Code

### 1. Install Extensions
- **Remote - WSL**
- **Python**

### 2. Project Settings
Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "/home/USERNAME/miniforge3/envs/my_project/bin/python",
    "python.terminal.activateEnvironment": true,
    "terminal.integrated.shellArgs.linux": ["-l"],
    "terminal.integrated.env.linux": {
        "CONDA_DEFAULT_ENV": "my_project"
    }
}
```

Replace `USERNAME` and `my_project` with your values.

## Auto-Activation Options

### Option A: VS Code Only (Easiest)
The settings above auto-activate in VS Code terminals. Done!

### Option B: Directory-Based
Add to `~/.bashrc`:

```bash
function cd_with_conda() {
    builtin cd "$@"
    if [[ -f ".vscode/settings.json" ]]; then
        ENV_NAME=$(grep -o '"CONDA_DEFAULT_ENV":\s*"[^"]*"' .vscode/settings.json | cut -d'"' -f4)
        if [[ -n "$ENV_NAME" ]] && [[ "$CONDA_DEFAULT_ENV" != "$ENV_NAME" ]]; then
            conda activate "$ENV_NAME"
        fi
    fi
}
alias cd='cd_with_conda'
```

## Test
```bash
cd /path/to/project
code .  # Should auto-connect to WSL and activate environment
```

## Troubleshooting

**Environment not activating?**
- Check interpreter path in VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter"
- Restart VS Code after changing settings

**Conda not found?**
```bash
export PATH="$HOME/miniforge3/bin:$PATH"
source ~/.bashrc
```

Done! 🎉
