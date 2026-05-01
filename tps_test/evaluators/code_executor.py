"""
代码执行器 - 用于验证生成的代码是否正确
"""
import subprocess
import tempfile
import os
import re
from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class ExecutionResult:
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0


def extract_code_from_markdown(code: str) -> str:
    lines = code.strip().split('\n')
    
    if lines and lines[0].strip().startswith('```'):
        lines = lines[1:]
    
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1]
    
    return '\n'.join(lines)


class CodeExecutor:
    @staticmethod
    def execute_python(code: str, timeout: int = 10) -> ExecutionResult:
        import time
        start_time = time.time()
        
        code = extract_code_from_markdown(code)
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name
            
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8'
            )
            
            execution_time = time.time() - start_time
            
            os.unlink(temp_file)
            
            if result.returncode == 0:
                return ExecutionResult(
                    success=True,
                    output=result.stdout,
                    execution_time=execution_time
                )
            else:
                return ExecutionResult(
                    success=False,
                    output=result.stdout,
                    error=result.stderr,
                    execution_time=execution_time
                )
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                success=False,
                output="",
                error=f"Execution timed out after {timeout} seconds",
                execution_time=timeout
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                output="",
                error=str(e),
                execution_time=time.time() - start_time
            )
    
    @staticmethod
    def execute_cpp(code: str, timeout: int = 10) -> ExecutionResult:
        import time
        start_time = time.time()
        
        code = extract_code_from_markdown(code)
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_cpp = f.name
            
            temp_exe = temp_cpp.replace('.cpp', '.exe' if os.name == 'nt' else '.out')
            
            compile_result = subprocess.run(
                ['g++', '-std=c++17', temp_cpp, '-o', temp_exe],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            if compile_result.returncode != 0:
                return ExecutionResult(
                    success=False,
                    output="",
                    error=f"Compilation failed: {compile_result.stderr}",
                    execution_time=time.time() - start_time
                )
            
            result = subprocess.run(
                [temp_exe],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            execution_time = time.time() - start_time
            
            os.unlink(temp_cpp)
            if os.path.exists(temp_exe):
                os.unlink(temp_exe)
            
            if result.returncode == 0:
                return ExecutionResult(
                    success=True,
                    output=result.stdout,
                    execution_time=execution_time
                )
            else:
                return ExecutionResult(
                    success=False,
                    output=result.stdout,
                    error=result.stderr,
                    execution_time=execution_time
                )
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                success=False,
                output="",
                error=f"Execution timed out after {timeout} seconds",
                execution_time=timeout
            )
        except FileNotFoundError:
            return ExecutionResult(
                success=False,
                output="",
                error="g++ compiler not found. Please install g++ to run C++ code.",
                execution_time=time.time() - start_time
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                output="",
                error=str(e),
                execution_time=time.time() - start_time
            )
    
    @staticmethod
    def execute(code: str, language: str = "python", timeout: int = 10) -> ExecutionResult:
        if language in ["python", "py"]:
            return CodeExecutor.execute_python(code, timeout)
        elif language in ["cpp", "c++"]:
            return CodeExecutor.execute_cpp(code, timeout)
        else:
            return ExecutionResult(
                success=False,
                output="",
                error=f"Unsupported language: {language}"
            )