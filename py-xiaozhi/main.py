import argparse
import asyncio
import sys
import signal

from src.application import Application
from src.utils.logging_config import get_logger, setup_logging

logger = get_logger(__name__)


def parse_args():
    """
<<<<<<< HEAD
    解析命令行参数.
    """
    parser = argparse.ArgumentParser(description="小智Ai客户端")
=======
    Parses command line parameters.
    """
    parser = argparse.ArgumentParser(description="Xiaozhi Ai Client")
>>>>>>> cab66c1 (1st commit)
    parser.add_argument(
        "--mode",
        choices=["gui", "cli"],
        default="gui",
<<<<<<< HEAD
        help="运行模式：gui(图形界面) 或 cli(命令行)",
=======
        help="run mode: gui (graphical interface) or cli (command line)",
>>>>>>> cab66c1 (1st commit)
    )
    parser.add_argument(
        "--protocol",
        choices=["mqtt", "websocket"],
        default="websocket",
<<<<<<< HEAD
        help="通信协议：mqtt 或 websocket",
=======
        help="Communication Protocol: mqtt or websocket",
>>>>>>> cab66c1 (1st commit)
    )
    parser.add_argument(
        "--skip-activation",
        action="store_true",
<<<<<<< HEAD
        help="跳过激活流程，直接启动应用（仅用于调试）",
=======
        help="Skip the activation process and start the application directly (for debugging only)",
>>>>>>> cab66c1 (1st commit)
    )
    return parser.parse_args()


async def handle_activation(mode: str) -> bool:
<<<<<<< HEAD
    """处理设备激活流程，依赖已有事件循环.

    Args:
        mode: 运行模式，"gui"或"cli"

    Returns:
        bool: 激活是否成功
=======
    """ handles the device activation process and relies on an existing event loop.

    Args:
        mode: Run mode, "gui" or "cli"

    Returns:
        bool: Whether the activation is successful
>>>>>>> cab66c1 (1st commit)
    """
    try:
        from src.core.system_initializer import SystemInitializer

<<<<<<< HEAD
        logger.info("开始设备激活流程检查...")

        system_initializer = SystemInitializer()
        # 统一使用 SystemInitializer 内的激活处理，GUI/CLI 自适应
        result = await system_initializer.handle_activation_process(mode=mode)
        success = bool(result.get("is_activated", False))
        logger.info(f"激活流程完成，结果: {success}")
        return success
    except Exception as e:
        logger.error(f"激活流程异常: {e}", exc_info=True)
=======
        logger.info("Start device activation process check...")

        system_initializer = SystemInitializer()
        #Use activation processing in SystemInitializer uniformly, GUI/CLI adaptive
        result = await system_initializer.handle_activation_process(mode=mode)
        success = bool(result.get("is_activated", False))
        logger.info(f"Activation process is completed, result: {success}")
        return success
    except Exception as e:
        logger.error(f"Activation process exception: {e}", exc_info=True)
>>>>>>> cab66c1 (1st commit)
        return False


async def start_app(mode: str, protocol: str, skip_activation: bool) -> int:
    """
<<<<<<< HEAD
    启动应用的统一入口（在已有事件循环中执行）.
    """
    logger.info("启动小智AI客户端")

    # 处理激活流程
    if not skip_activation:
        activation_success = await handle_activation(mode)
        if not activation_success:
            logger.error("设备激活失败，程序退出")
            return 1
    else:
        logger.warning("跳过激活流程（调试模式）")

    # 创建并启动应用程序
