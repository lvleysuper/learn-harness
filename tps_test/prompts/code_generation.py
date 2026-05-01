"""
代码生成提示词模板
"""
from typing import Optional
from tps_test.benchmarks.base_benchmark import Problem


class CodeGenerationPrompt:
    @staticmethod
    def create_prompt(problem: Problem, language: Optional[str] = None) -> str:
        lang = language or problem.language
        
        if lang == "python":
            return CodeGenerationPrompt._python_prompt(problem)
        elif lang in ["cpp", "c++"]:
            return CodeGenerationPrompt._cpp_prompt(problem)
        elif lang in ["javascript", "typescript"]:
            return CodeGenerationPrompt._js_prompt(problem)
        elif lang == "java":
            return CodeGenerationPrompt._java_prompt(problem)
        else:
            return CodeGenerationPrompt._generic_prompt(problem)
    
    @staticmethod
    def _python_prompt(problem: Problem) -> str:
        return f"""Write the complete Python function implementation for the following problem.

Requirements:
1. Output ONLY Python code (no markdown ``` blocks, no explanations)
2. Include necessary imports if needed
3. Write the complete function with proper indentation
4. Make sure the code passes the given doctests

{problem.prompt}

Complete function code (no markdown, no text outside code):"""
    
    @staticmethod
    def _cpp_prompt(problem: Problem) -> str:
        return f"""Complete the following C++ function. Only output the function implementation, no explanations.

{problem.prompt}"""
    
    @staticmethod
    def _js_prompt(problem: Problem) -> str:
        return f"""Complete the following JavaScript function. Only output the function implementation, no explanations.

{problem.prompt}"""
    
    @staticmethod
    def _java_prompt(problem: Problem) -> str:
        return f"""Complete the following Java method. Only output the method implementation, no explanations.

{problem.prompt}"""
    
    @staticmethod
    def _generic_prompt(problem: Problem) -> str:
        return f"""Complete the following code. Only output the implementation, no explanations.

{problem.prompt}"""