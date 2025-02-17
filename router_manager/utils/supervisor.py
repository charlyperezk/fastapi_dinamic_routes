from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from functools import wraps
from pydantic import BaseModel
from router_manager.utils.parse_response import format_data


class Supervisor:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def supervise(self,
                  success_message: Optional[str] = None,
                  success_status_code: Optional[int] = None,
                  error_message: Optional[str] = None,
                  error_status_code: Optional[int] = None,
                  return_method_response: Optional[bool] = False,
                  session: Session = None
                  ):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    result = await func(*args, **kwargs)

                    if return_method_response:
                        if isinstance(result, BaseModel):
                            content = format_data(result.dict())
                        if isinstance(result, list):
                            content = list(map(lambda x: format_data(x.dict()), result))
                        if isinstance(result, str):
                            content = result
                        
                    else:
                        content = success_message

                    if session:
                        session.commit()

                    return JSONResponse(
                        status_code=200 if not success_status_code else success_status_code,
                        content={"message": content}
                    )

                except Exception as e:
                    if session:
                        session.rollback()
                    if error_message:
                        print(error_message)
                        print(e)
                    raise HTTPException(
                        status_code=400 if not error_status_code else error_status_code,
                        detail=str(e) if not error_message else error_message
                    )
            return wrapper
        return decorator