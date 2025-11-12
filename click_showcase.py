#!/usr/bin/env python3
"""
Click 库功能展示
展示 Python Click 库的强大命令行接口功能
"""

import click
import time
from datetime import datetime
from typing import List, Optional

@click.group()
def cli():
    """主命令组 - 优雅的命令行工具集"""
    pass

@cli.command()
@click.option('--name', '-n', default='World', help='打招呼的对象名称')
@click.option('--count', '-c', default=1, help='打招呼的次数')
@click.option('--shout', '-s', is_flag=True, help='是否大声打招呼')
def hello(name, count, shout):
    """简单的打招呼命令"""
    message = f"Hello, {name}!"
    if shout:
        message = message.upper()
    
    for i in range(count):
        click.echo(f"{i+1}. {message}")

@cli.command()
@click.argument('numbers', nargs=-1, type=int)
@click.option('--operation', '-op', type=click.Choice(['sum', 'avg', 'min', 'max']), 
              default='sum', help='计算操作类型')
def calculate(numbers, operation):
    """数学计算器 - 支持多种计算操作"""
    if not numbers:
        click.echo("请提供至少一个数字!")
        return
    
    if operation == 'sum':
        result = sum(numbers)
        click.echo(f"总和: {result}")
    elif operation == 'avg':
        result = sum(numbers) / len(numbers)
        click.echo(f"平均值: {result:.2f}")
    elif operation == 'min':
        result = min(numbers)
        click.echo(f"最小值: {result}")
    elif operation == 'max':
        result = max(numbers)
        click.echo(f"最大值: {result}")

@cli.command()
@click.option('--file', '-f', type=click.Path(exists=True), 
              help='文件路径', required=True)
@click.option('--output', '-o', type=click.Path(), 
              help='输出文件路径')
@click.option('--verbose', '-v', is_flag=True, 
              help='显示详细输出')
def file_processor(file, output, verbose):
    """文件处理器 - 演示文件操作和验证"""
    if verbose:
        click.echo(f"正在处理文件: {file}")
    
    # 模拟文件处理
    try:
        with open(file, 'r') as f:
            content = f.read()
        
        processed = content.upper()  # 简单的处理示例
        
        if output:
            with open(output, 'w') as f:
                f.write(processed)
            click.echo(f"处理完成! 结果已保存到: {output}")
        else:
            click.echo("处理结果:")
            click.echo(processed)
            
    except Exception as e:
        click.echo(f"处理文件时出错: {e}", err=True)

@cli.command()
@click.option('--username', prompt=True, 
              help='用户名')
@click.option('--password', prompt=True, hide_input=True, 
              confirmation_prompt=True, help='密码')
@click.option('--email', prompt=True, 
              help='邮箱地址')
def register(username, password, email):
    """用户注册 - 交互式输入演示"""
    # 简单的邮箱验证
    if '@' not in email:
        click.echo("错误: 邮箱地址格式不正确!")
        return
    
    # 模拟注册过程
    click.echo(f"\n注册信息:")
    click.echo(f"用户名: {username}")
    click.echo(f"邮箱: {email}")
    click.echo(f"密码: {'*' * len(password)}")
    
    if click.confirm('确认注册吗?'):
        click.echo("🎉 注册成功!")
        # 这里可以添加实际的注册逻辑
    else:
        click.echo("❌ 注册已取消")

@cli.command()
@click.option('--host', default='localhost', help='主机地址')
@click.option('--port', default=8080, help='端口号')
@click.option('--timeout', default=30, help='超时时间(秒)')
@click.option('--retries', default=3, help='重试次数')
def server(host, port, timeout, retries):
    """服务器配置 - 演示复杂选项和默认值"""
    click.echo(f"🚀 启动服务器配置:")
    click.echo(f"主机: {host}")
    click.echo(f"端口: {port}")
    click.echo(f"超时: {timeout}秒")
    click.echo(f"重试: {retries}次")
    
    # 模拟服务器启动过程
    with click.progressbar(range(10), label='启动中') as bar:
        for i in bar:
            time.sleep(0.1)
    
    click.echo("✅ 服务器启动完成!")

@cli.group()
def db():
    """数据库操作子命令组"""
    pass

@db.command()
@click.option('--name', required=True, help='数据库名称')
@click.option('--user', help='用户名')
@click.option('--password', help='密码')
def create(name, user, password):
    """创建数据库"""
    click.echo(f"创建数据库: {name}")
    if user:
        click.echo(f"用户: {user}")
    # 实际的创建逻辑...

@db.command()
@click.option('--name', required=True, help='数据库名称')
@click.option('--backup', is_flag=True, help='是否创建备份')
def delete(name, backup):
    """删除数据库"""
    if backup:
        click.echo(f"创建备份并删除数据库: {name}")
    else:
        click.echo(f"删除数据库: {name}")
    
    if not click.confirm('确认删除吗? 此操作不可逆!'):
        click.echo("操作已取消")
        return
    
    click.echo("✅ 数据库删除完成")

@cli.command()
@click.option('--style', type=click.Choice(['simple', 'fancy', 'minimal']), 
              default='simple', help='输出样式')
@click.option('--color/--no-color', default=True, help='是否彩色输出')
def theme(style, color):
    """主题设置 - 演示互斥选项和选择器"""
    click.echo(f"主题样式: {style}")
    click.echo(f"彩色输出: {'启用' if color else '禁用'}")
    
    if style == 'fancy' and color:
        click.echo(click.style("🎨 华丽的彩色主题!", fg='cyan', bold=True))
    elif style == 'minimal':
        click.echo("⚪ 极简风格")
    else:
        click.echo("🔵 简洁风格")

@cli.command()
@click.option('--date', type=click.DateTime(), default=str(datetime.now()),
              help='特定日期 (格式: YYYY-MM-DD)')
@click.option('--format', '-f', default='%Y-%m-%d %H:%M:%S', 
              help='日期格式')
def show_date(date, format):
    """日期时间演示 - 高级类型处理"""
    formatted = date.strftime(format)
    click.echo(f"📅 日期时间: {formatted}")

if __name__ == '__main__':
    cli()