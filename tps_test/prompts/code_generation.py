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
        return f"""Complete the following Python function. Only output the function implementation, no explanations.

{problem.prompt}"""
    
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