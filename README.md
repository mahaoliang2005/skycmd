# skycmd - 天气查询工具

一个简单的命令行天气工具，可以获取指定城市的天气信息。

## 功能

- 获取指定城市的当前天气信息
- 显示简要或详细的天气信息

## 使用方法

基本用法：

```bash
uv run skycmd <城市名>
```

显示详细天气信息：
```bash
uv run skycmd <城市名>
```

## 构建发行包

```
uv build
```

## 安装本地工具

将构建的发现包，作为工具安装到用户目录：

```bash
uv tool install dist/skycmd-0.1.0-py3-none-any.whl
```

安装后就可以就可以在命令行直接使用 skycmd 查询天气信息了：

```bash
skycmd Shenzhen
skycmd -v Shenzhen
```