=======
    Start the unified entry to the application (execute in an existing event loop).
    """
    logger.info("Start Xiaozhi AI Client")

    # Process activation process
    if not skip_activation:
        activation_success = await handle_activation(mode)
        if not activation_success:
            logger.error("Defaulted to activation, program exit")
            return 1
    else:
        logger.warning("Skip activation process (debug mode)")

    # Create and start the application
>>>>>>> cab66c1 (1st commit)
    app = Application.get_instance()
    return await app.run(mode=mode, protocol=protocol)


if __name__ == "__main__":
    exit_code = 1
    try:
        args = parse_args()
        setup_logging()

<<<<<<< HEAD
        # 检测Wayland环境并设置Qt平台插件配置
=======
        # Detect Wayland environment and set the Qt platform plug-in configuration
>>>>>>> cab66c1 (1st commit)
        import os
        is_wayland = os.environ.get('WAYLAND_DISPLAY') or os.environ.get('XDG_SESSION_TYPE') == 'wayland'

        if args.mode == "gui" and is_wayland:
<<<<<<< HEAD
            # 在Wayland环境下，确保Qt使用正确的平台插件
            if 'QT_QPA_PLATFORM' not in os.environ:
                # 优先使用wayland插件，失败则回退到xcb（X11兼容层）
                os.environ['QT_QPA_PLATFORM'] = 'wayland;xcb'
                logger.info("Wayland环境：设置QT_QPA_PLATFORM=wayland;xcb")

            # 禁用一些在Wayland下不稳定的Qt特性
            os.environ.setdefault('QT_WAYLAND_DISABLE_WINDOWDECORATION', '1')
            logger.info("Wayland环境检测完成，已应用兼容性配置")

        # 统一设置信号处理：忽略 macOS 上可能出现的 SIGTRAP，避免“trace trap”导致进程退出
        try:
            if hasattr(signal, "SIGINT"):
                # 交由 qasync/Qt 处理 Ctrl+C；保持默认或后续由 GUI 层处理
                pass
            if hasattr(signal, "SIGTERM"):
                # 允许进程收到终止信号时走正常关闭路径
=======
            # In Wayland environment, make sure Qt uses the correct platform plug-in
            if 'QT_QPA_PLATFORM' not in os.environ:
                # Use the wayland plug-in first, and fall back to xcb (X11 compatibility layer) if it fails
                os.environ['QT_QPA_PLATFORM'] = 'wayland;xcb'
                logger.info("Wayland environment: set QT_QPA_PLATFORM=wayland;xcb")

            # Disable some unstable Qt features under Wayland
            os.environ.setdefault('QT_WAYLAND_DISABLE_WINDOWDECORATION', '1')
            logger.info("Wayland environment detection is completed, compatibility configuration has been applied")

        # Unified signal processing: Ignore SIGTRAP that may appear on macOS to avoid "trace trap" causing the process to exit
        try:
            if hasattr(signal, "SIGINT"):
                # Handle it to qasync/Qt to process Ctrl+C; keep it default or subsequently handled by the GUI layer
                pass
            if hasattr(signal, "SIGTERM"):
                # Allow the process to go to the normal closing path when it receives the termination signal
>>>>>>> cab66c1 (1st commit)
                pass
            if hasattr(signal, "SIGTRAP"):
                signal.signal(signal.SIGTRAP, signal.SIG_IGN)
        except Exception:
<<<<<<< HEAD
            # 某些平台/环境不支持设置这些信号，忽略即可
            pass

        if args.mode == "gui":
            # 在GUI模式下，由main统一创建 QApplication 与 qasync 事件循环
=======
            # Some platforms/environments do not support setting these signals, just ignore them
            pass

        if args.mode == "gui":
            # In GUI mode, create QApplication and qasync event loops uniformly from main
>>>>>>> cab66c1 (1st commit)
            try:
                import qasync
                from PyQt5.QtWidgets import QApplication
            except ImportError as e:
<<<<<<< HEAD
                logger.error(f"GUI模式需要qasync和PyQt5库: {e}")
=======
                logger.error(f"GUI mode requires qasync and PyQt5 libraries: {e}")
>>>>>>> cab66c1 (1st commit)
                sys.exit(1)

            qt_app = QApplication.instance() or QApplication(sys.argv)

            loop = qasync.QEventLoop(qt_app)
            asyncio.set_event_loop(loop)
<<<<<<< HEAD
            logger.info("已在main中创建qasync事件循环")

            # 确保关闭最后一个窗口不会自动退出应用，避免事件环提前停止
=======
            logger.info("qasync event loop has been created in main")

            # Make sure that the last window is closed and the application will not automatically exit, and avoid the event ring being stopped early
>>>>>>> cab66c1 (1st commit)
            try:
                qt_app.setQuitOnLastWindowClosed(False)
            except Exception:
                pass

            with loop:
                exit_code = loop.run_until_complete(
                    start_app(args.mode, args.protocol, args.skip_activation)
                )
        else:
<<<<<<< HEAD
            # CLI模式使用标准asyncio事件循环
=======
            # CLI mode uses standard asyncio event loop
>>>>>>> cab66c1 (1st commit)
            exit_code = asyncio.run(
                start_app(args.mode, args.protocol, args.skip_activation)
            )

    except KeyboardInterrupt:
<<<<<<< HEAD
        logger.info("程序被用户中断")
        exit_code = 0
    except Exception as e:
        logger.error(f"程序异常退出: {e}", exc_info=True)
        exit_code = 1
    finally:
        sys.exit(exit_code)
=======
        logger.info("Program interrupted by user")
        exit_code = 0
    except Exception as e:
        logger.error(f"Program Exit exception: {e}", exc_info=True)
        exit_code = 1
    finally:
        sys.exit(exit_code)
>>>>>>> cab66c1 (1st commit)
