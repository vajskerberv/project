from functools import wraps

from typing import Optional, Callable, Any

def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Функция-декоратор логирует начало и конец выполнения функции, её результат или ошибку выполнения.
    В зависимости от аргумента filename делает запись в файл
    или вывод в консоль (по умолчанию - вывод в консоль)
    """

    def decorator(func) -> Callable[..., Any]:
       @wraps(func)
       def wrapper(*args, **kwargs) -> Any:
          try:
             result = func(*args, **kwargs)
             logging = f"{func.__name__} ok, {result}\n"
             if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(logging)
             else:
                print(logging)
             return result
          except Exception as e:
              logging = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
              if filename:
                  with open(filename, "a", encoding="utf-8") as file:
                      file.write(logging)
              else:
                  print(logging)
              raise
       return wrapper
    return decorator
