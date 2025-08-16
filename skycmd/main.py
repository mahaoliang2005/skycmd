import click
from skycmd.weather.service import get_weather_from_wttr, get_detailed_weather_from_wttr


@click.command()
@click.argument("city", type=str, required=False)
@click.option("-v", "--verbose", is_flag=True, help="显示详细天气信息")
def main(city, verbose):
    """
    命令行天气工具 - 获取指定城市的天气信息

    \b
    使用示例：
      skycmd          # 获取帮助信息
      skycmd Shenzhen  # 获取深圳的天气
      skycmd -v Shenzhen  # 获取深圳的详细天气信息
    """
    if not city:
        # 如果没有提供城市名，显示帮助信息
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

    if verbose:
        # 显示详细天气信息
        weather_info = get_detailed_weather_from_wttr(city)
        print(weather_info)
    else:
        # 显示简单天气信息
        weather_info = get_weather_from_wttr(city)
        print("🌍 天气信息：")
        print(weather_info)


if __name__ == "__main__":
    main()
