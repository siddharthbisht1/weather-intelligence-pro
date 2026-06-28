from fastapi import HTTPException


def require_role(
    user_role: str,
    required_role: str
):

    if (
        user_role.lower()
        !=
        required_role.lower()
    ):

        raise HTTPException(

            status_code=403,

            detail=f"{required_role.capitalize()} access required"

        )

    return True