# TPS 测试工具

模块化的 AI 代码生成性能测试工具，用于测量编码场景下的真实 TPS (Tokens Per Second)。

## 特性

- **模块化设计**: 各组件独立，易于扩展
- **HumanEval基准测试**: 使用业界标准编程测试集
- **多语言支持**: Python、C++、JavaScript、Java
- **代码执行验证**: 自动运行测试用例验证生成代码
- **并发测试**: 支持可配置的并发请求
- **详细报告**: 控制台输出详细的性能统计

## 项目结构

```
tps_test/
├── __init__.py           # 包初始化
├── config.py             # 配置管理
├── main.py               # 主入口
├── clients/              # API客户端
│   ├── base_client.py    # 客户端基类
│   └── openai_client.py  # OpenAI兼容客户端
├── benchmarks/           # 基准测试
│   ├── base_benchmark.py # 基准测试基类
│   └── humaneval.py      # HumanEval测试集
├── prompts/              # 提示词模板
│   └── code_generation.py
├── evaluators/           # 代码执行器
│   └── code_executor.py
├── reporters/            # 报告生成
│   └── console_reporter.py
└── utils/                # 工具
    └── stats.py          # 统计计算
```

## 安装依赖

```bash
cd tps_test
pip install -r requirements.txt
```

## 配置

在项目根目录创建 `.env` 文件：

```
API_KEY=your-api-key
API_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
MODEL=glm-5
```

**注意**: `.env` 文件不会提交到 Git 仓库。

## 使用方法

### 基本用法

```bash
cd tps_test

# 运行完整测试 (默认10个问题，并发数2)
python main.py

# 指定问题数量和并发数
python main.py --num-problems 20 --concurrency 4

# 指定模型
python main.py --model glm-5

# 指定API基础URL
python main.py --api-base-url https://api.openai.com/v1

# 简化版测试（快速验证API连通性）
python simple_test.py 5 2  # 5个请求，并发数2
```

### 命令行参数

| 参数 | 短参数 | 默认值 | 说明 |
|------|--------|--------|------|
| `--num-problems` | `-n` | 10 | 测试问题数量 |
| `--concurrency` | `-c` | 2 | 并发请求数 |
| `--model` | `-m` | glm-5 | 模型名称 |
| `--api-key` | `-k` | - | API密钥 |
| `--api-base-url` | `-u` | - | API基础URL |
| `--max-tokens` | - | 1024 | 最大生成Token数 |
| `--language` | `-l` | python | 编程语言 |
| `--skip-execution` | - | False | 跳过代码执行验证 |

### 环境变量

| 变量 | 说明 |
|------|------|
| `API_KEY` | API密钥 |
| `API_BASE_URL` | API基础URL |
| `MODEL` | 模型名称 |

## 输出示例

```
======================================================================
 TPS 测试报告 - 代码生成性能
======================================================================

总请求数: 10
成功请求: 10
失败请求: 0
测试通过率: 80.0%

----------------------------------------------------------------------
 Token 生成速度 (TPS)
----------------------------------------------------------------------
  平均 TPS:         45.3 tokens/秒
  中位数 TPS:       42.8 tokens/秒
  整体 TPS:         41.5 tokens/秒
  最小 TPS:         35.2 tokens/秒
  最大 TPS:         58.7 tokens/秒
  标准差:           7.2 tokens/秒

----------------------------------------------------------------------
 延迟统计
----------------------------------------------------------------------
  平均延迟:         12.34 秒
  最小延迟:         8.56 秒
  最大延迟:         18.92 秒

----------------------------------------------------------------------
 Token 统计
----------------------------------------------------------------------
  总生成 Token:       4150
  总耗时:            123.45 秒
```

## 扩展指南

### 添加新的基准测试

1. 在 `benchmarks/` 目录创建新文件
2. 继承 `BaseBenchmark` 类
3. 实现 `load()` 和 `get_test_code()` 方法

### 添加新的API客户端

1. 在 `clients/` 目录创建新文件
2. 继承 `BaseClient` 类
3. 实现 `generate()` 方法

### 添加新的报告格式

1. 在 `reporters/` 目录创建新文件
2. 实现报告生成逻辑

## 注意事项

- 运行 C++ 测试需要安装 g++ 编译器
- 代码执行有 10 秒超时限制
- 建议并发数不超过 5，避免 API 限流